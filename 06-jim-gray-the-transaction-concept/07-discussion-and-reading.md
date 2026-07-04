# 7. Discussion and further reading

## The argument in one breath

Gray took a mess that every application programmer was solving by hand, the half-done change after a crash, the read of data that later got rolled back, and named a single abstraction that makes it disappear: the transaction, borrowed from contract law, with the properties of atomicity, consistency, and durability, invoked by three verbs, BEGIN, COMMIT, ABORT. He showed two ways to build it, versioning and logging plus locking, and argued they are the same idea underneath. He reduced concurrency correctness to one rule, see another transaction's committed inputs but never its uncommitted outputs, and built it out of locks, without ever naming it isolation. He gave the atomic commit across nodes its handshake, two-phase commit, the minister asking "do you." And then, in the half of the paper the folklore forgets, he turned on his own idea and showed where it breaks: nested and long-lived processes, where you must compensate rather than undo, which is the saga before it had the name.

Read it as one leg of a tripod. Ordering and replication keep systems alive and agreeing; the transaction keeps their state correct; and the modern distributed database stacks the transaction on top of the replicated log.

## Questions worth arguing about

These are seminar questions. Several have no settled answer.

1. **Three properties or four?** Gray named atomicity, consistency, durability. Haerder and Reuter added isolation and coined ACID. Was isolation always hiding inside consistency, so the addition just made it explicit, or is it a genuinely different kind of guarantee, the only one that comes in degrees? Why is it always the one systems relax first?

2. **Is "consistency" even the database's job?** Gray's C means preserving the declared consistency constraints. Many modern practitioners argue the C in ACID is really the application's responsibility, and that the database only supplies A, I, and D. Where do you draw that line in systems you have built?

3. **When is a distributed transaction worth it?** Chapter 4 showed why microservices avoid two-phase commit and reach for sagas. But sagas expose intermediate state and push compensation logic into the application. When is the operational cost of real distributed transactions (Spanner-style, on consensus) the better buy than the complexity of getting every compensation right?

4. **Compensation is not undo.** A rolled-back transaction leaves no trace; a compensated one leaves the original action and its reversal both visible, and the window between them is real. When does that window matter, refunds, cancellations, sent emails, and what have you shipped that quietly assumed compensation was as clean as rollback?

5. **Did BASE win or lose?** The 2000s declared ACID incompatible with scale. NewSQL declared that wrong. Which was the fashion and which was the physics? For your workload, is eventual consistency a deliberate trade or a habit inherited from a decade that could not yet build transactions on consensus?

6. **The log or the state?** Gray kept the state primary and the log as history; event-sourced systems invert it. Which is the right primary for your data, and what do you gain and lose by choosing the log, ordering and audit for free, but every read becomes a projection?

## Further reading

Start with the paper, both halves, then follow the two threads it opens.

- **Jim Gray, "The Transaction Concept: Virtues and Limitations" (VLDB 1981).** The source. Short and readable, and the second half on nested and long-lived transactions is the part to reread, because it is the part that predicted the present.

- **Haerder and Reuter, "Principles of Transaction-Oriented Database Recovery" (ACM Computing Surveys, 1983).** Where isolation becomes a named property and ACID is coined. Read it against Gray to see exactly what was added and when.

- **Gray, "Notes on Database Operating Systems" (1978).** Gray's fuller treatment of locking granularity and two-phase commit, the technical companion to the 1981 synthesis.

- **Eswaran, Gray, Lorie, Traiger, "The Notions of Consistency and Predicate Locks in a Database System" (CACM 1976).** The formal footing under chapter 3: serializability, two-phase locking, predicate locks.

- **Skeen, "Nonblocking Commit Protocols" (SIGMOD 1981).** The paper that names 2PC's blocking flaw and adds the third phase. The bridge from Gray's handshake to consensus.

- **Garcia-Molina and Salem, "Sagas" (SIGMOD 1987).** The naming and formal treatment of the long-lived, compensating transaction Gray sketched. The direct ancestor of the microservice saga pattern.

- **Gray and Reuter, *Transaction Processing: Concepts and Techniques* (1993).** The thousand-page canonical text, if you want the whole field from the person who named it.

## Where the series goes next

Gray's transaction is the correctness half of the story, and it leaves one debt that the rest of the series pays.

- The atomic commit of chapter 4 blocks when its coordinator fails, and Gray's own two-phase commit cannot fix that alone. Making agreement survive the failure of the agreer is the **consensus** problem, and it is **Lamport's Paxos**, a later seminar here. The user of this series was right to see the ordering thread, the replication thread, and the 2PC-blocking thread all pointing at the same destination: a protocol for irrevocable agreement among unreliable machines.
- The previous seminar, **Liskov's Viewstamped Replication**, was in its original form replicating a transaction system running Gray's commit protocol; read the two together and the transaction layer and the replication layer click into place.
- And the reliability framing that opened this paper, fail-fast modules, process pairs, a reliable system from unreliable parts, is the same lineage as **Armstrong's** failure-oriented architecture. The transaction is to Gray's process pairs what OTP is to Armstrong's raw processes: the reusable abstraction that lets ordinary programmers inherit fault tolerance they did not write.

Read this way, Gray's paper is not just where transactions come from. It is where the field admitted that correctness under failure needs its own abstraction, and then, honestly, listed everything that abstraction could not yet do.
