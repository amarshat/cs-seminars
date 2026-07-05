# 3. The goals, in priority order

## The problem: why is the internet shaped like this?

The end-to-end argument tells you how to place a function. It does not tell you why the internet, in particular, came out connectionless, stateless in the middle, and indifferent to billing. For that, Clark wrote a second paper four years later, "The Design Philosophy of the DARPA Internet Protocols," to capture the reasoning that the specifications left out. Its abstract says the motivation for the datagram "has been greatly misunderstood," and its method is to state the goals the architecture was actually built to meet.

The fundamental goal is one sentence: "to develop an effective technique for multiplexed utilization of existing interconnected networks." Every word is chosen. Multiplexed, because the technique would be packet switching. Existing, because the project would connect networks that already ran, not design a single unified network, since the networks "represent administrative boundaries of control" and the ambition was "to come to grips with the problem of integrating a number of separately administrated entities into a common utility." Interconnected, by a layer of packet switches called gateways. That is the previous seminar's architecture, stated as a goal.

## Seven goals, and the order is the argument

Then comes the part that is almost always mishandled. Clark lists seven second-level goals, and he insists they are ranked:

| # | Goal, in priority order |
|---|---|
| 1 | Survive lost networks or gateways |
| 2 | Support many types of service |
| 3 | Accommodate varied networks |
| 4 | Permit distributed management |
| 5 | Be cost effective |
| 6 | Low-effort host attachment |
| 7 | Make resources accountable |

The first goal, in full, is "Internet communication must continue despite loss of networks or gateways." The last is "The resources used in the internet architecture must be accountable." And Clark could not be clearer that the sequence is not incidental: "It is important to understand that these goals are in order of importance, and an entirely different network architecture would result if the order were changed." He calls it "not a 'motherhood' list, but a set of priorities which strongly colored the design decisions." The reason survivability sits first and accountability last is stated plainly: "since this network was designed to operate in a military context, which implied the possibility of a hostile environment, survivability was put as a first goal, and accountability as a last goal." And the counterfactual: "An architecture primarily for commercial deployment would clearly place these goals at the opposite end of the list."

Read the list as an unordered set of nice properties and you have thrown away the paper's thesis. The claim is that priorities produce architecture, and that these particular priorities produced this particular internet.

## What the order bought, and what it cost

Follow the top of the list and you get the internet's strengths. Survivability first drove the decision that the network must keep a conversation alive through the loss of gateways, which drove fate-sharing, which drove the stateless datagram core, which is the next chapter. The high-ranked goals of supporting varied networks and varied services drove the thin, undemanding interface that let the internet run over everything and carry anything. These are the properties that made the internet spread.

Follow the bottom of the list and you get the internet's chronic troubles, and Clark says so directly. Accountability was dead last, and "at the present time, the Internet architecture contains few tools for accounting for packet flows." Cost-effectiveness ranked below distributed management and network variety, so the internet tolerates overhead that a more specialized design would not. Distributed management across separate administrations, ranked fourth, "has certainly been met in certain respects" but remained one of "the most significant problems with the Internet today," especially in routing. The internet is hard to bill, hard to manage across administrative boundaries, and, as the reckoning will show, hard to secure, and all three trace to the same fact: the goals that would have addressed billing and management were ranked last, and security was not on the list at all, because in 1975 this was a military research network and no one was trying to make money or stop hostile users with it. Clark's own conclusion names the gap: "in certain situations, the priorities of the designers do not match the needs of the actual users. More attention to such things as accounting, resource management and operation of regions with separate administrations are needed."

There is even a subtlety about the ordering that rewards attention. Survivability is first among the second-level goals, but Clark notes it "is still second to the top level goal of interconnection of existing networks." Had survivability truly been paramount, a single purpose-built network might have been more robust than a patchwork of borrowed ones. The internet chose interconnection first and survivability within that constraint, which is why it detects failures with weak, internet-level mechanisms rather than trusting the networks to report their own.

> **Principle:** An architecture is its designers' priorities made concrete, and reordering the goals yields a different system. The internet ranked survival first and accountability last because it was built for war, not commerce, which is the single fact that best explains both why it survives anything and why it is so hard to bill, manage, and secure.
