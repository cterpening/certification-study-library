# DP-900 study conversation — Part 1

> Independent AI-assisted resource — AI-GENERATED DRAFT; HUMAN REVIEW PENDING.

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900) is authoritative.

Series scope: Two county fair stories explore selected Azure Data Fundamentals objectives. Count arrivals across a delayed stream, then reconcile ticket sales across two relational tables.

Baseline: Skills measured as of July 21, 2026. Recorded blueprint check: 2026-10-28.

This is a production script, not an assertion that audio has been generated or listened to.

[Companion study guide, practice questions and visual aids](<../../../study-packs/dp-900-data-in-motion/study-guide.md>)

[Full source study guide](<../../../../guides/DP-900-microsoft-azure-data-fundamentals.md>)

## Introduction

**Host:** Welcome to part 1 of 2 of our DP-900 study conversation. How many people came through the gate? Both voices are synthetic. This independent, AI-assisted material is awaiting human review. The show notes link to the official exam blueprint and list the dates used for this episode.

**Learner:** We will work through the ideas, compare common choices, and pause for recall. The linked guide and show notes contain the sources and visual aids.

## How many people came through the gate?

**Host:** The first band is about to play at the county fair. The supervisor calls from the south gate. She wants to know whether to open another entrance. Meanwhile, the treasurer wants yesterday’s attendance figure for a meeting tomorrow. The same scanners can help both people. Which of them needs an answer while people are still walking through the gate?

**Learner:** The supervisor. A count that arrives tomorrow gives her no chance to move today’s queue. I’d feed incoming admissions into a running calculation. For the treasurer, I could collect yesterday’s records as a set, check them, and issue a daily total.

**Host:** That gives us stream processing and batch processing. The stream keeps taking new events. A batch has a boundary, such as all records selected for one day. You can keep the original events and use both approaches. Now let’s listen to exactly one five-minute interval. It starts at eleven fifty-five and ends just before noon.

**Learner:** I’ll run the counter. The first admission, Robin, reaches me on time. The second, Wren, also reaches me on time. The scanner didn’t hear the acknowledgment for Wren, so it sends that message again with the same event identifier. Those bird names stand for individual scans in our example.

**Host:** It’s noon. Pause here and say two numbers aloud. How many messages reached you? How many distinct admissions do you know about?

**Learner:** Three messages. Two admissions. Robin counts once and Wren counts once. If I counted deliveries, the retry would look like another person. I’d keep the scan identifier with the record so I can recognize the repeat.

**Host:** A third scanner was briefly offline. At one minute past noon it delivers Lark, a new scan. Lark happened one minute before noon. For this report, we group by the time people crossed the gate, and our procedure accepts this delay. Which interval gets the extra admission?

**Learner:** The earlier interval. Lark’s event time is eleven fifty-nine. Its arrival time is twelve oh one. At noon I could tell the supervisor we had seen two distinct admissions. Once Lark arrives, I can revise that figure to three and preserve when I made the correction.

**Host:** Change one detail. The technician wants to measure the load on the receiver and counts every incoming message in the minute it arrives. Pause and explain where Lark goes now, and whether Wren’s retry matters.

**Learner:** Lark goes into the minute starting at twelve oh one. And yes, Wren’s retry matters to the receiver because it had to handle the message again. I'd label one chart admissions by scan time and the other messages by arrival time. Two different answers can both be right when readers know what the counter measures.

**Host:** One last call from the gate. A ticket holder leaves and is later admitted again. Staff give the second admission a fresh scan identifier. Our measure is admissions, including reentry. Would keeping only one record per ticket work?

**Learner:** That would erase a genuine admission. Keep one record per admission event. If the treasurer asks for unique ticket holders instead, that is a different calculation. Before I publish either figure I want a sentence that says what counts once, which clock sets the interval, and how we handle a delayed record.

## Next steps

**Learner:** Before moving on, explain the distinctions from this episode without looking at your notes. Use the original practice questions in the study pack to find gaps.

**Host:** Then check the current official sources and complete the relevant hands-on work. This conversation covers selected objectives; listening alone is not evidence of readiness or complete exam coverage.

## Show notes

These registered sources are pinned through the study package's input fingerprints.

- **How many people came through the gate?** — [Explore fundamentals of real-time analytics](https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/), [Structured Streaming](https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/). Guide sections: Batch and streaming; 4. Duplicate and late stream events; Lab 6: Replay without double counting.
