# 8. Discussion and further reading

## The argument in one breath

One lab, three answers, a decade apart. MapReduce restricts the programming model to two functions so the framework can own distribution and failure, recovering by re-executing the deterministic pieces. Bigtable throws away joins, SQL, and multi-row transactions to spread a sparse sorted map across thousands of machines, and leans on Chubby, a Paxos-backed lock service, for the coordination it refuses to do itself. Spanner swings the pendulum back to SQL and ACID at global scale, by running two-phase commit over shards that are each Paxos-replicated, and by giving transactions globally meaningful timestamps through TrueTime, which exposes clock uncertainty as a bounded interval and waits it out. Read as an arc, the three papers are a field surrendering the relational model for scale and then, once consensus replication and bounded clocks matured, reclaiming it. Spanner is where Codd, Gray, Lamport, and Liskov are composed into one system, and it does not beat CAP; it chooses consistency and pays for availability where partitions are rare.

## Questions worth arguing about

1. **Do you need the far end of the pendulum?** Most systems are not Google. A single well-run relational database, perhaps with read replicas, is the right answer far more often than the architecture-diagram version of your ambitions admits. Where have you reached for a distributed store out of scale cargo-culting when one machine would have done?
2. **What did you actually give up?** If you run a NoSQL store, name the join or the cross-partition transaction you surrendered, and then check whether the application quietly reimplemented it in client code, usually more slowly and less correctly than the database would have.
3. **Where does a restricted interface pay off?** MapReduce restricted the model on purpose and inherited the framework's power. Where in your stack does a narrow interface, a schema, a query language, a pure-function boundary, give you operational freedom, and where has an over-general interface taken freedom away?
4. **Do you concentrate consensus or scatter it?** Do you run one coordination service that everything leans on, or does each component reinvent leader election and split-brain avoidance? And do you know what breaks when that one service is briefly down, the Chubby question stated as a percentage?
5. **What is your epsilon?** If you order events across machines by wall-clock timestamps anywhere, you are implicitly assuming a maximum clock skew. What is it, and what happens when it is exceeded? Most teams cannot answer, which is the point of TrueTime making the bound explicit.
6. **Which does your database choose under partition?** For your most important datastore, when the network splits, does it stay consistent and go unavailable, or stay available and risk divergence? Knowing the answer, rather than assuming it, is the difference between a design and a hope.

## Further reading

Read the four papers as a sequence; the arc is the argument.

- **Dean and Ghemawat, "MapReduce" (2004), and Ghemawat, Gobioff, and Leung, "The Google File System" (2003).** The restricted model and the storage layer it runs on.
- **Chang and colleagues, "Bigtable" (2006).** The sparse sorted map and the SSTable engine. Read the data-model section in the authors' own words.
- **Burrows, "The Chubby Lock Service" (2006).** The coordination service Bigtable depends on, and the fullest account of consensus as a product.
- **Corbett and colleagues, "Spanner" (2012).** The return of distributed SQL and ACID; read the TrueTime and concurrency-control sections together.
- **Brewer, "Spanner, TrueTime and the CAP Theorem" (2017).** The definitive short answer to "did Spanner beat CAP." It did not.
- **Chandra, Griesemer, and Redstone, "Paxos Made Live" (2007).** Building Chubby, and the evidence for how much real consensus the theory papers leave out.
- **Zaharia and colleagues, "Resilient Distributed Datasets" (Spark, 2012).** How the successor widened MapReduce's rigid two-step model.
- **DeCandia and colleagues, "Dynamo" (2007), and O'Neil and colleagues, "The Log-Structured Merge-Tree" (1996).** The other replication lineage that Cassandra fused with Bigtable, and the storage engine underneath all of it.

## Where the series goes next

Everything in this seminar tolerates crashes and trusts its participants. A Paxos group assumes its replicas are honest but sometimes down; Spanner assumes a TrueTime daemon that reports a wrong interval is broken, not lying; commit-wait assumes no one forges a timestamp. That trust is reasonable inside one company's datacenters and unreasonable the moment participants might be adversarial, compromised, or running someone else's code. Relaxing the assumption that failed means silent rather than malicious is the Byzantine problem, and it is where the series turns next, back to consensus but against components that may actively lie.

The recurring test of this book: would the authors recognize their ideas in the modern reading? Dean and Ghemawat would, and mostly have. They watched Spark supersede map-then-reduce, Bigtable's data model become an entire product category, and Spanner's architecture rebuilt by CockroachDB and its peers. The instincts that run through all three papers, restrict the model so the framework can help, and compose mature primitives rather than invent new theory, became the defaults of an industry. The vindication is that the arc no longer looks like Google's private history. It looks like the shape of how distributed data is built.
