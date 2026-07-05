# Reading Jerome Saltzer and Michael Schroeder

## *The Protection of Information in Computer Systems*

> Jerome H. Saltzer and Michael D. Schroeder, "The Protection of Information in Computer Systems," Proceedings of the IEEE, Volume 63, Number 9, September 1975, pages 1278 to 1308. Massachusetts Institute of Technology. An invited tutorial paper; earlier versions appeared at the 4th ACM Symposium on Operating System Principles (1973) and in Communications of the ACM (1974).

Most engineers meet this paper as a list. Eight design principles, still cited by name fifty years later: economy of mechanism, fail-safe defaults, complete mediation, open design, separation of privilege, least privilege, least common mechanism, psychological acceptability. The list is the enduring legacy, and it deserves to be. But the list is one short subsection of a thirty-page tutorial, and reading only the list misses what makes the principles land. The paper is a careful walk through how a computer actually protects information when several users share one machine, and the principles are the warnings the authors post along the way.

Saltzer and Schroeder wrote from inside the hardest working example of their day. Both worked on Multics at MIT, the system that pioneered most of what this paper describes: hardware descriptors, access control lists interpreted in software, rings of protection, and the idea that the supervisor should protect itself with the same machinery that protects users. When they compare capability systems to access control list systems, they are comparing designs they had built and measured. The paper reads like field notes from the frontier of a problem that was still open, and, in important ways, still is.

Two framings hold the paper together, and both matter more than the list. The first is the split between the protection mechanism and the security policy: the guard, the wall, and the door are mechanism, while who is allowed through is policy, and a good mechanism must serve many policies without being rebuilt. The second is the contrast between two ways to build the guard, the capability (a ticket you carry) and the access control list (a list the guard checks), a distinction that still organizes how we teach and build access control. Center the eight principles, but read them inside that frame, or they flatten into slogans.

## Why this seminar, tenth

This paper opens the security stretch of the book, and it also closes the design arc that ran through Lampson and Parnas. Economy of mechanism is Lampson's "keep it simple" pointed at the guard, and the authors say so, calling the supervisor that protects itself an example of it. A small trusted core that hides the security decision from everything above it is a Parnas module, information hiding applied to protection. And the whole paper is an answer to the question this series keeps circling: where should trust live? Saltzer and Schroeder's answer is that it should live in the smallest, most completely checked, least privileged core you can build and verify.

It also sets up what comes next. Once you can protect information inside one machine, the questions move onto the network, where Cerf and Kahn build an architecture for machines that do not trust each other and Clark explains the philosophy behind it. Complete mediation and least privilege, carried across a network, become what we now call zero trust. This seminar is where those ideas start, in hardware, on one shared computer.

## The four questions

1. **What problem were they solving?** Sharing. The moment several users share one computer, the system has to enforce an authority structure: who may read, who may modify, who may deny use, and it has to do so even when the intruder is a legitimate user. The mechanism that enforces this has to be separable from the policy, because the policy changes constantly.
2. **Why was the answer surprising?** It refused to be a product or a single trick. It offered a taxonomy, a clean split between mechanism and policy, and eight blunt principles it explicitly called warnings rather than rules. It argued the design should be public when secrecy felt safer, and that every access should be checked even when caching the answer was the obvious optimization.
3. **What survived?** The eight principles, by name, especially least privilege and fail-safe defaults. The capability-versus-access-control-list framing is still how access control is taught. What is contested is honest to report: a 2012 retrospective found that some principles thrived while others, like economy of mechanism and complete mediation, mostly did not, and the terms themselves get garbled in retelling.
4. **How should a working engineer read it today?** As the source of the vocabulary under IAM policies, firewall defaults, the reference monitor, zero trust, and the trusted computing base. And as a set of reminders that the principles are warnings, that a shared mechanism is a channel, and that a protection scheme people cannot use is not secure.

## Chapters

1. [Why sharing needs a guard](01-why-sharing-needs-a-guard.md). The problem sharing creates, the vocabulary the paper fixes, and the abstract model of wall, door, and guard.
2. [Mechanism, not policy](02-mechanism-not-policy.md). The frame that holds the paper together, and why one mechanism must serve many policies, discretionary and not.
3. [Building the guard: four principles](03-building-the-guard.md). Economy of mechanism, fail-safe defaults, complete mediation, and open design, the four about how the guard itself is built.
4. [Granting authority: four principles](04-granting-authority.md). Least privilege, separation of privilege, least common mechanism, and psychological acceptability, the four about how much to grant and to whom.
5. [Capabilities and access control lists](05-capabilities-and-acls.md). The two ways to build the guard, their tradeoffs in revocation and speed, and why real systems use both.
6. [Confinement and the shared mechanism](06-confinement-and-shared-mechanism.md). The borrowed program, covert channels, and least common mechanism as the ancestor of the side channel.
7. [Modern echoes](07-modern-echoes.md). Each principle mapped precisely onto IAM, default-deny, zero trust, public crypto, MFA, seL4, Spectre, and passkeys.
8. [Discussion and further reading](08-discussion-and-reading.md). The argument in one breath, what thrived and what did not, questions to argue about, and where the series goes next.

## A note on the source

Quotations come from the 1975 Proceedings of the IEEE version. This seminar is careful about the misreadings that have accumulated. Open design is Kerckhoffs's principle, that security must rest on the secrecy of keys and not of the mechanism, and it is not "open source," which it predates by roughly a century. Separation of privilege means requiring two keys or two conditions, and it is not the later "privilege separation" technique of splitting a program into least-privileged processes, which is a 2003 idea and really an application of least privilege. Fail-safe defaults means default-deny, not fail-safe in the reliability sense. Least common mechanism, the most forgotten of the eight, is the ancestor of shared-resource and side-channel worries, and this seminar gives it the space it deserves. The confinement problem the paper leans on is Lampson's, from 1973, not the authors'. And where modern frameworks like zero trust or the confidentiality-integrity-availability triad get read back into the paper, this seminar marks them as descendants, not as the same idea.
