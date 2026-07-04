# 7. Discussion and further reading

## The argument in one breath

Codd looked at databases where a program answered a question by walking pointers along access paths the storage designer had built, and saw that the query and the route had become the same thing, so that no storage could change without breaking programs. His fix was a hard line between the logical model and the physical store, which he called data independence. Above the line he put the mathematical relation, a set of tuples with no duplicates, no order, and named rather than numbered columns, defined so cleanly that it carries no storage assumptions at all; the table is only a picture of it. To ask questions without naming a route, he sketched a declarative language grounded in predicate logic: describe the data you want, and the system finds it. The paper goes as far as first normal form and a sketch of an algebra, and openly leaves the rest, the later normal forms, the calculus, the completeness theorem, to work that came after. And the promise that a declarative query could be fast waited nine years for the cost-based optimizer to keep it.

Read in the series, this is information hiding applied to data, the logical schema a stable interface over storage that changes underneath, which is the same move the modularity seminars make for code.

## Questions worth arguing about

These are seminar questions. Several have no settled answer.

1. **Is SQL relational enough?** Codd thought not, and published twelve rules to say so. SQL permits duplicate rows, nulls, and ordering the model forbids. Does that gap cause real harm in your work, or is it a purist's complaint about a language that clearly won? Where has a SQL-is-not-a-set assumption actually bitten you?

2. **What did NoSQL relearn?** The 2000s threw out the relational model for scale and, in effect, went back to navigating: denormalized data, relationships managed in the application, storage shaped to query paths. Which of those were sound trades and which were rediscoveries of why Codd left? What did you give up, and did you get it back with NewSQL?

3. **Nulls.** The model of 1970 had atomic domain values and no null. SQL added it and inherited three-valued logic. Was representing "missing" as a special value the right call, or should missing information have been modeled some other way? What would your schemas look like without nulls?

4. **The optimizer as a leaky abstraction.** Data independence says you never think about access paths. Every experienced database engineer does, reading query plans and coaxing the optimizer. Is that a failure of the abstraction, or the normal price of one, and where is the line between trusting the planner and fighting it?

5. **Declarative everywhere.** "Say what, not how" now runs build systems, infrastructure-as-code, and configuration reconcilers. Where does the declarative bargain pay off, and where does hiding the how cost you more than it saves, when the planner gets it wrong and you cannot easily override it?

6. **Data independence versus schema change.** Storage changes are hidden; schema changes are not. In fast-moving systems the schema itself changes constantly. Has the hard part of the job migrated from physical tuning to schema evolution, and does the relational model help or hinder there?

## Further reading

Start with the paper, then follow the model as it was formalized in stages.

- **E. F. Codd, "A Relational Model of Data for Large Shared Data Banks" (CACM 1970).** The source. Read section 1 for data independence and the model, section 2 for the algebra sketch and the connection trap; keep in mind it stops at first normal form.

- **Codd, "Further Normalization of the Data Base Relational Model" (1971 to 1972).** Where second and third normal form appear. The normalization doctrine the 1970 paper deferred.

- **Codd, "Relational Completeness of Data Base Sublanguages" (1972).** The relational calculus and the completeness yardstick, a query language is relationally complete if it can express what the calculus can. Not in the 1970 paper.

- **Bachman, "The Programmer as Navigator" (Turing Lecture, CACM 1973).** The other side. Read it to understand what Codd was arguing against, and why intelligent people defended the navigational model.

- **Chamberlin and Boyce, "SEQUEL: A Structured English Query Language" (SIGFIDET 1974).** The origin of SQL, explicitly designed around how people use tables. Read it against chapter 2 to see where the language and the model part ways.

- **Selinger et al., "Access Path Selection in a Relational Database Management System" (SIGMOD 1979).** The System R cost-based optimizer, the component that made data independence pay off. The technical heart of chapter 5.

- **Codd, "Is Your DBMS Really Relational?" (Computerworld, 1985).** The twelve rules, and Codd's public argument that the products calling themselves relational were not. Short and pointed.

## Where the series goes next

Codd turns the series toward how we structure what systems know, and the thread runs straight into software structure.

- The principle under data independence, hide what is likely to change behind a stable interface, is **David Parnas's** information hiding, a later seminar here. Codd made the argument for data; Parnas makes it the general criterion for splitting a system into modules. Read them together and the relational schema is a module interface with an unusually long life.
- The consistency and constraint machinery Codd sketched in section 2, and his passing note about keeping "a journal of all state-changing transactions," is **Gray's** transaction concept, the previous seminar. The relational model says what a consistent state is; transactions keep the database in one.
- And the modern reunion of the relational model with distribution, NewSQL on top of consensus, ties this seminar back to **Liskov's** replication and forward to **Lamport's** Paxos: declarative relational queries, served from a fault-tolerant replicated store.

Read this way, Codd's paper is the moment data got its own version of the idea the rest of the series keeps finding: draw a line, put the volatile thing behind it, and let the two sides change without breaking each other.
