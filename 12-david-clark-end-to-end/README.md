# Reading David Clark

## *The End-to-End Internet*

> Jerome H. Saltzer, David P. Reed, and David D. Clark, "End-to-End Arguments in System Design," ACM Transactions on Computer Systems, Volume 2, Number 4, November 1984, pages 277 to 288 (revised from the Second International Conference on Distributed Computing Systems, Paris, 1981).
>
> David D. Clark, "The Design Philosophy of the DARPA Internet Protocols," Proceedings of SIGCOMM '88, Computer Communication Review, Volume 18, Number 4, August 1988, pages 106 to 114.
>
> Marjory S. Blumenthal and David D. Clark, "Rethinking the Design of the Internet: The End-to-End Arguments vs. the Brave New World," ACM Transactions on Internet Technology, Volume 1, Number 1, August 2001. And David D. Clark et al, "Tussle in Cyberspace: Defining Tomorrow's Internet," SIGCOMM '02.

The previous seminar drew the internet's shape: dumb network, smart edges. This one supplies the reasoning behind that shape, the priorities that produced it, and the honest reckoning with how it eroded. The through-figure across all of it is David Clark, who took over architectural responsibility for TCP/IP in 1981 and spent the next two decades explaining why the internet is the way it is, and then why that way stopped holding.

Three works carry the argument, and they are three distinct points made at three distinct times. The end-to-end argument (1984) is the principle: a function should not be built into the lower levels of a system if it can only be completely and correctly implemented with knowledge that lives at the endpoints. It is not Clark's alone; it is Saltzer, Reed, and Clark, and the same Saltzer who co-wrote the protection paper two seminars back. The Design Philosophy paper (1988) is the why: it lists the internet's seven goals in strict priority order, with survivability first because this was a military network and accountability last, and introduces fate-sharing, the reason the core could be a stateless datagram network. And the reckoning (2001 to 2002) is Clark turning on his own creation, arguing that the end-to-end world assumed a trust between endpoints that no longer exists, and that commercial and government interests have pushed function back into the middle.

One nuance to fix before reading, because it is the most common misreading. The end-to-end argument is not "put everything at the edges and make the network dumb." It is a claim about correctness: the network trying to be reliable is redundant for correctness, because the endpoints must check anyway. But the very same argument explicitly permits a lower layer to implement a function as a performance optimization, like a wireless link retransmitting a lost frame. Correctness lives at the edges; performance help in the middle is allowed. Drop that distinction and you have a slogan, not the argument.

## Why this seminar, twelfth

This closes the internet-architecture pair. Cerf and Kahn built the blueprint; Clark supplies the reasoning and the reckoning, and the previous seminar handed off to this one deliberately. Together they are the sharpest statement of the question this whole series keeps circling: where should function and trust live, in the core of a system or at its edges?

The connections run in several directions. Fate-sharing is the deep answer to why the internet's core is stateless, which is the design Cerf and Kahn chose, so this seminar explains the choice the last one made. The end-to-end argument shares an author, Saltzer, and a preoccupation with trust, with the protection seminar: Saltzer and Schroeder asked where to put the guard, and here the reckoning is that the guard has to move because the endpoints can no longer be trusted. That loss of trust is the same one that produced zero trust and the reference monitor. And the whole design rests on the assumption that the network will lose and reorder data and that recovery belongs at the edge, the same unreliability that Lamport and Armstrong built against.

## The four questions

1. **What problem were they solving?** Two, at two levels. The end-to-end argument answers a general design question: where in a layered system should a function live, the core or the endpoints? The Design Philosophy paper answers a specific one: what goals, and in what order, should shape an internetwork built for the military.
2. **Why was the answer surprising?** Because it argued that making the network more reliable is often wasted effort. If the endpoints must check correctness anyway, and they must, then the network's internal guarantees are redundant for correctness, useful only for performance. And because the priorities were not what a commercial designer would choose: survivability first, billing and accountability last, which is why the internet is so hard to monetize, manage, and secure.
3. **What survived?** The end-to-end principle became the internet's defining rule and the reason it could host applications no one had imagined. Fate-sharing kept the core stateless. What eroded is trust: spam, denial-of-service, and malware meant the endpoints could no longer be trusted, and ISPs and governments wanted a say, so function flowed back into the middle as firewalls, NAT, and middleboxes. Clark documented the erosion himself.
4. **How should a working engineer read it today?** As the reasoning behind the internet's shape and its honest post-mortem in one seminar. Keep the correctness-versus-performance distinction, because most of the "violations" you will meet are the permitted performance kind. And take the reckoning seriously: the clean end-to-end world assumed a cooperation between endpoints that the real world does not provide.

## Chapters

1. [The principle, stated carefully](01-the-principle-stated-carefully.md). The end-to-end argument, the careful-file-transfer example, and the correctness-versus-performance distinction that is the whole point.
2. [A guideline, not a dumb network](02-a-guideline-not-a-dumb-network.md). The range of examples, packet voice, identifying the ends, and why this is a design guideline rather than "make the network stupid."
3. [The goals, in priority order](03-goals-in-priority-order.md). The Design Philosophy paper's seven goals, why the order is the argument, and why survivability first and accountability last still shape the internet.
4. [Fate-sharing](04-fate-sharing.md). Keep a conversation's state at its endpoints so it shares their fate. The deep reason the core is a stateless datagram network, and the bridge back to Cerf and Kahn.
5. [Types of service, and the split](05-types-of-service-and-the-split.md). Why one protocol became TCP and IP, why the datagram is a building block and not a service, and Clark's own second thoughts.
6. [The reckoning](06-the-reckoning.md). Clark turning on his own design: the loss of trust between endpoints, commercial and government interests, and the middleboxes they produced.
7. [Modern echoes](07-modern-echoes.md). End-to-end encryption against an untrusted middle, middleboxes justified by the performance clause, fate-sharing as stateless services, and zero trust.
8. [Discussion and further reading](08-discussion-and-reading.md). The argument in one breath, questions to argue about, and where the series goes next.

## A note on the sources

Quotations come from the four works above. This seminar keeps three things straight that retellings usually blur. First, the end-to-end argument is about correctness, and it explicitly allows performance help in lower layers, so it is not the same as "dumb network." Second, the three ideas are three papers with three dates: the principle (1984, itself revised from 1981), the goals (1988), and the reckoning (2001 to 2002). Third, the 1988 goals are seven and they are ordered, and the order is the argument, not an unordered wish list. The end-to-end argument is Saltzer, Reed, and Clark, not Clark alone, even though Clark anchors this seminar. And where "net neutrality" gets read back into the argument, this seminar treats it as a later policy overlay that invokes end-to-end, not as the original claim.
