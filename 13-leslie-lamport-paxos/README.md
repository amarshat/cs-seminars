# Reading Leslie Lamport

## *The Part-Time Parliament* and *Paxos Made Simple*

> Leslie Lamport, "The Part-Time Parliament," ACM Transactions on Computer Systems, Volume 16, Number 2, May 1998, pages 133 to 169 (written and first submitted around 1990; also SRC Research Report 49).
>
> Leslie Lamport, "Paxos Made Simple," ACM SIGACT News, Volume 32, Number 4, December 2001, pages 51 to 58.

This is the theoretical center the series has been circling since the fourth seminar. The question is the oldest one in distributed systems: how can a group of processes that crash, restart, and talk over a network that loses, delays, and duplicates messages nonetheless agree on a single value? Agree on one value and you can, by repeating the trick, agree on an ordered sequence of them, which is a replicated log, which is a fault-tolerant replicated state machine, which is how essentially every serious distributed system keeps its copies consistent. Paxos is the canonical answer, and Lamport is its author.

The genius of the protocol is how little it needs. Choose a value when a majority of acceptors accept it, and rely on one fact: any two majorities share at least one member. Add one rule: before proposing, a proposer must ask a majority what they have already accepted and adopt the highest-numbered value among the answers. From those two ideas the whole safety argument follows almost unavoidably. Once a value is chosen, every later proposer is forced to re-propose it, so no second value can ever be chosen. That guarantee is unconditional. It survives any pattern of delays, losses, and crashes.

What Paxos does not do is equally important, and this is the part most retellings get wrong. It does not beat the impossibility result the fourth seminar flagged. In a fully asynchronous system with even one crash, no algorithm can guarantee that consensus is ever reached, and Paxos is no exception. It guarantees safety always and progress only conditionally, when a single stable leader can talk to a majority and messages arrive in time. Two proposers dueling with ever-higher numbers can block each other forever. Lamport says this himself. Safety is a theorem; liveness is a hope backed by a timeout.

## Why this seminar, thirteenth

This is Leslie Lamport's second appearance, and it closes a loop the series opened long ago. His own 1978 work on logical clocks seeded the state-machine approach that Paxos makes fault-tolerant, and it set up the world with no global clock in which a process cannot tell a crashed peer from a slow one. Barbara Liskov's Viewstamped Replication reached an equivalent crash-fault-tolerant protocol from the systems side in 1988, independently, and Lamport's paper acknowledges the equivalence. Jim Gray showed that two-phase commit blocks and pointed at the consensus problem that Paxos answers. Read together, these are four approaches to one question, and Paxos is its sharpest theoretical statement.

There is a lovely human thread, too. The paper sat unpublished for years because reviewers thought its Greek-parliament allegory was a joke, and the one person who immediately understood its importance was Butler Lampson, whose own seminar sits earlier in this series. And the seminar sets up the next step in the argument: Paxos tolerates crashes but assumes no one lies, so the Byzantine case, where components may be actively malicious, is the Castro and Liskov seminar still to come.

## The four questions

1. **What problem was Lamport solving?** How a collection of unreliable processes agree on one value, and, by repetition, on an ordered log of commands, which is the foundation of fault-tolerant replicated state machines. The processes may crash and restart, and the network may lose, delay, and duplicate messages, but no one is malicious.
2. **Why was the answer surprising?** Because it guarantees safety, that two processes never disagree on the chosen value, unconditionally, through any delays, losses, and crashes, while honestly conceding that it cannot guarantee progress in a fully asynchronous system. And because the whole protocol falls out of two simple ideas: majorities intersect, and a proposer must adopt the highest-numbered value already accepted.
3. **What survived?** All of it. Paxos, and its deliberately understandable cousin Raft, is how modern systems agree: Chubby, Spanner, ZooKeeper, etcd, Consul, CockroachDB, Kafka, and more. The replicated log is the universal coordination primitive. What stayed contested is readability, which is why "Paxos Made Simple" exists and why Raft was designed to be teachable.
4. **How should a working engineer read it today?** As the canonical account of what consensus can and cannot do: safety always, liveness only with a stable leader. Keep single-decree Paxos, the safety heart, distinct from Multi-Paxos, which adds the log and the leader. And read the history as a caution about how a field treats an idea it does not immediately understand.

## Chapters

1. [The consensus problem](01-the-consensus-problem.md). What agreement means, the three roles, the crash-asynchronous model, and why a process cannot tell a dead peer from a slow one.
2. [Majorities intersect](02-majorities-intersect.md). The one fact the whole protocol rests on, and why quorum intersection is the same math as Liskov's 2f+1.
3. [The Synod, and the safety trick](03-the-synod-and-the-safety-trick.md). Single-decree Paxos: two phases, ballot numbers, and the rule that once a value is chosen it can never be unchosen.
4. [Safety always, liveness sometimes](04-safety-always-liveness-sometimes.md). Dueling proposers, the distinguished leader, and why Paxos does not, and cannot, beat FLP.
5. [From one value to a log](05-from-one-value-to-a-log.md). Multi-Paxos and the state machine: a sequence of instances, a stable leader that skips phase one, and how the log gets its order.
6. [The strangest famous paper](06-the-strangest-famous-paper.md). The allegory, the eight-year rejection, and why the paper that founded modern consensus was almost lost.
7. [Modern echoes](07-modern-echoes.md). Chubby and Spanner on Paxos, the Raft systems, the replicated log as coordination primitive, and where each follows the single-decree core.
8. [Discussion and further reading](08-discussion-and-reading.md). The argument in one breath, questions to argue about, and where the series goes next.

## A note on the sources

Quotations come from both papers, with the protocol taken from the readable "Paxos Made Simple" and the allegory and history from "The Part-Time Parliament." This seminar keeps several things straight. Paxos guarantees safety unconditionally and liveness only with a stable leader, so it does not solve asynchronous consensus outright, and saying it does is the most common error. Single-decree Paxos, which agrees on one value, is distinct from Multi-Paxos, which builds the log. Proposal numbers are unique ordered ballots drawn from disjoint sets per proposer, not values and not timestamps. Paxos is crash-tolerant, not Byzantine, which is a later seminar. It is convergent with Liskov's Viewstamped Replication, not first and not derived from it. And it is famously hard to implement correctly, which is why Raft and "Paxos Made Live" exist, so this seminar does not present it as the clean end of the story.
