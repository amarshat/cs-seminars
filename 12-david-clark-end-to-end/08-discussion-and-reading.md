# 8. Discussion and further reading

## The argument in one breath

Across three works and two decades, Clark and his coauthors gave the internet its reasoning and then its reckoning. The end-to-end argument (1984, with Saltzer and Reed) is the principle: a function belongs at the endpoints if it can only be completely and correctly implemented there, which for reliability, ordering, encryption, and most interesting functions it can, so the network's version is redundant for correctness and justified only as a performance optimization. The Design Philosophy paper (1988) is the why: the internet's seven goals were ranked, survivability first because it was a military network and accountability last, and that ranking produced fate-sharing, keeping a conversation's state at its endpoints so it survives the loss of any gateway, which is the deep reason the core is a stateless datagram network. And the reckoning (2001 to 2002) is Clark turning on his own design: the end-to-end world assumed cooperating, trusted endpoints, and once that trust failed and commercial and government interests diverged, function and control flowed back into the middle as firewalls, NAT, and middleboxes, and the internet became an arena of tussle rather than a community of common purpose.

Read with the previous seminar, this closes the internet-architecture pair. Cerf and Kahn drew the blueprint; Clark explained why it was drawn that way and why the drawing no longer holds unamended.

## Questions worth arguing about

These are seminar questions. Several have no settled answer.

1. **Correctness or performance?** Take a function you have pushed into the "network," a proxy, an API gateway, a service mesh, a CDN. Be honest about which it is: a performance optimization the endpoints could live without, or a correctness or policy decision the endpoints can no longer make for themselves. The first is the tradeoff the argument invites; the second is the erosion it warns of.
2. **Where are your endpoints, really?** The 1984 paper says the hard part is identifying the ends. In a system of clients, edge caches, gateways, and backends, what is the true endpoint for a given function's correctness, and did you verify that, or assume it?
3. **What are your priorities, in order?** Clark ranked survivability first and accountability last, and the ranking explains the internet. Write your own system's goals in strict priority order. Does the order match what you actually built, and what is your last-place goal, billing, security, multi-tenancy, quietly costing you now?
4. **Does your state share fate?** Find state that lives in a middle tier, a sticky session, a stateful proxy, a broker. If that tier dies, which conversations die with it? Could the state move to the endpoint whose fate it should share?
5. **Can you still trust your endpoints?** The reckoning turned on losing that trust. Where does your design still assume well-behaved clients, and what happens when one is hostile, a spammer, an abuser, a malicious tenant? What did you have to move to the middle to cope, and what did that cost?
6. **Are you designing for tussle?** Where do parties with opposed interests meet inside your system, users against the platform, tenants against each other, product against compliance? Did you hardwire one side's victory, or design so the outcome can vary and the fight stays within the architecture?

## Further reading

Read the three core works in order, then the popular framing and the policy overlay that grew around them.

- **Saltzer, Reed, and Clark, "End-to-End Arguments in System Design" (1984).** The principle. Read the file-transfer example and the "Performance aspects" section together, so the correctness-versus-performance distinction stays intact.
- **Clark, "The Design Philosophy of the DARPA Internet Protocols" (1988).** The why. The seven ordered goals, fate-sharing, and Clark's own second thoughts about the datagram, soft state, and flows.
- **Blumenthal and Clark, "Rethinking the Design of the Internet" (2001).** The reckoning. Trust erosion, ISPs, and governments, and the risk to the internet's ability to host unanticipated applications.
- **Clark, Wroclawski, Sollins, and Braden, "Tussle in Cyberspace" (2002).** The reframing of the internet as an arena of competing interests, and the idea of designing for tussle rather than for harmony.
- **Reed, "Naming and Synchronization in a Decentralized Computer System" (MIT thesis, 1978).** Where a coauthor sharpened the end-to-end reasoning through atomic actions. Background for how the argument was found.
- **Isenberg, "The Rise of the Stupid Network" (1997).** The memorable popularization of "dumb network, smart edges." Read it, then read it against the 1984 paper to see what the slogan drops.
- **Wu, "Network Neutrality, Broadband Discrimination" (2003).** The policy overlay that invokes end-to-end. Read it to keep the policy argument separate from the technical one.

## Where the series goes next

Fate-sharing and the end-to-end argument both rest on a single idea: the endpoints hold the truth, and the network is not to be trusted with it. That works when there are two endpoints and each keeps its own state. It gets much harder when the truth must be shared, when a group of machines, any of which may fail, has to agree on one authoritative history. That is the problem of consensus, and it is where the series turns next, to Lamport's parliament of unreliable legislators and the algorithm that lets them agree anyway. It reconnects with the replication seminar and with logical time: once you cannot trust a single endpoint to survive, you need several to agree, and agreement among unreliable machines is its own deep problem. The end-to-end internet pushed state to the edges to survive failure; consensus asks how the edges themselves can hold a shared truth when they, too, fail.

The test this series puts to every chapter: if the authors were in the room, would they recognize their idea and learn something from the modern reading? Clark, uniquely among the authors in this series, has already done the recognizing and the revising himself, in public, across four papers. He would recognize all of it, because he wrote both the principle and its critique. What he might enjoy is watching the endpoints answer the reckoning on their own terms: told they could no longer trust the middle, they encrypted end to end until the middle went blind, reasserting the argument he first wrote down by turning its logic against the very forces that had eroded it.
