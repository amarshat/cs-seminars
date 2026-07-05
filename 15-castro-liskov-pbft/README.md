# Reading Miguel Castro and Barbara Liskov

## *Practical Byzantine Fault Tolerance*

> Miguel Castro and Barbara Liskov, "Practical Byzantine Fault Tolerance," Proceedings of the Third Symposium on Operating Systems Design and Implementation (OSDI), New Orleans, February 1999. The fuller treatment is Castro's MIT PhD thesis, "Practical Byzantine Fault Tolerance" (2001).

Every consensus protocol in this book so far has made the same quiet assumption, and it is time to break it. Viewstamped Replication, Paxos, and their production descendants Chubby and Spanner all assume that a broken node fails by stopping. It goes silent. It never sends a wrong answer, never sends different answers to different peers, never actively works against the protocol. That assumption is called the crash-fault model, and it is comfortable because a silent node is easy to reason about: you wait, you time out, you route around it.

Practical Byzantine Fault Tolerance drops the assumption. In the Byzantine model, a faulty node may do anything at all. It may lie. It may send one story to one replica and a contradictory story to another. It may collude with the other faulty nodes to attack the honest ones. This is the failure model of a compromised server, a corrupted disk that returns plausible garbage, a buggy replica computing the wrong result, or an attacker who owns part of your system. The demand is severe: the honest replicas must still agree, and the service must still behave as if it ran on one correct machine, even while some of its own members are trying to break it.

Tolerating lies is not free, and the price is the shape of the protocol. Where crash tolerance needs 2f+1 replicas to survive f failures, Byzantine tolerance needs 3f+1, a third more hardware, because a quorum must now overlap in at least one honest node rather than merely one live node. Where Paxos needs two phases, PBFT needs three, and the extra round exists specifically to catch a primary that lies. And cryptography becomes load-bearing: replicas sign or authenticate their messages so a faulty node cannot forge an honest one's words. The remarkable part, and the entire point of the title, is that Castro and Liskov made all of this fast enough to use. Byzantine agreement had existed since 1982 and had always been too slow for real systems. PBFT ran a Byzantine-fault-tolerant network file system at roughly three percent overhead. Tolerating lies turned out to be nearly affordable.

## Why this seminar, fifteenth and last

This is the capstone, and it closes two threads the book has been pulling for fourteen seminars. It is the end of the replication thread: Lamport's ordering seeded state-machine replication, Viewstamped Replication and Paxos made it survive crashes, Spanner put it into global production, and PBFT now makes it survive treachery. It is also the sharpest point of the trust thread: Saltzer and Schroeder said mediate completely and grant least privilege, Clark watched the internet's trust in its own endpoints erode, and PBFT is what you build when you extend that erosion to its logical end and stop trusting the participants entirely. There is a fitting symmetry in the authorship, too. Barbara Liskov opened the replication thread with Viewstamped Replication and closes it here, and Leslie Lamport, who named the Byzantine Generals problem in 1982 and gave us both logical clocks and Paxos, is the origin this seminar builds on.

## The four questions

1. **What problem were Castro and Liskov solving?** How replicas reach agreement and keep a service correct when up to f of them are not merely down but Byzantine: buggy, corrupted, compromised, or malicious, possibly colluding and lying differently to different peers. The honest replicas must still agree.
2. **Why was the answer surprising?** Byzantine agreement had been known since 1982 and was considered too slow for real use, because earlier work assumed a synchronous network or cost orders of magnitude in performance. PBFT works in an asynchronous network and added only about three percent overhead to a real file system. The surprise was that tolerating lies could be nearly free.
3. **What survived?** The permissioned Byzantine-fault-tolerant lineage: Tendermint, HotStuff, and Diem, and the BFT-finality consensus inside many modern distributed ledgers, all descend from PBFT's quorum math and its leader-plus-view-change structure. What it is not is Nakamoto proof-of-work, which is a separate lineage for open membership.
4. **How should a working engineer read it today?** As the moment the failure model becomes the first architectural decision. Crash tolerance and Byzantine tolerance are different worlds, with different replica counts, quorum sizes, phase counts, and cryptographic needs, and which world you are in determines everything else.

## Chapters

1. [The assumption every protocol made](01-crash-versus-byzantine.md). Crash faults fail silently; Byzantine faults lie. Why that difference changes everything.
2. [The Byzantine Generals, and why it was impractical](02-byzantine-generals.md). The problem was posed in 1982; PBFT did not invent it, it made it fast.
3. [Why 3f+1](03-why-3f-plus-1.md). The single most important point: quorums must intersect in an honest node, not just a live one.
4. [The three-phase protocol](04-the-three-phase-protocol.md). Pre-prepare, prepare, commit, and why the extra round exists to catch a lying primary.
5. [When the primary lies: view changes](05-view-changes.md). Suspect the leader, elect a new one, and lose nothing that already committed.
6. [Practical: cryptography and the 3 percent](06-practical-cryptography.md). Message authentication, not signatures everywhere, and the benchmark that made Byzantine tolerance credible.
7. [The blockchain lineage](07-the-blockchain-lineage.md). Permissioned BFT and its descendants, kept distinct from Nakamoto proof-of-work.
8. [The finale: trust, and the end of the book](08-the-finale.md). The failure model as the first decision, and the threads this book has been weaving.

## A note on the sources

Quotations come from the OSDI 1999 paper. This seminar keeps several things straight. Byzantine tolerance needs 3f+1 replicas and 2f+1 quorums, not the 2f+1 replicas of crash-tolerant Viewstamped Replication, and the reason is that a quorum overlap must contain an honest node, because a faulty node in the overlap can lie to both sides. PBFT did not invent Byzantine agreement, which dates to Lamport, Shostak, and Pease in 1982; its contribution is making it practical and asynchronous. It does not beat the FLP impossibility: safety holds always, liveness only under a weak synchrony assumption, exactly as in Paxos. Its cryptography is load-bearing and it assumes known, fixed membership, so it is not "trustless" in the blockchain sense. And it is the ancestor of permissioned BFT, Tendermint and HotStuff and Diem, which is a different lineage from Bitcoin's proof-of-work.
