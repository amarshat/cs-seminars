# Reading Edgar F. Codd

## *A Relational Model of Data for Large Shared Data Banks*

> E. F. Codd, "A Relational Model of Data for Large Shared Data Banks," Communications of the ACM, Volume 13, Number 6, June 1970, pages 377 to 387. IBM Research Laboratory, San Jose.

This is the paper under your database, and it is almost never read for what it actually argues. The folklore version is "Codd invented tables." The real paper barely mentions tables, calls the table a mere "array representation" that "is not an essential part of the relational view," and spends its energy on something harder and more durable: freeing programs from the way data is stored.

Codd's target in 1970 was the reigning database technology, the navigational systems. In a hierarchical database like IMS or a network database like IDS, the data was a maze of records wired together by pointers, and a program answered a question by walking the pointers, hop by hop, along access paths the storage designer had laid down. Charles Bachman, who won the Turing Award for this design and called it "the programmer as navigator," saw the maze as the point. Codd saw it as the prison. Change how the data was laid out, add an index, reorganize a tree, and every program that had memorized the old paths broke. His paper is an argument that the logical shape of data, what relates to what, should be stated once, mathematically, and kept completely separate from how the machine happens to store it. He called that separation data independence, and it is the whole point.

The tool he reached for was the mathematical relation: a set of tuples drawn from named domains, with no duplicate rows, no meaningful row order, and columns you name rather than count. On top of it he sketched a language in which you describe the data you want by its properties, not the route to reach it, "the information, like Everest, is there." That declarative move, say what, not how, is the idea that had to wait a decade for the query optimizer to make it fast, and it is the idea that still separates SQL from the pointer-chasing it replaced.

## Why this seminar, seventh

The series now turns from keeping systems alive to organizing what they know. But the through-line holds. Codd's data independence is information hiding applied to data: put the thing most likely to change, the physical storage, behind a stable interface, the logical schema, so the two can evolve separately. That is the same instinct the Parnas seminar later makes into a general rule for software modules. And "say what, not how" is the declarative idea that runs from this paper through every query planner, build system, and configuration language that decides the how for you. Read Codd here and the later seminars on modularity read as the same argument in a different domain.

## The four questions

1. **What problem was Codd solving?** Programs were welded to storage. In navigational databases, application logic encoded the access paths through the data, so any change to the physical layout broke the programs. Codd wanted the logical model and the physical storage to be independent.
2. **Why was the answer surprising?** Because it threw out the pointers. Instead of navigating a structure, you would describe the data you wanted with logic and let the system find it. Practitioners doubted a machine could ever do that efficiently, which is exactly what the debate of 1974 was about.
3. **What survived?** The model itself, almost entirely: relations, keys, normalization, and above all data independence. What got compromised is the language. SQL, the commercial vehicle, permits the duplicates, nulls, and ordering the model forbids, and Codd spent later years objecting that the products calling themselves relational were not.
4. **How should a working engineer read it today?** As the origin of the declarative query and of the separation between logical schema and physical plan that the optimizer exploits every time you run a `SELECT`. And as a caution that the model and SQL are not the same thing.

## Chapters

1. [Programs chained to storage](01-programs-chained-to-storage.md). The navigational databases, the pointers, and data independence as the real argument.
2. [A relation is not a table](02-a-relation-is-not-a-table.md). The mathematical model, what it forbids, and why SQL is a commercial approximation Codd disowned.
3. [Say what, not how](03-say-what-not-how.md). The declarative sublanguage, symmetric exploitation, and naming data by content instead of by path.
4. [What 1970 settled](04-what-1970-settled.md). The honest scope: first normal form and an algebra sketch here, the later normal forms and the calculus elsewhere.
5. [The optimizer makes it real](05-the-optimizer-makes-it-real.md). System R and cost-based optimization, the component that turns a declarative query into a physical plan.
6. [What survived, and information hiding](06-what-survived-and-information-hiding.md). The model's endurance, SQL's divergence, and the bridge to modularity.
7. [Discussion and further reading](07-discussion-and-reading.md). Questions to argue about, and where the series goes next.

## A note on the source

Quotations come from the 1970 CACM paper. This seminar is deliberate about three things the folklore gets wrong. The relational model is not tables and not SQL; a relation is a set of tuples grounded in predicate logic, and SQL permits things the model forbids, which Codd said loudly in his 1985 "12 rules." Second and third normal form, Boyce-Codd normal form, and the formal relational calculus are later work (Codd 1971 to 1972, and Boyce in 1974), not this paper, which goes only as far as first normal form and says so. And the point of the paper is data independence, a reaction against the navigational databases of its day, best framed by the 1974 Codd-versus-Bachman debate. Where the paper is famous for something it did not say, this seminar says what it said.
