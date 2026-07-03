# Reading Barbara Liskov

## *Viewstamped Replication*

> Brian M. Oki and Barbara H. Liskov, "Viewstamped Replication: A New Primary Copy Method to Support Highly-Available Distributed Systems," PODC 1988, pages 8 to 17. Read alongside Barbara Liskov and James Cowling, "Viewstamped Replication Revisited," MIT-CSAIL-TR-2012-021, July 2012.

The Lamport seminar ended on an admission. Lamport had shown how to replicate a state machine by feeding every copy the same totally ordered log of commands, and then said, in plain words, that his algorithm halts the moment a single process fails, because it needs to hear from all of them. Fault tolerance, he wrote, was beyond the scope of that paper. This seminar reads the work that finished the job.

Viewstamped Replication is the concrete, crash-tolerant realization of state-machine replication. It answers the question Lamport set aside: how do you keep a replicated log making progress, in the same agreed order, when machines keep crashing and recovering and the network keeps dropping and reordering messages? The answer has two moving parts, and the protocol is the interaction between them. In normal operation a single replica, the primary, picks the order and the others follow, which is cheap and fast. When the primary fails, a view change installs a new one, and the delicate part is that the new regime must inherit every operation the old one had already committed, with nothing lost and nothing reordered. VR makes that guarantee rest on a single arithmetic fact: any two majorities of the replicas share at least one member.

There is a naming hazard to clear up front, because this work exists in two quite different forms. The 1988 paper presents VR wrapped inside a distributed transaction system, with two-phase commit, locking, and a database's worth of machinery around it. The 2012 "Revisited" report, by Liskov and Cowling, strips all of that away and presents VR as pure state-machine replication, and it is the version most engineers mean today. This seminar reads both and is careful about which is which, because the clean protocol people quote, with its PREPARE and PREPAREOK and COMMIT messages, is the 2012 formulation, not the 1988 one.

## Why this seminar, fifth

The series has been building toward agreement under failure. Hewitt and Hoare gave two models of communication. Lamport showed that ordering events is the real problem and gave the state-machine recipe, then hit the wall: you cannot tell a crashed machine from a slow one, so an algorithm that waits for everyone stops forever the first time anyone dies. VR is the first work in this series to walk through that wall. It does not need to hear from everyone, only from a majority, and that single relaxation, plus a protocol to change leaders safely, is enough to keep a replicated service alive across the failures that Lamport's algorithm could not survive.

## The four questions

1. **What problem was Liskov solving?** How to keep a replicated service correct and available while machines crash and recover and the network misbehaves, without needing every replica to be up, and without ever losing a committed operation or reordering the log.
2. **Why was the answer surprising?** Because it makes an unreliable leader safe. A primary can crash mid-operation, two primaries can briefly coexist during a partition, and the protocol still never loses committed work. The safety does not come from perfect failure detection, which is impossible; it comes from majority quorums that always overlap.
3. **What survived?** Almost all of it, under other names. The leader-orders-a-log shape, the majority-acknowledge-before-commit rule, and the leader-change-that-preserves-committed-entries protocol are the skeleton of Raft, Multi-Paxos, Zab, and every production replicated log built since.
4. **How should a working engineer read it today?** As the clearest early statement of the pattern you now reach for by default when you need a replicated, consistent log, and as the place where the view change, the part everyone underestimates, was first gotten right.

## Chapters

1. [The unfinished business](01-the-unfinished-business.md). From Lamport's halting state machine to a protocol that survives crashes, and the failure model that makes it possible.
2. [The primary imposes the order](02-the-primary-imposes-order.md). Normal-case operation: PREPARE, PREPAREOK, COMMIT, and how a leader realizes Lamport's total order cheaply.
3. [Why 2f+1](03-quorum-intersection.md). The arithmetic the protocol rests on, and why any two majorities must overlap.
4. [The view change](04-the-view-change.md). Where correctness lives: changing leaders without losing a committed operation, and why the old primary must be shut out.
5. [1988 versus 2012](05-1988-vs-2012.md). Two versions of one idea: the transaction-bound original, the clean state-machine revisit, and where the name came from.
6. [VR and its family](06-vr-and-its-family.md). Paxos, Raft, Zab, and the modern replicated logs, with the map from "view" to "term" and "epoch."
7. [Discussion and further reading](07-discussion-and-reading.md). Questions to argue about, and where the series goes next.

## A note on the sources

Quotations come from the 1988 PODC paper and the 2012 "Revisited" report. This seminar keeps three things carefully apart from VR itself. Paxos, developed independently and at about the same time by Lamport, is the subject of a later seminar; VR and Paxos converged, neither copied the other, and the 2012 report says so directly. Byzantine fault tolerance, where replicas can lie rather than merely crash, is PBFT (Castro and Liskov, 1999), a separate later seminar and the sequel to this one. And state-machine replication as a general fault-tolerant technique was named and surveyed by Schneider in 1990. VR is the crash-tolerant protocol that makes the pattern real.
