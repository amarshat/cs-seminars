# Reading Carl Hewitt

## *A Universal Modular ACTOR Formalism for Artificial Intelligence*

> Carl Hewitt, Peter Bishop, and Richard Steiger. IJCAI-73, Proceedings of the Third International Joint Conference on Artificial Intelligence, Stanford, August 1973, pages 235 to 245.

Most people who say "actor model" today are thinking about concurrency: a runtime full of little stateful objects, each with a mailbox, each handling one message at a time. Erlang processes, Akka actors, Orleans grains. That picture is real, and it works, but it is not quite the thing Hewitt, Bishop, and Steiger wrote down in 1973.

They were not trying to build a concurrency runtime. They were at the MIT AI Lab, deep in the PLANNER project, trying to answer a much stranger question: how do you embed knowledge in procedures so that a program can reason about the world, and about itself? Their move was to throw out the entire zoo of programming constructs (functions, data structures, processes, semaphores, monitors, ports) and replace all of it with a single kind of object that does a single thing. An actor. It sends messages to other actors. That is the whole model.

The surprise is what falls out of that one decision. If the only event in the universe is one actor sending another a message, then control flow and data flow become the same thing, there is no place for a `goto` to jump to, there is no global clock to synchronize against, and "when did this happen" turns into a partial order of events rather than a timeline. Hewitt was writing about artificial intelligence, but he had stumbled into the foundations of concurrent and distributed computation, and he knew it.

## Why this seminar, second

Armstrong went first in this series because his question, how do you keep a system correct while parts of it fail, is the one most of the classics circle. Hewitt goes second because he supplies the shape Armstrong's answer took, from a completely different direction and eleven years earlier.

Here is the honest version of that link, because it is easy to get wrong. Erlang is not descended from the actor model. Armstrong's thesis does not cite Hewitt, and Erlang's designers have said plainly that they had never heard of the actor model while building it. They came from Prolog, telephony, and a concrete reliability problem. Hewitt came from Lisp, logic, and artificial intelligence. They arrived at share-nothing entities that communicate only by messages independently. That is convergence, not inheritance, and convergence is more interesting than a family tree: two people solving different problems reached for the same structure, which suggests the structure is doing real work.

## The four questions

1. **What problem was Hewitt actually solving?** Not concurrency for its own sake. He wanted a single, uniform foundation for representing knowledge and computation, general enough that a function, a database, and a process were all the same kind of thing, so a program could reason about any of them the same way.
2. **Why was the answer surprising?** Because it deleted the constructs everyone treated as primitive. No `goto`, no interrupt, no semaphore. Hewitt claimed a single primitive, sending a message, was strictly more powerful, and that the discarded constructs were special cases of it.
3. **What survived?** The core did: everything is an entity that communicates only by message, addresses are capabilities, and there is no global state. What got replaced is subtle. Hewitt's 1973 actor is side-effect-free by default, its state confined to explicit cells, and it can share a continuation with others. The actor that survived into Erlang and Akka is stateful and serialized. The word stayed; the semantics drifted.
4. **How should a working engineer read it today?** As the source of a mental model you already use, and as a warning about how much a popular idea can mutate. Read it to see the model in its purest, strangest form, before the runtimes sanded off the parts that were hard to build.

## Chapters

1. [Knowledge, not reliability](01-the-problem.md). Why an AI lab invented the actor model, and what "procedural embedding of knowledge" was really asking for.
2. [One kind of object](02-one-kind-of-object.md). Everything is an actor. Functions, data, and processes as special cases of a single thing.
3. [The message is the only move](03-the-only-move.md). Sending as the sole primitive, continuations as actors, and why there is no `goto` to write.
4. [No clock, only order](04-no-clock-only-order.md). Events, histories, and the arrow of time. How Hewitt described causality without a global now, and why distributed systems needed exactly this.
5. [Behavior, not state](05-behavior-not-state.md). The side-effect-free actor, shared continuations, intentions as contracts. Where the 1973 model diverges hardest from the actors you use.
6. [What survived, what got replaced](06-what-survived.md). Agha's recasting, Erlang's convergence, Akka and Orleans, and where each analogy breaks.
7. [Discussion and further reading](07-discussion-and-reading.md). Questions to argue about, and where to go next.

## A note on the source

Quotations come from the 1973 IJCAI proceedings text (pages 235 to 245), with one exception flagged where it appears: the sharpest statement of message-passing as a universal control primitive is quoted from Hewitt's follow-up, "Viewing Control Structures as Patterns of Passing Messages" (1977). One page of the scanned proceedings, the page carrying the formal definitions of event and history, does not survive automatic text extraction cleanly, so those definitions were transcribed by reading the page image directly. Where the actor model's folklore has drifted from the paper (the famous "create, send, become" trio in particular, which comes from Gul Agha's 1986 formulation, not this paper), this seminar uses what the 1973 text actually says and flags the later additions as later.
