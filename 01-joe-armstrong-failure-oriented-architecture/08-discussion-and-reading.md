# 8. Discussion and further reading

## The argument in one breath

Armstrong started from a concession most engineers resist: in a large, long-running, constantly-changing system, some of the code is wrong right now, and you cannot test your way out of it. Everything else followed from taking that seriously. Isolate processes so a fault has a boundary. Let a broken process die rather than limp, because a dead process is safe and a corrupted one is dangerous. Put recovery above the failure, in a supervisor whose only job is to restart, with a budget so it escalates instead of flapping. Turn failure itself into a message, so the same code handles a local crash and a dead machine. And stay honest about the one thing none of it can fix: from the outside, you can never be sure whether a silent process is dead or merely unreachable.

That is a complete architecture, derived from a single premise, and the premise has only gotten more true. The systems most of us run now are larger and more distributed than Armstrong's switch, which means more of our code is wrong at any moment, not less.

## Questions worth arguing about

These are seminar questions, not quiz questions. Several have no settled answer, which is the point.

1. **Is "let it crash" portable?** The slogan rests on share-nothing isolation and cheap restart. Try to adopt it in a shared-memory, heavyweight-thread system and what actually happens? Which half of the idea survives the move, and which half quietly turns into a corrupted heap and a thread pool full of zombies?

2. **Where is your error kernel, and is it really small?** Armstrong concentrates correctness into a small core that must not fail. Every system has such a core whether or not anyone named it. Find yours. Is it actually small, actually simple, actually well-tested? Or has it grown features until the thing you most need to trust is the thing you understand least?

3. **Same shape, six orders of magnitude.** A supervisor reacts to a pushed exit signal in microseconds, inside one VM. A Kubernetes controller observes and reconciles in seconds, across machines. What classes of fault does that gap, and the edge-triggered versus level-triggered difference, let through? What can Armstrong's model catch that the cloud's coarse-grained version structurally cannot, and the other way around?

4. **What does the nine-nines story teach?** The AXD301's famous reliability number came, by Armstrong's own account, from a slide with undocumented methodology. The number got cleaner every time it was retold. What does that say about how our industry measures reliability, and about the difference between a system that is reliable and a system that is believed to be?

5. **Did we make the right trade on upgrades?** Erlang's hot code loading swaps code in a running system. The industry mostly walked away from that and chose rolling restarts instead. Was that a retreat from a hard problem, or a wise simplification? What did we give up, and what did we get?

6. **Restart after a partition.** A supervisor that restarts a process it believes dead can create a second live copy if the first was only unreachable. When has this bitten you? What did you add (fencing, leases, quorum, idempotency) to make recovery safe, and where in the stack did it belong?

7. **Does designing for survival make us lazy about correctness?** The uncomfortable critique: if "we'll just restart it" is always available, does failure-oriented architecture quietly excuse not fixing the bug? Where is the line between resilient and negligent?

## Further reading

Start with the source. It is more readable than its reputation suggests.

- **Joe Armstrong, *Making Reliable Distributed Systems in the Presence of Software Errors* (2003).** The thesis itself. The early chapters on the problem domain and concurrency-oriented programming are the heart; the later case studies are where Armstrong is most candid about what was and was not measured. Hosted by Ericsson at erlang.org.

- **Armstrong, *Programming Erlang* (2nd ed.).** The practical companion. Read it for how the ideas feel in code, not as a language reference.

- **Cesarini and Thompson, *Erlang Programming*, and Cesarini and Vinoski, *Designing for Scalability with Erlang/OTP*.** The second is the best treatment of OTP supervision, restart strategies, and the patterns chapter 4 only sketched.

- **Armstrong, "A History of Erlang" (HOPL III, 2007).** The honest origin story, including the dead ends. Good antidote to the tidy version of history.

- **Candea and Fox, "Crash-Only Software" (HotOS 2003), and "Microreboot" / recursive restartability.** The operating-systems tradition arriving at the same conclusions in the same era, from a different direction. The convergence is the lesson.

- **Nygard, *Release It!*** The modern, operational version of these ideas: bulkheads, circuit breakers, timeouts, the failure modes that page you at 3am. Read it alongside chapter 3's asterisks.

## Where the series goes next

This seminar kept running into limits it could name but not resolve, and those limits are the next readings.

- The processes Armstrong isolates are close cousins of **Carl Hewitt's actors**, a formal model Erlang's designers reached the same destination as without drawing on it. That independent convergence is the subject of the next seminar in this series.
- The dead-versus-unreachable impossibility that haunts chapter 5 is **Leslie Lamport's** territory: ordering, logical clocks, and eventually consensus.
- The split-brain risk in restart-after-partition is what **Liskov and Castro** confront head-on when nodes can be not just broken but malicious.
- And R6, stable storage, the durability Armstrong leans on but does not build, is where **Jim Gray's** transaction concept takes over.

Read this way, Armstrong is not the last word on reliability. He is the clearest statement of the problem the rest of the series spends its time solving.
