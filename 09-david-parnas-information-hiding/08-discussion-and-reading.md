# 8. Discussion and further reading

## The argument in one breath

By 1972 everyone agreed to build systems out of modules, but no one had written down how to choose the boundaries, and the unspoken default was to follow the steps of the computation. Parnas took a KWIC index, decomposed it that conventional way and then a second way, by the design decisions most likely to change, and showed that the two could compile to the same program while behaving completely differently under change. A change to how lines are stored touched every module in the flowchart design and exactly one module in the second, because in the second the storage decision was a secret that one module kept. From that he drew the criterion: do not start from a flowchart; start from a list of decisions likely to change, and build each module to hide one. He was careful that a module is a responsibility, not a subroutine, that the interface should reveal as little as possible even down to an ordering, that hiding costs performance unless a tool assembles the boundaries away, and that hierarchy is a separate property from a clean decomposition. Small paper, one experiment, and much of modern software structure follows from it.

Read next to the Lampson seminar, this closes a two-part arc on design judgment. Lampson's catalog gave "keep secrets" as one hint among many, crediting Parnas. Parnas gives the argument that makes it a criterion rather than a slogan.

## Questions worth arguing about

These are seminar questions. Several have no settled answer.

1. **What are your secrets?** Take a system you own and write down the decisions most likely to change: the storage engine, the wire format, an external vendor, a business rule. Now look at your module boundaries. Do they match that list, or do they match the processing steps? If they match the steps, which change will teach you the difference?
2. **By step or by capability?** Where has splitting services by technical layer bitten you, a schema change that touched every service, a release that needed four teams to coordinate? And is your org chart, in Conway's sense, fighting the decomposition you want or producing it?
3. **Is over-hiding real?** Parnas argued for hiding aggressively, and his own confessed error was revealing too much. But is there a failure in the other direction, too many tiny modules, an interface around everything, indirection that hides nothing anyone needed hidden? Where is the line between hiding a decision and hiding for its own sake?
4. **Does your encapsulation hide a decision?** Pick a class with all-private fields and a getter for each. What decision does it actually hide? Could a client come to depend on its representation anyway, through those accessors, and if so what did "private" buy you?
5. **Where do you pay for a boundary?** Parnas said naive hiding is slow and asked the compiler to fix it. The compiler does, for function calls. It does not for network hops. When is a service boundary worth a cost that a function boundary would not be, and are you paying that cost on a boundary you drew for the wrong reason?
6. **Hierarchy or hiding?** Look at a layered architecture you know. Are the layers actually hiding decisions from each other, or just ordering who calls whom? Could a storage change still ripple up through all your clean layers, the way it did through Modularization 1?

## Further reading

Start with the paper, then follow information hiding forward into Parnas's own later work and the doctrines that grew on top of it.

- **Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules" (CACM 1972).** The source. Six pages, one experiment. Read the KWIC comparison and the conclusion.
- **Parnas, "A technique for software module specification with examples" (CACM 1972).** The companion on how to actually specify a hiding module's interface, which the main paper points to for the Line Storage and Circular Shifter definitions.
- **Parnas, "On the Design and Development of Program Families" (IEEE TSE, 1976).** Where the foreshadowing in the compiler-interpreter example becomes a theory: design the common decisions once and derive a family of related programs. Later than 1972, and worth keeping separate from it.
- **Parnas, Clements, and Weiss, "The Modular Structure of Complex Systems" (1984 to 1985).** Information hiding applied at real scale, the A-7E flight software and its module guide. The answer to "does this work outside a class project."
- **Parnas and Clements, "A Rational Design Process: How and Why to Fake It" (1986).** The honest sequel: real design is not the tidy top-down process the documents pretend, so produce the documentation as if it had been. Read it against any methodology that promises the design will follow from the steps.
- **Dijkstra, "The Structure of the THE Multiprogramming System" (CACM 1968).** The source of the hierarchy Parnas cites, and the reason he is careful to call hierarchy and clean decomposition separate properties.
- **Liskov and Zilles, "Programming with Abstract Data Types" (1974).** The programming-languages cousin, developed in parallel. Read it to see the same instinct become a language feature rather than a design criterion.
- **Meyer, "Object-Oriented Software Construction" (1988), and Larman, "Protected Variation" (IEEE Software 2001).** Where the open-closed principle is stated, and where the field later traced it back to Parnas. Useful for seeing how information hiding was absorbed into object-oriented doctrine, and how much of that doctrine is later folklore rather than anything in the 1972 paper.

## Where the series goes next

Parnas closes the design mini-arc. Lampson gave the practitioner's hints and Parnas gave the criterion, and together they answer how to structure a system so it survives change: draw the boundaries around what will change, hide the decision, keep the interface honest about what it reveals.

The series turns next from structure to trust. Saltzer and Schroeder's protection principles ask a related question about a different kind of boundary: not what a module is allowed to know, but what a subject is allowed to do, and where the checks belong. Least privilege, economy of mechanism, and complete mediation are, in part, information hiding read through a security lens, decisions about the smallest surface each part should expose. And the end-to-end argument, which Lampson already cited and which the David Clark seminar takes up directly, is the same instinct aimed at where a function should live rather than where a secret should. Read the design arc as the setup: once you know how to cut a system into parts that hide their decisions, the next questions are where trust sits between those parts and where the network ends and the application begins.

The test this series puts to every chapter: if Parnas were in the room, would he recognize his idea and learn something from the modern reading? He would recognize all of it, since the vocabulary is still his, and he might enjoy watching "secret" survive intact into bounded contexts and ports and adapters. He would also, being Parnas, point out that most of what gets called information hiding today is only marking fields private, and that the harder discipline he actually asked for, starting from the list of things likely to change, is still the part most often skipped.
