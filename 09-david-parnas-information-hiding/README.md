# Reading David Parnas

## *On the Criteria To Be Used in Decomposing Systems into Modules*

> D. L. Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules," Communications of the ACM, Volume 15, Number 12, December 1972, pages 1053 to 1058. Carnegie-Mellon University. Received August 1971, revised November 1971.

By 1972 everyone agreed that you should build a system out of modules. The managerial case was obvious: split the work, let separate groups build the pieces, assemble the result. What no one had written down was the part that actually decides whether modularity pays off. As Parnas puts it, "usually nothing is said about the criteria to be used in dividing the system into modules." Everyone knew to cut. Nobody said where.

This paper is one experiment, and its power is in how small it is. Parnas takes a toy system, a KWIC index, the kind of keyword-in-context listing a good programmer could write in a week, and decomposes it two different ways. The first is the decomposition almost every programmer would produce: one module per step in the processing, input then shift then alphabetize then output, the shape of a flowchart. The second cuts along a different line entirely: one module per design decision that is likely to change, with each module built to hide that decision from all the others. Both decompositions produce the same running program. The boundaries are in different places, and that difference is the entire argument.

Then he runs the test. He lists the decisions likely to change (the input format, whether the lines live in core, how characters are packed, whether the shifts are stored or computed, when the sort happens) and traces each change through both designs. In the flowchart version, a change to how lines are stored forces a change in every module, because every module touches the shared storage format. In the second version, that knowledge is sealed inside one module, and the change stops there. From that single contrast Parnas extracts a criterion he had named a year earlier: information hiding. Decompose a system around the secrets it needs to keep, not around the steps it performs.

## Why this seminar, ninth

This is the second half of a two-part arc on design judgment. The Lampson seminar just before it is a working engineer's catalog of hints, and one of those hints is "keep secrets of the implementation," which Lampson explicitly credits to Parnas. This seminar reads the source of that hint. Where Lampson gives you the practitioner's rule of thumb, Parnas gives you the argument and the experiment behind it, and states the criterion precisely enough to act on.

It also connects sideways and forward. Barbara Liskov was arriving at a close cousin of this idea at the same time, from the programming-languages side, as data abstraction and the abstract data type. The two are convergent, not one descended from the other, and reading them together shows a single insight surfacing in two communities at once. Forward, information hiding becomes the intellectual root of encapsulation, of the module and package systems in every modern language, and of the service-boundary arguments that dominate architecture today. It is one of those rare papers whose central word, "secret," you still use without always remembering where it came from.

## The four questions

1. **What problem was Parnas solving?** Not whether to modularize, which was settled, but how to choose the boundaries. The default cut, one module per processing step, produced modules that all depended on the same shared data formats, so a single change spread across the whole system. He wanted a criterion for cutting that made change cheap and let groups work independently.
2. **Why was the answer surprising?** Because it told you not to start with a flowchart, the one move every programmer was trained to make first. And it redefined the unit: a module is not a subroutine and not a step in the computation. It is a secret, a design decision you expect will change, wrapped so nothing else can come to depend on it.
3. **What survived?** The criterion, almost entirely, under the name information hiding. It is the backbone of encapsulation, of stable interfaces, of service boundaries and plugin systems. What gets misremembered is what a secret is. Flatten it to "private variables" and you lose the "likely to change" part that was the whole point.
4. **How should a working engineer read it today?** As the argument under every boundary you draw. Put the module around what you expect to change, not around the steps of the computation. And read it with Parnas's own honesty about the cost: hiding is not free, and a module is not the same thing as a subroutine, or a microservice.

## Chapters

1. [The criterion nobody stated](01-the-criterion-nobody-stated.md). Everyone agreed to modularize; no one said how to cut. The three benefits, and why the choice of boundary is the real question.
2. [KWIC, and the obvious cut](02-kwic-and-the-obvious-cut.md). The example system, and Modularization 1: one module per processing step, the shape of a flowchart.
3. [The same system, cut by secrets](03-the-same-system-cut-by-secrets.md). Modularization 2: one module per design decision likely to change, and why the running program can be identical.
4. [Which change ripples](04-which-change-ripples.md). The experiment's result. Trace a storage change through both designs and watch one confine it while the other spreads it everywhere.
5. [What a secret is, and is not](05-what-a-secret-is.md). A secret is a decision likely to change, not a private field. Why this is not encapsulation, not OOP, and not "hide everything."
6. [A module is not a subroutine](06-a-module-is-not-a-subroutine.md). The cost of hiding, the inlining answer, and why hierarchy is a separate property from a clean decomposition.
7. [Modern echoes](07-modern-echoes.md). Microservices by layer versus by capability, hexagonal architecture, plugins, and Conway's law, read structurally.
8. [Discussion and further reading](08-discussion-and-reading.md). The argument in one breath, questions to argue about, and where the series goes next.

## A note on the source

Quotations come from the 1972 CACM paper. This seminar is careful about the misreadings that have grown over fifty years. Information hiding is not encapsulation and not object orientation: the secret a module keeps is a design decision likely to change, and OOP with private fields is only one later mechanism for keeping it, arriving well after 1972. The criterion is specifically "hide what is likely to change," not "hide everything" and not "break the program into functions." The open-closed principle (Meyer, 1988) and the SOLID framing (Martin and Feathers, 2000s) are later folklore often retrofitted onto this paper, and Parnas's own program-families work (1976) and the A-7E project (from 1977) are later too. Where a retelling would smooth the paper into "make things private," this seminar keeps Parnas's sharper and more demanding claim, and keeps his own honesty that hiding has a cost.
