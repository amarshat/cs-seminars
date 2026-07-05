# 8. Discussion and further reading

## The argument in one breath

Sharing a computer forces a choice about who may do what, and the machine has to enforce that choice even when the intruder is a legitimate user. Saltzer and Schroeder framed the problem as a guard at a door in a wall, separated the mechanism that enforces access from the policy that decides it, and observed that the same mechanism, a capability you carry or an access control list the guard checks, can serve discretionary or mandatory policy. Because a secure system must prevent all unauthorized use, a negative requirement you cannot test, they offered eight design principles as warnings rather than rules: keep the mechanism small, default to denial, check every access, keep the design public, require two keys for the dangerous things, grant the least privilege, share the least mechanism, and make it usable. They walked through capabilities and access control lists honestly, showing that revocation and audit trade against speed and that real systems layer both and inherit a revocation gap at the seam. And they named the problem no mechanism fully solves: a confined program can still leak through any resource it shares, which is least common mechanism collecting its debt.

Read in the series, this closes the design arc and opens the security one. Economy of mechanism is Lampson's simplicity aimed at the guard, a small trusted core is a Parnas module hiding the security decision, and the whole paper answers the book's recurring question, where should trust live, with a single sentence: in the smallest core you can completely check.

## Questions worth arguing about

These are seminar questions. Several have no settled answer.

1. **Which of the eight does your system honor, and which does it only claim?** Least privilege is easy to say and hard to reach; most services run with more authority than their job needs. Complete mediation is quietly broken every time an authorization is cached. Pick your system and grade it honestly against all eight.
2. **What is your revocation lag?** Find a place where you cache an authorization decision, a session, a token, a shadow of a permission check. How long after a person loses access can they still act? Is that gap written down anywhere, or did it arrive by accident?
3. **Capability or access control list, and did you choose?** Bearer tokens are capabilities, with all the revocation pain the paper predicted. Is your system's mix of tickets and lists a design decision or an inheritance, and does it give you the revocation and audit you actually need?
4. **What do your tenants share, and is it a channel?** Least common mechanism says every shared thing is a potential information path. In a multi-tenant system, what hardware, cache, or service do tenants share, and what could leak across it? What would it cost to stop sharing it?
5. **Does your security fit the human?** Or do people route around it, reusing passwords, clicking through warnings, keeping data in unsanctioned tools because the sanctioned ones are too hard? Psychological acceptability says those workarounds are a security failure of your design, not of your users.
6. **What is your security actually resting on?** Somewhere in your system, is any protection relying on an attacker not knowing how it works? Name the secret doing the real work. If it is anything other than a key you can rotate, open design says you have a problem.

## Further reading

Start with the paper, then read the works it leans on and the honest retrospective on how the principles fared.

- **Saltzer and Schroeder, "The Protection of Information in Computer Systems" (Proc. IEEE, 1975).** The source. Section I for the principles and the frame, Section II for capabilities versus access control lists, Section III for the state of the art.
- **Anderson, "Computer Security Technology Planning Study" (1972).** The origin of the reference monitor and of the three violation categories the paper uses. The formalization of complete mediation.
- **Lampson, "A Note on the Confinement Problem" (CACM, 1973).** The source of confinement, which the paper leans on and does not claim. Short and foundational.
- **Dennis and Van Horn, "Programming Semantics for Multiprogrammed Computations" (CACM, 1966).** Where capabilities come from. Read it to see the ticket idea in its original form.
- **Saltzer, "Protection and the Control of Information Sharing in Multics" (CACM, 1974).** The Multics grounding in depth, from one of the authors. This is the real system behind the tutorial.
- **Bell and LaPadula, the security model (1973 onward).** The formalization of mandatory, nondiscretionary controls and the no-write-down rule that confinement needs. The military-security lineage the paper points to.
- **Whitten and Tygar, "Why Johnny Can't Encrypt" (USENIX Security, 1999).** Psychological acceptability, demonstrated. The study that launched usable security.
- **Provos, Friedl, and Honeyman, "Preventing Privilege Escalation" (USENIX Security, 2003).** Read it to see the name collision clearly: this "privilege separation" is an application of least privilege, not the paper's separation of privilege.
- **Smith, "A Contemporary Look at Saltzer and Schroeder's 1975 Design Principles" (IEEE Security and Privacy, 2012).** The honest scorecard on which principles thrived and which did not, and why.

## Where the series goes next

This paper answered where trust should live inside one computer. The next seminars take the question onto the network, where there is no shared supervisor to appeal to and no common hardware to lean on. Cerf and Kahn design an architecture for connecting networks that do not trust one another, and Clark explains the philosophy that decided where the intelligence and the trust should sit. There is a direct human thread, too: Jerome Saltzer is one of the three authors of the end-to-end argument that the Lampson and Parnas seminars already invoked and that the Clark seminar takes up, so the person who framed protection inside the machine also helped frame where function belongs across the network.

The principles cross the boundary with the reader. Complete mediation and least privilege, applied to machines that must assume the network is hostile, become zero trust. Open design, applied to the wire, becomes open protocols secured by public cryptography. The guard at the door does not go away when the door opens onto the internet. It multiplies.

The test this series puts to every chapter: if the authors were in the room, would they recognize their idea and learn something from the modern reading? They would recognize all of it, because the vocabulary is still theirs, down to the word "principal." They might be gratified that least privilege and default-deny became reflexes, and unsurprised that complete mediation keeps losing to caching and that a shared cache turned into Spectre. And being the careful writers they were, they would probably remind us of the sentence everyone forgets: these are warnings, not rules, and a design that violates one is not condemned, only asked to explain itself.
