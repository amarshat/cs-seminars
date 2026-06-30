# 6. Armstrong's rules

## Six requirements, read as a rubric

Early in the thesis, while he is still laying out the problem rather than the solution, Armstrong writes down a specification. To support this style of programming and meet the demands of a telecom system, he says, you arrive at six requirements on the underlying operating system and programming language. He is careful about the framing: these are requirements on the system as a whole. He does not care whether a given one is satisfied by the language, by a library, or by the operating system underneath. He cares that the system satisfies it somehow.

That framing is what makes the list worth more than its Erlang origins. Twenty years on, the most useful thing to do with these six is to treat them as a grading rubric. Any platform that claims to be fault-tolerant, a Kubernetes cluster, a serverless runtime, an actor framework, a service mesh, can be held up against this list. Where it scores well, it earned its claim. Where it scores badly, you have found the failure mode that will surprise its operators. Here are the six, in Armstrong's order, with what each one is really demanding and where modern platforms pass or quietly fail.

| # | Requirement | What it demands | Where it lives in this seminar |
|---|-------------|-----------------|-------------------------------|
| R1 | Concurrency | Create and destroy processes so cheaply there is no penalty for having huge numbers of them | [Chapter 2](02-concurrency-oriented-programming.md) |
| R2 | Error encapsulation | A fault in one process cannot damage another | [Chapter 2](02-concurrency-oriented-programming.md) |
| R3 | Fault detection | Detect failures both locally and in a remote process | [Chapter 5](05-links-and-monitors.md) |
| R4 | Fault identification | Determine why a failure happened, well enough to fix it later | [Chapter 5](05-links-and-monitors.md) |
| R5 | Code upgrade | Change code in a running system without stopping it | this chapter |
| R6 | Stable storage | Keep data that survives a crash | [Chapter 4](04-supervision-trees.md) |

Notice the shape. R1 and R2 are the isolation base: cheap processes and hard boundaries. R3 and R4 are about perceiving failure: not just that something broke, but what and why. R5 and R6 are about continuity over time: changing the system and keeping its memory across crashes. The architecture of the previous chapters falls out of these six almost line by line.

## R1 and R2: the base nobody can skip

**Concurrency** demands that a process be cheap enough to spend freely. This is not a performance nicety. Chapter 2 argued that isolation is only usable if it is cheap, because expensive isolation gets rationed and rationed isolation gets undermined by sharing. The modern platforms that pass R1 cleanly are the ones with lightweight units: goroutines, Java's virtual threads, async tasks. But passing R1 says nothing about R2, and that is the whole reason these are two requirements and not one. A goroutine is cheap enough to spawn by the million (R1) and still shares its process's heap, so an unrecovered panic in one can take the lot down (R2 failed). The platforms that fail even R1 are the ones still mapping each concurrent activity onto a heavyweight thread or a container, where you cannot afford a million, so you pool and share and lose R2 too.

**Error encapsulation** demands a fault boundary that holds. A bug here must not corrupt state there. Memory-safe languages, OS process isolation, container boundaries, and bulkhead patterns all serve R2. Shared-mutable-memory threading fails it by construction, which is the whole reason chapter 2 threw sharing out. R2 is the requirement most often claimed and least often delivered, because a system can look isolated at the diagram level while leaking through a shared cache, a shared connection pool, or a shared database row.

## R3 and R4: detection is not diagnosis

**Fault detection** demands that failure be observable, locally and remotely. This is the links-and-monitors machinery of chapter 5, and its modern cousins are liveness probes, heartbeats, and health checks. The subtle word is "remotely." Detecting that your own call threw is easy. Detecting that a process on another machine has died, and getting that fact delivered to you as something you can act on, is the hard half, and it carries the unreachable-not-dead caveat that chapter 5 lays out in full.

**Fault identification** is the requirement people forget, and it is the one that separates a system you can operate from one you can only restart. Detection tells you something broke. Identification tells you what and why, in enough detail to fix it later. There is a real tension here that the rest of this seminar has been leaning on: discard-and-restart actively fights identification. Restarting throws away the crashed process's memory, which is the forensic evidence, and a cascade of secondary crashes can bury the original error under noise. So R4 is not free alongside "let it crash," it is the discipline that makes "let it crash" survivable in the long run. You have to capture the crash report, and the first error in a cascade specifically, before recovery erases the scene. Armstrong's processes die with a reason attached, and OTP logs structured crash reports for exactly this; the modern analogue is the whole observability stack, stack traces, structured logs, distributed tracing. Skip R4 and you get a system that recovers beautifully and teaches you nothing, restarting forever around a bug you can never locate. Detection without identification is a system that survives but cannot improve.

## R5 and R6: continuity across time

**Code upgrade** demands that you change the software without stopping the system, because chapter 1's switch was never allowed to halt. Erlang's answer is genuine hot code loading: swap a module's code in a running VM while processes keep handling calls. This is the strong form, and it is hard, and here honesty is required. The industry mostly did not follow Armstrong here. The dominant way to satisfy R5 today is the weak form: do not upgrade the running instance, start new instances on the new code and drain the old ones. Rolling deployments, blue-green, canaries. That is the same "cattle, not pets" move from chapter 3 applied to upgrades, and it trades Erlang's in-place elegance for operational simplicity. Both satisfy R5. They satisfy it very differently, and the trade is worth naming rather than glossing.

**Stable storage** demands data that outlives a crash. This requirement is the quiet partner of the entire supervision story. Chapter 4 said restart is only safe if good state survives somewhere, and R6 is that somewhere. Erlang does not make stable storage a language primitive; it lives in libraries (dets, mnesia) and, in practice, in real databases. The modern world is thick with R6: write-ahead logs, replicated stores, durable queues. And R6 is exactly where this seminar hands off to the next ones. What "survives a crash" really guarantees, how a log makes a write durable and recoverable, what it costs to keep replicas consistent, is the subject Jim Gray and Barbara Liskov take up later in the series. Armstrong names the requirement and leans on storage to meet it. He does not try to solve durability himself, and the thesis is better for knowing its own boundaries.

## Why the rubric still works

The reason these six have aged so well is that Armstrong derived them from the problem, not from his solution. He did not write down "the features Erlang has." He wrote down what any system must provide to keep working while parts of it fail, and then built a language that provided them. That is why you can grade Kubernetes or a serverless platform against the same list and learn something real. A platform that nails R1 and R2 but fumbles R4 will be operable right up until the first novel failure, then go dark on you. One that has R5 but treats R6 as an afterthought will upgrade smoothly and lose data on the first hard crash. The list is a way of asking a new platform the only question that matters: when, not if, your components fail, which of the six do you actually have?

> **Principle:** Fault tolerance is not one feature. It is six, and a platform that has five of them has found you a new way to fail.
