# 7. Discussion and further reading

## The argument in one breath

Hewitt started from an AI problem, not a concurrency one: how do you embed knowledge in procedures so a program can reason about anything in its world, and about itself, in one uniform way? His answer was to delete the zoo of programming constructs and keep a single kind of object, the actor, with a single ability, sending messages. Everything followed from taking that seriously. Define objects by behavior, not representation, so a function and a database are the same kind of thing. Rebuild every control structure out of messages, so returning is just sending to a continuation you were handed. Give up the global clock, because a swarm of independent senders has no shared now, and let causality be a partial order instead. Define sameness by what an observer can see, and correctness by a contract on each actor. And, in the version he actually wrote in 1973, keep the actor side-effect-free, so many activities can share it and it is never busy.

That last piece is the one history rewrote. The actor that conquered industry is stateful and handles one message at a time, and it got that way through Agha's reformulation and Erlang's independent invention, not through this paper. The abstract commitments survived. The concrete semantics of a single actor were replaced. Reading the 1973 paper is how you tell the two apart.

## Questions worth arguing about

These are seminar questions, not quiz questions. Several have no settled answer.

1. **Is a stateless actor still an actor?** Hewitt's 1973 actor is side-effect-free and shareable. Agha's is stateful and serialized. If you handed both to an engineer today, only the second would feel like "an actor." Did the model improve, or did we narrow it until we forgot half of it existed?

2. **Mailbox inside or outside?** Hewitt argued buffering and ordering belong inside an actor; Erlang put an external mailbox in front of each process and added selective receive. Which is right, and for what? What does selective receive make easy that a strict "handle every message as it arrives" model makes hard, and what does it cost in reasoning?

3. **Actors or channels?** Hewitt's actors are named and hold their own inboxes; Hoare's CSP, the next seminar, coordinates anonymous processes through named channels with synchronous rendezvous. Same era, opposite choices about where the addressing and the buffering live. Which model fits the systems you build, and why did Go pick channels while Erlang picked mailboxes?

4. **Convergence as evidence.** Hewitt from AI, Armstrong from telecom, Lamport from distributed clocks, all reached for message-passing entities and causal partial orders without borrowing from each other. What does that independent convergence tell you? When several people solving unrelated problems build the same structure, is that a law of the territory, or just a fashion of the era?

5. **Where did the intentions go?** Every actor in 1973 had an intention, a contract checked on each message, and Hewitt built a proof principle on it. Modern actor runtimes mostly dropped this. Was it impractical, or did we just not build the tooling, and does property-based testing bring it back in a different form?

6. **No global clock, then what?** Hewitt was content to define causality as a partial order and stop. Real systems have to make separated machines agree anyway. Where, in your stack, do you pay to manufacture the global order that Hewitt correctly said does not exist for free?

## Further reading

Start with the paper. It is short, strange, and studded with Lewis Carroll epigraphs, and it reads nothing like a modern systems paper, which is part of the point.

- **Hewitt, Bishop, and Steiger, "A Universal Modular ACTOR Formalism for Artificial Intelligence" (IJCAI-73).** The source. Read it for the ambition and for how much of the later model is already implicit here, and how much is not.

- **Gul Agha, *Actors: A Model of Concurrent Computation in Distributed Systems* (MIT Press, 1986).** The reformulation that produced the actor most people mean, built on the create, send, become primitives. If you only know actors from a framework, this is the book that framework is implementing.

- **Irene Greif, *Semantics of Communicating Parallel Processes* (MIT PhD, 1975), and Will Clinger, *Foundations of Actor Semantics* (MIT PhD, 1981).** The formal backbone. Greif turned the event-and-history sketch into a semantics; Clinger nailed down unbounded nondeterminism.

- **Hewitt and Baker, "Laws for Communicating Parallel Processes" (IFIP 1977).** Where the guarantees, including fair delivery, get stated as laws.

- **De Koster, Van Cutsem, and De Meuter, "43 Years of Actors: A Taxonomy of Actor Models and Their Key Properties" (AGERE 2016).** The best single map of how the model splintered into processes, active objects, and event-loop actors, and which language sits where. Read it after the paper to see the family tree whole.

- **Joe Armstrong, *Making Reliable Distributed Systems in the Presence of Software Errors* (2003).** The convergent cousin, and the previous seminar in this series. Read the two together to feel how far apart their starting points were and how close their conclusions landed.

## Where the series goes next

Hewitt gave us message-passing entities and a causal order with no global clock. He did not tell us how to coordinate them under failure, or whether messages should even be asynchronous. Those gaps are the next readings.

- **Tony Hoare's Communicating Sequential Processes** is the road not taken: synchronous rendezvous over named channels instead of asynchronous messages to named actors. Same problem, a rigorously different answer, and the direct ancestor of Go's channels. It is the next seminar.
- **Leslie Lamport** takes the partial order of chapter 4 and makes it operational, with logical clocks a running system can compute, and then confronts the harder question Hewitt sidestepped: how do separated machines agree on one order when some of them fail.
- The reliability machinery that Erlang wrapped around its actors, supervision, links, restart, is **Armstrong's** contribution, not Hewitt's, and reading the two seminars side by side shows exactly where the model of computation ends and the architecture of survival begins.

Read this way, Hewitt is not the first chapter of a concurrency textbook. He is the moment someone tried to reduce all of computation to one act, sending a message, and discovered, almost as a side effect, the shape that distributed systems would need for the next fifty years.
