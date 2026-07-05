# 6. The strangest famous paper

## The problem: a right idea in the wrong costume

Now that the algorithm makes sense, its history reads as a cautionary tale, because the paper that founded modern consensus was nearly lost, and not because it was wrong. Lamport wrote it around 1990 and submitted it to a journal, and it was rejected. The reviewers did not find a flaw; they found the presentation absurd. He had written the algorithm as archaeology.

The paper describes a fictional Aegean island, Paxos, whose parliament kept passing consistent laws even though its legislators were part-timers who wandered in and out of the chamber and whose messengers were forgetful. An archaeologist narrates the reconstruction of the island's long-lost parliamentary protocol. It is an elaborate, sustained joke, complete with Greek-lettered legislator names that parody real researchers, Fischer and Lynch among them, the very authors of the impossibility result the algorithm has to live with. Reviewers thought the whole thing was unserious and the algorithm unimportant, and Lamport, by his own account, "was quite annoyed at how humorless everyone working in the field seemed to be," and did nothing with it. It sat unpublished for years.

## The allegory, decoded

The allegory is not decoration; every element maps to a piece of the distributed-systems problem, which is what makes it both clever and, for most readers, maddening.

| In the allegory | In a distributed system |
|---|---|
| Legislator | Process |
| Leaving the chamber | Crash or failure |
| Indelible ledger | Stable storage |
| Messenger | The network |
| Hourglass timer | Timeout, real time |
| A decree | A command, a value |
| Single-decree Synod | One-value consensus |
| The Parliament | The replicated log |

Read that way, the paper is exactly the protocol of the previous chapters. The Synod of priests choosing one decree is single-decree Paxos. The Parliament passing an ordered sequence of decrees into every legislator's ledger is the replicated log. The requirement that no two ledgers ever record contradictory decrees is agreement, and the progress condition, that decrees get passed only when a majority stay in the chamber long enough, is the conditional liveness of the fourth chapter, stated as a fact about legislators' attendance. Everything is there. It is just wearing a toga.

## Rescued, twice

The algorithm was saved by people who needed it. Engineers at Digital Equipment's research lab, building real distributed storage systems, wanted a fault-tolerant agreement protocol, were handed the paper, and read it without trouble. And one reader had understood its importance from the start: Butler Lampson, whose own work is a seminar earlier in this series, championed it, lectured on it, wrote it into a paper of his own, and drew others in. That pressure finally moved Lamport to publish. In a last turn of the joke, rather than rewrite the paper he proposed that it appear in 1998 as a "recently discovered" manuscript, annotated by Keith Marzullo, whose editorial note deadpans that the submission "was recently discovered behind a filing cabinet in the TOCS editorial office." Lamport later noted it had set a personal record for the delay between writing and publishing a paper.

Publication did not make it readable. The algorithm kept its reputation as impenetrable, and so in 2001 Lamport wrote a second, plain-English paper, "Paxos Made Simple," which opens by admitting the original "has been regarded as difficult to understand, perhaps because the original presentation was Greek to many readers." These are two different papers doing two different jobs: the 1998 allegory is the origin and the formal treatment, and the 2001 note is the teachable version. This seminar takes the protocol from the second and the story from the first, and it is worth not confusing them.

## What the paper itself says about its neighbors

Marzullo's annotations do one more useful thing: they place Paxos among its relatives, and the placement closes two loops in this series. The note observes that Oki and Liskov's view-management protocol, Viewstamped Replication from the fifth seminar, "seems to be equivalent" to the Paxon protocol. That is the honest relationship: VR reached crash-fault-tolerant replicated state machines from the systems side in 1988, Paxos reached the same place from the theory side around 1990, independently, and neither is derived from the other. They are two roads to one destination, and their author and editor say so. The paper also notes that the Synod is "similar to standard three-phase commit protocols," which closes the loop with Gray's seminar: two-phase commit blocks when the coordinator fails, three-phase commit tries to be non-blocking, and consensus is the general, non-blocking answer to the agreement problem those protocols were circling. A commit protocol chooses between commit and abort; the Synod chooses an arbitrary value, and that generality is the difference.

One boundary is worth marking, because it defines the next step. Throughout, the messengers may lose, delay, or duplicate messages, but they do not garble them, and the legislators, though absent-minded, are not liars. Paxos assumes crashes, not treachery. The case where a component actively misbehaves, sending different stories to different peers, is Byzantine fault tolerance, and it is the Castro and Liskov seminar still to come.

> **Principle:** A correct idea and an accepted idea are not the same thing. Paxos was right for the better part of a decade before the field would read it, and it took a plain rewrite, a rival built for clarity, and the advocacy of people who needed it to make the most important consensus algorithm legible. Package your ideas for the reader you have, not the one you wish you had.
