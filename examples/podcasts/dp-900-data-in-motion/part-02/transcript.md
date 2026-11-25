# DP-900 study conversation — Part 2

> Independent AI-assisted resource — AI-GENERATED DRAFT; HUMAN REVIEW PENDING.

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900) is authoritative.

Series scope: Two county fair stories explore selected Azure Data Fundamentals objectives. Count arrivals across a delayed stream, then reconcile ticket sales across two relational tables.

Baseline: Skills measured as of July 21, 2026. Recorded blueprint check: 2026-10-28.

This is a production script, not an assertion that audio has been generated or listened to.

[Companion study guide, practice questions and visual aids](<../../../study-packs/dp-900-data-in-motion/study-guide.md>)

[Full source study guide](<../../../../guides/DP-900-microsoft-azure-data-fundamentals.md>)

## Introduction

**Host:** Welcome to part 2 of 2 of our DP-900 study conversation. Two paid orders, three tickets, and an extra twenty dollars. Both voices are synthetic. This independent, AI-assisted material is awaiting human review. The show notes link to the official exam blueprint and list the dates used for this episode.

**Learner:** We will work through the ideas, compare common choices, and pause for recall. The linked guide and show notes contain the sources and visual aids.

## Two paid orders, three tickets, and an extra twenty dollars

**Learner:** I have a box office mystery. The fair has two paid orders, twenty dollars each. The sales report says we took sixty dollars. I was going to look for a third card payment. The clerk says to look at the tickets first. How could counting tickets create money?

**Host:** Let's retrace the report. There are two tables. The orders table has one row per paid order. On paper you could write two slips, both for twenty dollars. Call the first order Blue and the second order Gold. Every slip has its own order identifier. That identifier is the primary key.

**Learner:** And the tickets table has one row per issued ticket. Blue bought two tickets. Gold bought one. Each ticket needs its own identifier, and it also carries the order identifier. The column that points back to the order is a foreign key.

**Host:** Exactly. With Structured Query Language, often called SQL, you can select rows from those tables and join them where the order identifiers match. An inner join gives you one row for each matching pair. Say the pairs aloud with me. Blue and its first ticket. Blue and its second ticket. Gold and its only ticket. What amount does each joined row carry?

**Learner:** Twenty, twenty, twenty. There’s my sixty dollars! The same Blue payment appeared on two rows because two tickets matched the order. Nobody charged the card again. A row in the joined result now describes an order paired with a ticket.

**Host:** Here’s a tempting fix. Someone says, add each different dollar amount just once. Pause and work out what that would pay into the till.

**Learner:** Only twenty dollars. Blue and Gold paid the same price, but both orders count. I need to tell orders apart by their identifiers. To report money alone, I can sum the two paid order rows directly. That gives forty dollars.

**Host:** The clerk wants tickets and dollars next to each other on each order. First use a group by clause on the tickets’ order identifier and count the rows in each group. Picture a note for Blue saying two tickets and a note for Gold saying one ticket. How many times will Blue's payment appear when you attach those notes to the orders?

**Learner:** Once. Each note belongs to one order, and each order can match at most one note. Now I can report three issued tickets and forty dollars. I’ll check that the report still contains just two order rows before I add the money.

**Host:** Change one fact. Gold has paid, but its ticket hasn’t been issued yet. Blue still has two tickets. Pause here. The clerk wants all paid orders, including paid orders waiting for tickets. Which side of the join must keep its rows? What totals should the clerk expect?

**Learner:** Keep the paid orders on the left and use a left join to the grouped ticket counts. Gold has no matching ticket group yet, but it still has a payment. Here a missing count means zero tickets issued. I expect two paid orders, forty dollars in payments, and two issued tickets. An inner join at this point would hide Gold’s payment.

**Host:** That gives the clerk a way to check any new version of this report. Point to one row and finish the sentence: this row stands for one what? If the answer changes between steps, check again before adding money.

## Next steps

**Learner:** Before moving on, explain the distinctions from this episode without looking at your notes. Use the original practice questions in the study pack to find gaps.

**Host:** Then check the current official sources and complete the relevant hands-on work. This conversation covers selected objectives; listening alone is not evidence of readiness or complete exam coverage.

## Show notes

These registered sources are pinned through the study package's input fingerprints.

- **Two paid orders, three tickets, and an extra twenty dollars** — [Primary and foreign key constraints](https://learn.microsoft.com/en-us/sql/relational-databases/tables/primary-and-foreign-key-constraints?view=sql-server-ver17), [SQL GROUP BY](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-group-by-transact-sql?view=sql-server-ver17), [Explore fundamental relational data concepts](https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/). Guide sections: Tables, keys, and relationships; SQL and database objects; 1. Customer identity and the grain of revenue; 2. Run the SQL example and undo an accidental change.
