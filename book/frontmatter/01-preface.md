# Preface

Some of the ideas that hold up your stack were written down decades ago. Logical clocks, the relational model, supervision trees, the end-to-end argument, replicated state machines: the systems you ship this week are still arguments these papers started. But the papers themselves are hard to walk into. They assume you lived through the problem they were solving, and they were written for readers who already had.

This book closes that gap.

The title is a claim, and it has two edges. These papers describe machinery that is still running: not history, but the live infrastructure your systems sit on right now. Logical clocks order events inside databases in production today, supervision trees restart your containers, the relational model still quietly runs the world's data. And the ideas are still running too, still valid, still executing, resurfacing under new names decade after decade. This book reads the classics as descriptions of things that never stopped.

Each seminar is a margin note in the old sense, a *scholion*, the kind of explanatory note scribes once wrote alongside a classical text so the next reader could follow the argument. It reconstructs what the author was actually thinking, puts it back in its own time, and then asks the honest question. Does this still hold up, and where?

Every seminar works through four questions:

1. What problem was the author actually trying to solve?
2. Why was the answer surprising at the time?
3. Which parts survived, and which ones quietly got replaced?
4. How should a working engineer read this today?

The goal is not to teach you a language or a framework. It is to get at the ideas underneath operating systems, distributed systems, databases, networking, programming languages, and security. Frameworks rot. These ideas keep showing up under new names.

Read the seminars together and they stop being about Erlang, or actors, or TCP, or Paxos. They are answers to a small set of questions that never went away. How do independent components coordinate? How does a system stay correct when parts of it fail? How should state be represented, copied, and recovered? Where should trust live? How do you keep complexity survivable?

A note on method. These are not summaries, and they are not nostalgia. Every chapter was checked by a panel of adversarial reviewers whose job was to catch folklore, shallow analogies, and modern ideas wrongly put in a dead author's mouth. The test each chapter had to pass: if the original author were sitting in the room, would they recognize their own idea, and would they learn something from the modern reading? Where a chapter could not pass that, it was rewritten.

You can read the seminars in any order, but they are arranged so the arguments build on each other. If you are new here, start at the beginning.

Read the classics. Understand them in their own context. Apply them to the systems we build today.
