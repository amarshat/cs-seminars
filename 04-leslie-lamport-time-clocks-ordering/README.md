# Reading Leslie Lamport

## *Time, Clocks, and the Ordering of Events in a Distributed System*

> Leslie Lamport, Communications of the ACM, Volume 21, Number 7, July 1978, pages 558 to 565.

The two previous seminars, on Hewitt's actors and Hoare's CSP, both take an ordering of events for granted. An actor's events form a causal sequence; a CSP process is a sequence of communications. Neither asks the awkward question underneath: when two things happen on two different machines, which one happened first? Lamport asked it, and his answer is that the question usually has no answer, and that most bugs in distributed systems come from people not noticing.

This is the paper that taught the field to stop believing in a global clock. Its central move is deflationary. There is no universal "now" that separated machines can read, so "happened before" cannot mean "earlier on the wall clock." Lamport rebuilds the relation from the only thing the system can actually observe, which messages were sent and received, and shows that what you get is not a timeline but a partial order. Some pairs of events are ordered by cause. Many pairs are simply concurrent, with no fact about which came first. Then he shows how to bolt a logical clock onto that partial order to get a usable total order, and, in a second half most people forget, how the whole scheme breaks when information leaks around the system through a side channel, and what physical clocks can and cannot do about it.

Two of the ideas seeded here grew into the backbone of modern distributed systems: the causal partial order that vector clocks, Git, and Kafka all rest on, and the state-machine replication that consensus protocols implement. This seminar is careful about that word "seeded," because the 1978 paper starts those lines without finishing them, and Lamport himself finishes one of them in a later paper that gets its own seminar in this series.

## Why this seminar, fourth

Hewitt and Hoare gave two answers to how independent things communicate. Both quietly assume that when a message is sent and received, the order is clear. Lamport is the one who stares at the assumption and finds it wanting. His partial order is the same shape as Hewitt's "arrow of time" and the sequences in Hoare's CSP, but he is the first to make it the subject rather than the scenery, and the first to give a running system a way to compute with it. Read him after the concurrency pair and the through-line snaps into focus: coordinating independent processes is really about agreeing on an order of events, and agreement, it turns out, is the hard part the whole field spends the next forty years on.

## The four questions

1. **What problem was Lamport solving?** How to reason about the order of events across machines that have no shared clock, and how to give such a system a consistent ordering it can actually use.
2. **Why was the answer surprising?** Because it threw out physical time as the basis for ordering. "Happened before" became a partial order defined by causality, not a comparison of timestamps, and Lamport showed that treating it as a timeline is where the bugs come from.
3. **What survived?** The happened-before partial order is now foundational: vector clocks, version vectors, Git's DAG, and Kafka's per-partition ordering are all built on it. The state-machine idea seeded here became state-machine replication. The scalar logical clock itself was superseded by vector clocks for detecting concurrency.
4. **How should a working engineer read it today?** As the source of the mental model that stops you writing distributed-systems bugs: there is no global now, a timestamp is not a time, and using physical clocks to stand in for causality is a hazard, not a shortcut.

## Chapters

1. [There is no now](01-there-is-no-now.md). Why time in a distributed system has to be rebuilt from order, not the other way around.
2. [Happened-before](02-happened-before.md). The partial order, concurrency as incomparability, and Lamport's own relativity analogy.
3. [Logical clocks](03-logical-clocks.md). Counting causality with a counter, the clock condition, and why a timestamp is not a time.
4. [The total order and its price](04-total-order-and-its-price.md). Completing the partial order arbitrarily, the mutual-exclusion algorithm, and the seed of state-machine replication.
5. [The forgotten half: physical clocks](05-physical-clocks-and-the-anomaly.md). The out-of-band anomaly, the strong clock condition, and how closely real clocks can be synchronized.
6. [Modern echoes](06-modern-echoes.md). Vector clocks, Git, Kafka, Spanner's TrueTime, hybrid logical clocks, and the last-write-wins hazard.
7. [Discussion and further reading](07-discussion-and-reading.md). Questions to argue about, and where the series goes next.

## A note on the source

Quotations come from the 1978 CACM paper (pages 558 to 565). This seminar keeps two lines carefully separated from the paper: state-machine replication as a fault-tolerant technique (named and surveyed by Schneider in 1990) and consensus (Lamport's own Paxos, in *The Part-Time Parliament*, written around 1990 and published in 1998). The 1978 paper seeds the state-machine idea and says outright that its algorithm halts if a single process fails. Making that survivable is the subject of a later seminar, not this one.
