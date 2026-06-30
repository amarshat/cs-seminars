# Reading Joe Armstrong

## *Making Reliable Distributed Systems in the Presence of Software Errors*

> Joe Armstrong, PhD thesis, The Royal Institute of Technology (KTH), Stockholm, December 2003.

Most papers on reliability start from a hope: if we are careful enough, the software will be correct. Armstrong starts from the opposite assumption. The software is large, it has been written by many people over many years, and right now, in production, some of it is wrong. You do not know which part. You cannot test your way to certainty. And the system has to keep working anyway.

That single move, treating bugs in running code as a permanent condition rather than a temporary embarrassment, is what makes this thesis worth reading twenty years later. Armstrong was not chasing elegance. He was at Ericsson, and the thing on the other end of the wire was a telephone exchange that was not allowed to stop. The question was brutally concrete: how do you build software that stays up while parts of it are broken?

His answer became Erlang and OTP, and the shape of that answer (isolated processes, no shared memory, let it crash, supervise and restart) has resurfaced in Kubernetes, in actor runtimes, in serverless platforms, and in every microservice that gets killed and rescheduled instead of debugged in place. Most engineers who rely on that shape have never traced it back to where it was written down clearly. This seminar does.

## Why this thesis, first

Armstrong goes first in CS-Seminars because his question is the one most of the other classics are also circling. Lamport asks how unreliable machines agree on an order of events. Liskov and Castro ask how they stay correct when some are malicious. Gray asks what "correct" even means once you have concurrency and failure in the same system. Armstrong asks the most direct version: given that failure is normal, how do you architect for survival rather than for the absence of bugs? Read him first and the rest of the series reads as variations on his theme.

## The four questions

This seminar, like every seminar here, works through four questions:

1. **What problem was Armstrong actually solving?** Not "how do I make a nice language," but "how do I keep a telecom switch alive for forty years through hardware faults, software bugs, and in-place upgrades."
2. **Why was the answer surprising?** Because it threw out the reflex every programmer is taught: handle the error where it happens. Armstrong's system handles errors somewhere else, on purpose.
3. **What survived?** The architecture did. Share-nothing isolation and supervised restart are now defaults in systems that have never heard of Erlang. Some of the specifics (the nine-nines folklore, the assumption of one language end to end) need an asterisk.
4. **How should you read it today?** As an architecture document that happens to be written in a programming language, not as a language tutorial.

## Chapters

1. [The problem](01-the-problem.md) — A switch that cannot stop, and why testing cannot save you.
2. [Concurrency-oriented programming](02-concurrency-oriented-programming.md) — Processes as the unit of the world. Share nothing. Copy messages.
3. [Let it crash](03-let-it-crash.md) — Why defensive programming makes things worse, and what to do instead.
4. [Supervision trees](04-supervision-trees.md) — Putting recovery somewhere it can actually work: above the thing that failed.
5. [Links and monitors](05-links-and-monitors.md) — Turning a crash into a message another process can act on.
6. [Armstrong's rules](06-armstrongs-rules.md) — The six requirements he distills, read as a checklist for any platform.
7. [Modern echoes](07-modern-echoes.md) — Kubernetes, systemd, Akka, Orleans, Temporal, and what they got right and wrong.
8. [Discussion and further reading](08-discussion-and-reading.md) — Questions to argue about, and where to go next.

## A note on the source

Quotations and figures here come from the 2003 thesis (the PDF Ericsson still hosts). Where the famous numbers have gotten exaggerated in retellings (the "nine nines" claim in particular), this seminar uses Armstrong's own, more careful framing rather than the folklore version. He was more honest about the evidence than the internet has been on his behalf.
