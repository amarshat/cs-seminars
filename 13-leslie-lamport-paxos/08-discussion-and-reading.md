# 8. Discussion and further reading

## The argument in one breath

Paxos is how unreliable processes agree. Choose a value when a majority of acceptors accept it, and lean on the one fact that any two majorities intersect, so two different values can never both be chosen. Add the rule that a proposer must first ask a majority what they have already accepted and adopt the highest-numbered answer, and once a value is chosen every later proposer is forced to re-propose it, so the choice is permanent. That is the two-phase Synod, and its safety is a theorem that holds through any delay, loss, duplication, or crash. What it cannot promise is progress: in a fully asynchronous system, dueling proposers can block each other forever, and no deterministic algorithm can guarantee otherwise, so Paxos gives up guaranteed liveness and buys it back with a stable leader and timeouts. Run one instance per log slot, elect a stable leader that runs phase one once and thereafter needs only phase two, and single-value consensus becomes a replicated log, which is a fault-tolerant state machine. The idea was almost lost to an eight-year publication delay because it was dressed as a Greek parliament, and it took a plain rewrite and a rival built for clarity to make it teachable.

Read in the series, this is the payoff of the consensus thread: Lamport's own state-machine seed and the dead-versus-slow impossibility, Liskov's independent and equivalent systems-side answer, and Gray's blocking commit protocols all converge here.

## Questions worth arguing about

These are seminar questions. Several have no settled answer.

1. **Where does your system assume a stable leader?** Every Paxos or Raft deployment quietly depends on one. During leader churn or a partition, does yours stay safe, never returning a wrong or divergent answer, or does it merely stay available? Be sure which one you actually get, because the two are different guarantees.
2. **Do you even need consensus?** A replicated log through a majority is expensive: a round trip per command and a hard dependency on a quorum being up. Where have you reached for full consensus when a weaker primitive, a lease, last-writer-wins, a conflict-free replicated type, would have done, and where have you done the reverse and paid for it in lost updates?
3. **Single-decree or the whole system?** When you say your service "uses Raft," is your mental model the one-value safety core or the log-and-leader machine on top? Which part do you rely on, and which part are you trusting your library to have gotten right, given how much "Paxos Made Live" says can go wrong there?
4. **What breaks if two nodes both think they are leader?** If the honest answer is "we could lose or diverge data," then your safety is not where the theorem puts it. In correct Paxos, dueling leaders cost only progress. If they cost correctness, something in your implementation has moved safety out of the quorum.
5. **Where are your ballot numbers?** The monotonic epoch, term, or fencing token that makes a stale leader's late writes harmless is the ballot-number idea in production. Find yours. If you cannot, a zombie leader can still do damage.
6. **Is legibility an engineering property for you?** Raft beat Paxos on understandability, not power, and won the field for it. Where have you chosen a less clever, more legible mechanism on purpose, and where has cleverness you were proud of cost you in bugs no one could review?

## Further reading

Start with the readable paper, then the origin, then the hard-won production experience.

- **Lamport, "Paxos Made Simple" (2001).** The protocol in plain English. Read sections 2 and 3; the safety derivation is the whole thing.
- **Lamport, "The Part-Time Parliament" (1998).** The origin, the formal treatment, and the allegory. Read Marzullo's notes for the relation to Viewstamped Replication and commit protocols.
- **Chandra, Griesemer, and Redstone, "Paxos Made Live" (2007).** Google's account of turning the algorithm into Chubby. The definitive evidence of the gap between the paper and a correct system.
- **Ongaro and Ousterhout, "In Search of an Understandable Consensus Algorithm" (Raft, 2014).** The deliberately teachable alternative that most new systems now use. Read it against "Paxos Made Simple" to see what understandability costs and buys.
- **Oki and Liskov, "Viewstamped Replication" (1988).** The convergent, equivalent protocol from the systems side, and the subject of the fifth seminar.
- **Fischer, Lynch, and Paterson, "Impossibility of Distributed Consensus with One Faulty Process" (1985).** The impossibility that Paxos respects rather than defeats. The reason liveness is conditional.
- **Lampson, "How to Build a Highly Available System Using Consensus" (1996).** The operational reading, by the person who understood Paxos first and championed it into print.
- **Schneider, "Implementing Fault-Tolerant Services Using the State Machine Approach" (1990).** The tutorial on the state-machine method that the log construction turns fault-tolerant.

## Where the series goes next

Every protocol in this seminar tolerates crashes and trusts that no one lies. A replica's report of what it accepted is taken at face value, because a crashed process simply goes silent; it does not send one story to one peer and a contradictory story to another. Drop that assumption and the problem hardens. If a participant can be actively malicious, agreement needs more replicas, more rounds, and cryptographic care, and majority intersection alone no longer suffices. That is Byzantine fault tolerance, and Castro and Liskov's Practical Byzantine Fault Tolerance is where the series turns next, generalizing the crash-tolerant consensus of this seminar to a world where some of the processes are adversaries.

The test this series puts to every chapter: if the author were in the room, would he recognize his idea and learn from the modern reading? Lamport would recognize all of it, and he has watched most of it happen, from Chubby to Raft. What he might appreciate is the vindication buried in the story. The paper was rejected as a frivolous joke and sat for the better part of a decade; it is now the theoretical foundation of the systems that run the internet's control planes. The field's humorlessness, which annoyed him, cost it eight years of catching up. The idea was right the whole time. It was only ever the costume that was wrong.
