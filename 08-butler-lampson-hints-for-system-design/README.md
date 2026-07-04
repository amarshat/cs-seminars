# Reading Butler Lampson

## *Hints for Computer System Design*

> Butler W. Lampson, "Hints for Computer System Design," Proceedings of the 9th ACM Symposium on Operating Systems Principles (SOSP), in ACM SIGOPS Operating Systems Review, Volume 17, Number 5, October 1983, pages 33 to 48. Reprinted in IEEE Software, Volume 1, Number 1, January 1984, pages 11 to 28. Xerox Palo Alto Research Center.

Every seminar so far has read one deep result: a model, a theorem, a mechanism. This one is different, and it is different on purpose. Lampson did not set out to prove anything. He had spent fifteen years building systems that shipped, and a few that did not, and he wrote down the judgment he wished he could hand to the next designer. The result is a catalog of more than two dozen design hints, each compressed into a slogan and paid for with a real example from a real machine.

The examples are not toys. Lampson helped build the Alto, the first computer most people would recognize as personal; the Dorado behind it; the Bravo editor that became Word; the Star office system; the Pilot operating system; the Dover laser printer; and Grapevine, an early distributed mail and naming service. He had a hand in the Ethernet. Before PARC he built the SDS 940 time-sharing system at Berkeley. When he says an interface was too general, or that a cache should have been a hint, he is usually talking about code he or his colleagues wrote and then had to live with. In 1992 he received the Turing Award for exactly this body of work.

The title is a pun, and the pun is the point. A "hint" in everyday English is a piece of friendly advice, which is what the paper appears to be. But halfway through, Lampson defines "hint" as a technical term: the saved result of a computation that speeds up the common case, may be wrong, and therefore must be checked against the truth, with a correct fallback when it turns out to be stale. A cache entry that is allowed to lie. One of the hints in the paper is literally "use hints." So the paper delivers advice as hints, teaches hints as a technique, and, read closely, offers all of its own advice in the technical sense: not laws, not guaranteed, correct often enough to be worth having, and always to be checked against the system in front of you. Miss that and you have read a listicle. Catch it and you have the paper.

## Why this seminar, eighth

The series pauses here. The first seven seminars each drove at one hard idea and followed it down. Lampson's paper is the interlude where a master builder steps back and talks about judgment: how to choose an interface, where to spend simplicity, when to be fast instead of correct, how to keep a large system from collapsing under its own changes. It reads as a hinge.

It also sets up what comes next. The hints about interfaces, about hiding what is likely to change while exposing what clients need, are Parnas's information hiding applied by a practitioner. Lampson cites Parnas directly, and the next seminar reads Parnas as the origin of the criterion Lampson is using. The fault-tolerance hints turn on the end-to-end argument, which Lampson attributes to Saltzer, Reed, and Clark, and which David Clark's seminar takes up later on its own terms. And the paper looks backward too. Its crash-and-restart recovery ("one crash a week is a cheap price"), its logs, and its atomic actions are the same shapes the Armstrong and Gray seminars already covered, written down here twenty years before Armstrong built a language around them.

## The four questions

1. **What problem was Lampson solving?** How to make good decisions when designing a system, as opposed to an algorithm. The requirement is vague and keeps changing, the internal structure is large and full of interfaces, and there is no clear measure of success. There is rarely a best design, so the real skill is avoiding a terrible one. He wanted to pass on the judgment that steers you clear.
2. **Why was the answer surprising?** Because it refused to become a method. The early 1980s were thick with grand methodologies, and Lampson wrote down blunt, contradictory rules of thumb, called them hints, and openly disclaimed that they were consistent, foolproof, or laws. Then he made "hint" a technical term and built one of the hints out of it. The advice and the mechanism share a name deliberately.
3. **What survived?** Almost all of it, usually under newer names. Caches and hints run through every layer of a modern stack. End-to-end, make it fast, do one thing well, keep interfaces stable: these are defaults now. What got harder is the part he already flagged, the tensions. His contradictions are today's standing debates: simplicity of a service against the complexity of a distributed system, the mounting cost of never breaking an interface.
4. **How should a working engineer read it today?** As a checklist of judgment, not a rulebook. Read the contradictions as the content, not as sloppiness. And notice, once you know the technical meaning of the word, how much of what you build is hints.

## Chapters

1. [The catalog and the pun](01-the-catalog-and-the-pun.md). What kind of paper this is, the two axes of its summary table, the disclaimer, and the double meaning of "hint."
2. [Keep it simple, get it right](02-keep-it-simple-get-it-right.md). The interface as a small programming language, the three requirements that fight each other, and why generality is the standing danger.
3. [Don't hide power](03-dont-hide-power.md). Make it fast rather than powerful, expose what clients need, and leave the rest to the client. The half of the argument about exposing the good.
4. [Designing for change](04-designing-for-change.md). Stable interfaces, a place to stand, planning to throw one away, and keeping secrets. Hiding what changes, and the handoff to Parnas.
5. [Speed, and the normal case](05-speed-and-the-normal-case.md). Optimize the common case, handle the worst case separately, and the honest lesson that you cannot optimize a general system, so aim to avoid disaster.
6. [The hint](06-the-hint.md). The technique defined precisely: a fast, possibly-wrong value checked against the truth. The pun paid off, from file labels to branch predictors.
7. [End-to-end, logs, and atomic actions](07-end-to-end-logs-atomic-actions.md). The fault-tolerance hints, their debts to Saltzer and Gray, and the crash-and-restart philosophy that predates Armstrong.
8. [Contradictions, and how to read it today](08-contradictions-and-reading-today.md). The deliberate tensions, judgment over rules, the recursion in the title, discussion questions, and where the series goes next.

## A note on the source

Quotations come from Lampson's own slightly revised version of the 1983 paper. Three things are worth stating up front. First, the citation itself is a small trap: Lampson's personal copy and the Microsoft Research listing both give the volume as "15, 5," but the ACM Digital Library and DBLP confirm Operating Systems Review 17(5). This seminar uses 17(5). Second, Lampson is a curator. Several of the most quoted hints are other people's: "plan to throw one away" is Brooks, "keep secrets" is Parnas, the end-to-end argument is Saltzer, Reed, and Clark. This seminar attributes each one and grounds every example in the actual PARC system it came from. Third, the hints contradict each other, and Lampson says so in his own disclaimer. Where a retelling would smooth the contradictions into a tidy list, this seminar keeps them, because the contradictions are where the judgment lives.
