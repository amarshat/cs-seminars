# Reading Tony Hoare

## *Communicating Sequential Processes*

> C.A.R. Hoare, Communications of the ACM, Volume 21, Number 8, August 1978, pages 666 to 677.

The previous seminar read Carl Hewitt, who answered the concurrency question one way: independent actors that fire messages at named recipients and never wait for a reply. This seminar reads the other great answer, published five years later by Tony Hoare, and the two are worth reading back to back because they disagree at almost every joint.

Hoare's processes do not fire and forget. When one process wants to send a value to another, both must arrive at the meeting point together: the sender waits, the receiver waits, and the value passes in a single synchronized step. There is no mailbox, no buffer, no queue. Communication is a handshake. And where an actor addresses a recipient by identity, a Hoare process names the other process directly in the source text, `X!v` to send to `X`, `Y?x` to receive from `Y`, with the set of processes fixed before the program runs.

That single decision, communication as a synchronized handshake between named processes, is the seed of a whole tradition. It grew into a process algebra in the 1980s, into the occam language and the transputer chip built to run it, and into the `select` statement and channels of Go. This seminar traces that line, and keeps careful about what belongs to the 1978 paper and what came later, because the CSP most engineers half-remember is a mixture of the paper, a 1985 book, and a Google language, and the three are not the same thing.

## Why this seminar, third

Hewitt and Hoare are the two poles of concurrency, and putting them side by side is the fastest way to understand either. Actors are asynchronous, buffered, and addressed to a recipient. CSP is synchronous, unbuffered, and addressed to a named process. Neither is more correct. They are different bets about what the hard part of concurrency is, and modern systems have inherited both, often in the same codebase. Read Hewitt for the shape of a message-driven system that scales by not waiting. Read Hoare for the shape of a system that stays analyzable because every communication is a point where two processes agree.

## The four questions

1. **What problem was Hoare actually solving?** How the processors of a multiprocessor machine, each with its own private store, should communicate and synchronize, given that shared memory was expensive and error-prone. He wanted input and output to be language primitives, not afterthoughts.
2. **Why was the answer surprising?** Because he made communication synchronous and unbuffered on purpose, rejecting the automatic buffering others were proposing, and because he built it all on Dijkstra's guarded commands, turning a construct for local nondeterminism into the mechanism for choosing between communications.
3. **What survived?** The handshake, the guarded choice, and the idea that you structure a concurrent program as sequential processes that only communicate. `select` in Go is Dijkstra's guarded command by way of Hoare. What changed is that the descendants replaced direct process naming with first-class channels, and most of them added the buffering Hoare refused.
4. **How should a working engineer read it today?** As the origin of the channel-and-select style, and as a lesson in the cost of the choices. The 1978 paper is honest about its own limits in a way more papers should copy: it says plainly that it offers no proof method and should not be used as a language.

## Chapters

1. [Input, output, and a machine of processors](01-the-problem.md). The problem Hoare set himself, and why shared memory was the wrong tool for it.
2. [Communication is a handshake](02-the-handshake.md). Synchronous rendezvous, no buffering, and the deliberate contrast with the actor's asynchronous send.
3. [Name the process, not the channel](03-name-the-process.md). Direct process naming, the static world it implies, and the asymmetry Hoare himself flagged.
4. [Choice and nondeterminism](04-guarded-choice.md). Dijkstra's guarded commands, input guards, deadlock, and why fairness is left to the programmer.
5. [The algebra came later](05-the-algebra-came-later.md). What the 1978 paper does not contain: traces, failures, refinement, and the 1985 book that added them.
6. [occam, the transputer, and Go](06-occam-transputer-go.md). The faithful descendant, the chip built for it, and the CSP-inspired language most engineers actually use.
7. [Discussion and further reading](07-discussion-and-reading.md). Questions to argue about, and where to go next.

## A note on the source

Quotations come from the 1978 CACM paper (pages 666 to 677). The two-column scan defeats naive text extraction, so quotes were checked against a clean reading-order pass and, where symbols mattered, against the page images. This seminar is deliberate about the difference between the 1978 paper and Hoare's 1985 book *Communicating Sequential Processes*: the process algebra, the traces and failures models, and refinement are the book's contribution, developed with Brookes and Roscoe, and this seminar does not put them in the 1978 paper's mouth.
