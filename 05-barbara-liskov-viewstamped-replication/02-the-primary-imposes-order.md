# 2. The primary imposes the order

## The problem: who decides the order?

State-machine replication reduces to one requirement, stated cleanly in the 2012 report: replicas "start in the same initial state," operations are "deterministic," and so "replicas will end up in the same state if they execute the same sequence of operations." The whole game is that last phrase. Every replica must execute the same sequence, in the same order, despite clients firing requests concurrently from everywhere and replicas failing partway through. Lamport's 1978 scheme built that order by having every replica timestamp events and merge them, which is elegant and leaderless and, as the last seminar showed, halts if anyone stops responding. VR needs an order that survives failure and costs little in the common case. The question is who produces it.

## Why the obvious fix fails: agreeing on each step is expensive

You could run a fresh agreement protocol for every single operation: propose operation number 100, have the replicas vote, reach consensus on what 100 is, then move to 101. This is correct, and it is roughly what a leaderless consensus protocol does. It is also wasteful. Every operation pays for a full round of proposing and voting among peers, with the contention and extra message rounds that implies, and nobody is in charge, so two replicas can propose different operations for the same slot and burn rounds resolving the conflict. When the common case is "the leader is up and healthy for hours at a time," paying the full price of distributed agreement on every operation is a bad trade.

## Liskov's move: one primary orders, a majority confirms

VR's normal case is deliberately cheap. One replica is the primary, and its job is to impose the order: it receives client requests, assigns each the next slot in the log, and tells the backups. The backups do not vote on the order; they accept the primary's choice. Ordering, the thing that was hard, becomes trivial, because a single machine picking numbers in sequence is trivially consistent with itself. The difficulty is displaced entirely into what happens when the primary fails, which is the next two chapters. In exchange, the common case is close to free.

The clean statement of this protocol, with the message names everyone quotes, is the 2012 "Revisited" report, not the 1988 paper; the 1988 version did the same work buried inside transaction processing, which chapter 5 untangles. Here is the 2012 normal case. Each replica keeps a `view-number`, a `log` of operations, an `op-number` marking the latest slot filled, and a `commit-number` marking the latest slot known to be committed.

```mermaid
sequenceDiagram
    participant C as client
    participant P as primary
    participant B as backups (f of them)
    C->>P: REQUEST(op)
    Note over P: advance op-number,<br/>append op to log
    P->>B: PREPARE(view, op, op-number, commit-number)
    Note over B: append to log in order
    B->>P: PREPAREOK(view, op-number)
    Note over P: on f PREPAREOKs → committed;<br/>execute via up-call
    P->>C: REPLY(result)
    Note over P,B: next PREPARE (or COMMIT) carries the new commit-number
```

Walk the steps, because the details are where the guarantees hide. The client sends its request to the primary. The primary advances the `op-number`, appends the request to its log, and sends a `PREPARE` message carrying the current view, the request, the assigned `op-number`, and its current `commit-number`. Backups "process PREPARE messages in order": a backup will not accept the operation at slot `n` until it already has every earlier slot, fetching them by state transfer if it has fallen behind. Only then does it append the operation and reply `PREPAREOK`. The primary waits for `PREPAREOK` from `f` different backups. At that point the operation, and every operation before it, is committed, because it now sits in the logs of `f+1` replicas: the primary plus the `f` backups that answered. The primary executes the operation with an up-call to the service code, increments its `commit-number`, and replies to the client.

Notice what "committed" means here, because it is the hinge of the protocol: an operation is committed exactly when `f+1` replicas have it in their logs. Not when the primary has it, not when the client is told, but when a majority holds it. That is the fact the view change will lean on in chapter 4, and the reason it is safe is the arithmetic of chapter 3.

One more efficiency detail to keep. The primary does not send a separate message to announce commits. It piggybacks the `commit-number` on the next `PREPARE`, so backups learn that slot `n` committed when they receive the prepare for slot `n+1`. Only if the primary goes idle, with no new requests to carry the news, does it send a standalone `COMMIT` message. Commit information rides along for free whenever the system is busy, which is when it matters.

And, pointedly, none of this touches disk. The 2012 report is explicit: "The protocol does not require any writing to disk. For example, replicas do not need to write the log to disk when they add the operation to the log." Durability comes from replication, not from stable storage. An operation is safe because `f+1` machines hold it in memory, and by assumption no more than `f` fail at once, so at least one survivor always remembers it. This was a deliberate bet, present already in 1988, that talking to a majority of peers is cheaper than forcing a write to disk, and it is why VR is fast.

## The modern echo, stated precisely

This is Raft's normal case, almost line for line, which is no accident given Raft cites VR as its nearest relative. A Raft leader appends a client command to its log, sends `AppendEntries` to the followers, and marks the entry committed once a majority has stored it, then applies it to the state machine. Rename `PREPARE` to `AppendEntries`, `PREPAREOK` to a successful append response, `view` to `term`, and you have VR's normal case. Multi-Paxos reaches the same structure from the other direction: rather than run the full two-phase Paxos per operation, it elects a stable leader that skips the first phase and streams operations, precisely to avoid the per-operation agreement cost this chapter opened with. The industry converged, hard, on exactly VR's answer: let one leader impose the order, and commit on a majority acknowledgment. The interesting part, the part that separates a real protocol from a plausible sketch, is what happens when that leader dies, and that is next.

> **Principle:** Make the common case cheap by letting one leader impose the order, and define an operation as committed the moment a majority holds it, not the moment the leader does. Push all the difficulty into leader change, where it can be handled once.
