# 7. Discussion and further reading

## The argument in one breath

Hoare started from a hardware prediction: the machine of the future would be many self-contained processors, each with its own store, and shared memory across them would be the expensive, error-prone illusion rather than the free primitive. From that he derived a single answer to concurrency. Structure a program as sequential processes that do not share memory and communicate only by input and output. Make that communication a synchronous handshake, so a send and a matching receive happen as one event with no buffer in between. Name the other process directly. Build all the choosing on Dijkstra's guarded commands, extended so a process can offer several communications and take whichever is ready, with the choice among ready ones left arbitrary. That is the entire 1978 proposal, and it is deliberately austere: static, unbuffered, and, by Hoare's own admission, without any method for proving programs correct.

The proof method came later, and it is the thing most people now mean by CSP. The traces, failures, and refinement of the 1984 and 1985 work turned the notation into a theory you could check machines against. Read the paper and the book as two achievements, not one, and the history stays honest.

## Questions worth arguing about

These are seminar questions. Several have no settled answer.

1. **Synchronous or asynchronous, and who decides?** Hoare made communication synchronous and rejected buffering; Hewitt's actors are asynchronous and buffered. Go lets you pick per channel. Is the buffering decision better made once by the language designer, or every time by the programmer at the point of use? What goes wrong under each choice, and does "let the programmer choose" just relocate the mistake?

2. **Backpressure for free, or backpressure by accident?** A synchronous rendezvous gives backpressure automatically: a slow consumer slows its producer. An unbounded actor mailbox does not, and can grow until it exhausts memory. Is CSP's synchrony the right default for systems under load, or does mandatory blocking create its own failure, where one slow consumer stalls a whole pipeline?

3. **Name the process, the pid, or the channel?** Each choice makes different things easy. Direct process naming is simple but static and hostile to libraries, as Hoare admitted. First-class channels enable dynamic topologies but add a value to manage. Pids sit in between. Which does your current system use, and what did that choice cost you?

4. **Should a language promise fairness?** Hoare said no: correctness must not depend on the scheduler being fair, and a program that only terminates under a fair scheduler is incorrect. The actor tradition leaned the other way. Which position matches how you actually reason about your programs, and which matches how they actually run?

5. **What did the disclaimer buy?** The 1978 paper openly says it offers no proof method and should not be used as a language. It became one of the most influential papers in the field anyway. Did the honesty about its limits help or hurt its influence? What would you cite it for, and what would you not?

6. **Was shared memory really the enemy?** Hoare and Hewitt both banned it. Go allows it and merely advises against it, and Go is wildly popular. Were the founders too austere, or is Go's permissiveness a debt that comes due in data races?

## Further reading

Start with the paper, then the book, and keep them separate in your head.

- **C.A.R. Hoare, "Communicating Sequential Processes," CACM 21(8), 1978.** The source. Short, sharp, and unusually candid about its own limits. Read sections 1 and 7 for the argument and the self-criticism; the middle is worked examples.

- **C.A.R. Hoare, *Communicating Sequential Processes* (Prentice Hall, 1985).** The book, and a different thing from the paper: the process algebra, traces, failures, and refinement. Available free online. Read it for the theory the paper deliberately lacked.

- **Brookes, Hoare, and Roscoe, "A Theory of Communicating Sequential Processes," JACM (1984).** Where the failures model was first set out. The bridge between the paper and the book.

- **A.W. Roscoe, *The Theory and Practice of Concurrency* (Prentice Hall, 1998).** The modern treatment of the CSP models and refinement checking, from the person who built much of the theory and the FDR tool.

- **Robin Milner, *A Calculus of Communicating Systems* (1980).** The sibling process algebra, developed at Edinburgh in mutual influence with CSP. Read it to see which choices were CSP's and which were shared across the field, and it sets up the later π-calculus that gave channels their mobility.

- **Rob Pike, "Go Concurrency Patterns" (2012).** The clearest short account of how CSP became Go, by the person who carried it through Newsqueak, Alef, and Limbo. He is explicit about what Go took and what it changed.

- **Gilles Kahn, "The Semantics of a Simple Language for Parallel Programming" (IFIP 1974).** The road not taken, and Hoare's own point of contrast in section 7.7: deterministic, automatically buffered, functional process networks. Read it against CSP to feel the applicative-versus-imperative split.

## Where the series goes next

CSP and the actor model are the two great answers to how independent things coordinate by message. Both, notably, dodge a harder question, and that question is the next seminar.

- Hoare's processes run at "arbitrary" relative speeds with no global clock, and the 1985 traces model describes a process as a sequence, an ordering, of the events it engages in. But CSP assumes communication either happens or does not; it does not ask how physically separated machines, some of which may fail, come to agree on an ordering of events in the first place. That is **Leslie Lamport's** question: logical clocks, the happens-before relation, and eventually consensus. The partial order that ran quietly through the Hewitt seminar becomes the explicit subject there.
- And the contrast that anchored this seminar points back to **Carl Hewitt**. Read the two together and you have the whole design space: synchronous versus asynchronous, buffered versus not, channel versus process versus pid. Every concurrency runtime you will ever use is a set of positions on those axes, and these two papers staked out the corners.

Read this way, Hoare is not just the origin of `select` and channels. He is one half of a decades-long argument about what communication is, and the argument is still live in every codebase that has to choose.
