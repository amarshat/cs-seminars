# CS-Seminars

**Modern graduate seminars on the classic papers of computer science.**

Some of the ideas that hold up your stack were written down decades ago. Logical clocks, the relational model, supervision trees, the end-to-end argument: the systems you ship this week are still arguments these papers started. But the papers themselves are hard to walk into. They assume you lived through the problem they were solving, and they were written for readers who already had.

This project closes that gap.

Each seminar here is a margin note on a foundational work of computer science: a chapter-by-chapter reading that reconstructs what the author was actually thinking, puts it back in its own time, and then asks the honest question. Does this still hold up, and where?

## What a seminar does

Every seminar works through four questions:

1. What problem was the author actually trying to solve?
2. Why was the answer surprising at the time?
3. Which parts survived, and which ones quietly got replaced?
4. How should a working engineer read this today?

The goal is not to teach you a language or a framework. It is to get at the ideas underneath operating systems, distributed systems, databases, networking, programming languages, security, and the cloud. Frameworks rot. These ideas keep showing up under new names.

Each seminar gives you:

- The historical setup: who, when, and what hurt
- A guided read of the original work
- A modern architectural reading, with diagrams
- Real systems that inherited the idea (and the ones that misread it)
- Discussion questions and a short reading list

## How to read it

Start anywhere, but the seminars are ordered so the arguments build on each other. If you are new here, read the Armstrong seminar first. It sets up the question that most of the others are also trying to answer: how do you keep a system correct when its parts are failing?

## The through-line

Read these works together and they stop being about Erlang, or TCP, or Paxos. They are answers to a small set of questions that never went away:

- How do independent components coordinate?
- How does a system stay correct when parts of it fail?
- How should state be represented, copied, and recovered?
- Where should trust live?
- How do you keep complexity survivable?

CS-Seminars reads the classics as answers to those questions, then checks the answers against the systems we build now.

## Seminars

| # | Author | Reading | Theme |
|---|--------|---------|-------|
| 01 | Joe Armstrong | *Making Reliable Distributed Systems in the Presence of Software Errors* | Failure-oriented architecture |
| 02 | Carl Hewitt | *A Universal Modular ACTOR Formalism for Artificial Intelligence* | The actor model |
| 03 | Tony Hoare | *Communicating Sequential Processes* | Synchronous message-passing |
| 04 | Leslie Lamport | *Time, Clocks, and the Ordering of Events in a Distributed System* | Causal order without a clock |
| 05 | Barbara Liskov | *Viewstamped Replication* (Oki & Liskov 1988; Liskov & Cowling 2012) | Crash-fault-tolerant state-machine replication |
| 06 | Jim Gray | *The Transaction Concept: Virtues and Limitations* | Transactions and atomic commit |
| 07 | Edgar F. Codd | *A Relational Model of Data for Large Shared Data Banks* | Data independence and the relational model |

More seminars are planned. They get added to this index as each one clears review.

## A note on method

These are not summaries, and they are not nostalgia. Every chapter is checked by a panel of adversarial reviewers (distributed systems, programming languages, reliability, security, and a systems historian) whose job is to catch folklore, shallow analogies, and modern ideas wrongly put in a dead author's mouth. If a chapter cannot survive that, it gets rewritten.

The test each chapter has to pass: if the original author were sitting in the room, would they recognize their own idea, and would they learn something from the modern reading?
