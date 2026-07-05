# 6. The split, and the honest scope

## The problem: the paper is a blueprint, not the building

It is tempting to read the 1974 paper as if it described the internet we have, and doing so gets both the credit and the mechanics wrong. This chapter draws the line between what Cerf and Kahn actually specified and what came later, because the most common errors about this paper are errors of date.

Start with their own modesty. The paper calls itself a "protocol design and philosophy," and the conclusion is explicit that the work is not finished: "The next important step is to produce a detailed specification of the protocol so that some initial experiments with it can be performed." It leaves real questions open. Retransmission timeout durations are "unspecified." The initial synchronization of sequence numbers is deferred. The duplicate-message problem at teardown, which Steve Crocker pointed out, is flagged as something that "must be solved," with the note that they "do not go into further detail here." This is a blueprint offered for experiment, and it says so.

## The split that made TCP/IP

The single biggest gap between 1974 and today is the one hiding in the name. In 1974 there is one Transmission Control Program that does addressing, routing help, reliability, ordering, flow control, and connection management together. That monolith was pulled apart later in the decade. As people tried to build real applications, it became clear that not everyone wanted what TCP provided: packet voice and simple request-reply exchanges did not want retransmission and in-order delivery, which for them added delay and bought nothing. So the addressing-and-routing part was separated from the reliability part, so that the bare packet-delivery service could be used on its own.

| Function | In 1974 | Later became |
|---|---|---|
| Addressing, routing | inside TCP | IP (RFC 791, 1981) |
| Reliability, ordering | inside TCP | TCP (RFC 793, 1981) |
| Bare datagrams | not offered | UDP (RFC 768, 1980) |

The split was worked out in the late 1970s, around 1978, and standardized in 1981 when IP and TCP became separate specifications, with UDP arriving just before them in 1980. This is the origin of the layered TCP/IP you know, and of the idea that IP is the one thing everything shares while TCP and UDP are choices above it. None of that layering is in the 1974 paper. Read backward, the split looks inevitable; at the time it was a real design decision that took years.

## What else arrived later

Several other familiar pieces are absent or embryonic in 1974, and it is worth dating them so they are not read back into the paper. The address is eight bits of network and sixteen of host, good for 256 networks, which the authors thought "sufficient for the foreseeable future"; the foreseeable future arrived fast, and the address grew into IPv4's 32 bits in 1981 and then IPv6's 128 in the late 1990s. In-network fragmentation, which the 1974 gateways perform, fell out of favor and was later replaced by having the source discover the smallest packet size along the path, with IPv6 removing router fragmentation entirely. And crucially, the paper has flow control but not congestion control. The receiver's advertised window keeps a fast sender from swamping a slow receiver, but nothing in 1974 keeps the senders collectively from overwhelming the network's interior. That gap was real: the internet suffered congestion collapse in the mid-1980s, and congestion control was added to TCP by Van Jacobson in 1988, fourteen years on. The 1974 design assumed, as chapter 4 noted, that the underlying networks were fairly well behaved.

## What survived

Set against all that change, what is striking is how much of the architecture held. The gateways between independent networks survived, grown into routers. The common host-to-host protocol survived. The connectionless core survived, and so did reliability at the edges. The bet of chapters 1 through 5, keep the network simple and independent and push the intelligence to the hosts, is the thing that did not change, through every revision of the packaging. The acronym drifted, the address grew, the monolith split, congestion control was bolted on, but the shape is the one Cerf and Kahn drew. That is the right way to hold the paper: not as the specification of the internet, but as the architecture the internet kept even as it rebuilt everything else.

> **Principle:** Separate the architecture from its first implementation. Cerf and Kahn's monolithic program was split, regrown, and patched for decades, but the arrangement it proposed, dumb independent networks joined by simple gateways with reliability at the edges, is what survived. Judge a design by the shape that outlives its own code.
