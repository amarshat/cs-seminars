# Reading Jeff Dean and Sanjay Ghemawat

## Three papers, one arc: MapReduce, Bigtable, Spanner

> Jeffrey Dean and Sanjay Ghemawat, "MapReduce: Simplified Data Processing on Large Clusters," OSDI 2004, built on Sanjay Ghemawat, Howard Gobioff, and Shun-Tak Leung, "The Google File System," SOSP 2003.
>
> Fay Chang and colleagues, "Bigtable: A Distributed Storage System for Structured Data," OSDI 2006.
>
> James C. Corbett and colleagues, "Spanner: Google's Globally-Distributed Database," OSDI 2012.

This seminar is shaped differently from the others. It is not one deep read of a single result. It is an arc across four papers and roughly a decade, from a research lab that had to invent, in public, how to store and process data on tens of thousands of unreliable commodity machines. Jeffrey Dean and Sanjay Ghemawat are the recurring names, co-authors on all four papers, though Bigtable and Spanner are large-team efforts led by others. Follow their lineage and you watch an entire field change its mind twice.

The story is a pendulum. MapReduce makes one move: restrict the programming model to two functions, map and reduce, and the framework can then handle everything hard about running on a thousand machines, including failure, by simply re-executing the pieces that die. Bigtable makes the opposite move from the database tradition: throw away the relational model, joins, SQL, and transactions across rows, and you can spread a single sorted map across thousands of servers in a way a 2006 relational database could not. That was the turn the industry later called NoSQL, and its tradeoffs were real. Then Spanner swings back. It brings SQL, general ACID transactions, and global consistency to a database running on machines all over the planet, and it does so not by abandoning the earlier lessons but by composing them.

That composition is why this seminar sits where it does. Spanner is where the book's distributed-data threads meet. It runs the two-phase commit of Jim Gray's transaction seminar, over shards that are each replicated by Paxos from the Lamport seminar, which is the same crash-fault-tolerant replication Barbara Liskov reached independently, ordered globally by synchronized physical clocks of the kind Lamport's earliest seminar described, serving a query language descended from Codd's relational model. Bigtable's coordination service, Chubby, is Paxos put into production. The classics did not get replaced by the internet giants. They got assembled.

## Why this seminar, fourteenth

The book has spent thirteen seminars building primitives: relational data, transactions, logical and physical time, replication, consensus. This is where a working system picks them up at once. It is the convergence seminar, and reading it as an arc rather than three separate papers is the point. Each paper is represented by a single key mechanism, MapReduce by re-execution, Bigtable by the sparse sorted map and Chubby, Spanner by TrueTime and commit-wait, and each mechanism is grounded in its own paper's words. The aim is not to exhaust three dense systems papers. It is to see the pendulum swing, and to see what it swings on.

## The four questions

1. **What problem were they solving?** How to store and process internet-scale data on thousands of failure-prone commodity machines. The same lab asked it three times across a decade: batch processing (MapReduce), structured storage (Bigtable), and a globally consistent transactional database (Spanner).
2. **Why were the answers surprising?** Each inverted the previous decade's instinct. Restrict the programming model and the framework can hide distribution and failure. Discard joins and multi-row transactions and a sorted map scales across thousands of machines. Then, most surprising, bring SQL and ACID and global consistency back, by measuring clock uncertainty with atomic clocks and waiting it out so distributed timestamps mean something.
3. **What survived?** The lineage seeded the modern data stack. MapReduce led to Hadoop and then Spark; Bigtable to HBase, Cassandra, and the log-structured storage engines now everywhere; Chubby to ZooKeeper and etcd; Spanner to Google Cloud Spanner and the distributed-SQL systems CockroachDB, YugabyteDB, and TiDB. What got replaced was rigid map-then-reduce and the belief that scale required giving up SQL.
4. **How should a working engineer read it today?** As a pendulum, not a march of progress. The NoSQL tradeoffs were genuine, Spanner's return needed a decade of datacenter clock infrastructure, and Spanner does not beat the CAP theorem. And as convergence: the classics were composed, not superseded.

## Chapters

1. [The arc and the pendulum](01-the-arc-and-the-pendulum.md). Three papers, a decade, and the swing from relational to NoSQL and back.
2. [MapReduce: fault tolerance by re-execution](02-mapreduce-re-execution.md). Restrict the model to two functions, and the framework can make failure invisible by re-running the deterministic pieces.
3. [Bigtable: the sparse sorted map](03-bigtable-the-sorted-map.md). What you give up to shard structured data across thousands of machines, and the storage engine that made it work.
4. [Chubby: Paxos in production](04-chubby-paxos-in-production.md). Factor consensus into one lock service and let every other system lean on it.
5. [Spanner I: transactions over Paxos groups](05-spanner-transactions-over-paxos.md). Two-phase commit was fragile because a participant could die; replicate each participant with Paxos and it becomes durable.
6. [Spanner II: TrueTime and commit-wait](06-spanner-truetime-and-commit-wait.md). You cannot make clocks perfect, so measure how wrong they might be and wait out the error.
7. [Convergence, and the CAP honesty](07-convergence-and-cap.md). The threads meet in Spanner, and Spanner is a CP system, not a defeat of CAP.
8. [Discussion and further reading](08-discussion-and-reading.md). The argument in one breath, questions to argue about, and where the series goes next.

## A note on the sources

Quotations are grounded in each paper's own words. This seminar keeps several things straight. Dean and Ghemawat are the recurring co-authors, but Bigtable is Chang and colleagues and Spanner is Corbett and colleagues, so the teams get the credit. MapReduce is a batch programming model, not a database and not Hadoop, which is the later open-source reimplementation. Bigtable is not relational: single-row atomic operations only, no joins, no SQL at first, and it is best described in its own terms, a sparse multi-dimensional sorted map, not through the marketing category that came later. Spanner does not beat CAP; it is a consistent system that can become unavailable under a partition, and Google's network simply makes partitions rare, a point Eric Brewer made himself. TrueTime does not give perfect clocks; it exposes clock uncertainty as a bounded interval and waits it out. And the distributed-SQL systems that followed Spanner use software clocks, not its atomic-clock hardware.
