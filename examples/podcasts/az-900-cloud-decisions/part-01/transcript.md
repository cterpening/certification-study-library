# AZ-900 study conversation — Part 1

> Independent AI-assisted resource — AI-GENERATED DRAFT; HUMAN REVIEW PENDING.

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) is authoritative.

Series scope: Two decisions in Azure fundamentals: keeping reservations available during a location failure and choosing who maintains a ticketing application. These cases cover selected public objectives.

Baseline: Skills measured as of July 20, 2026. Recorded blueprint check: 2026-10-28.

This is a production script, not an assertion that audio has been generated or listened to.

[Companion study guide, practice questions and visual aids](<../../../study-packs/az-900-cloud-decisions/study-guide.md>)

[Full source study guide](<../../../../guides/AZ-900-microsoft-azure-fundamentals.md>)

## Introduction

**Host:** Welcome to part 1 of 2 of our AZ-900 study conversation. Can the booking desk stay open when a zone goes down? Both voices are synthetic. This independent, AI-assisted material is awaiting human review. The show notes link to the official exam blueprint and list the dates used for this episode.

**Learner:** We will work through the ideas, compare common choices, and pause for recall. The linked guide and show notes contain the sources and visual aids.

## Can the booking desk stay open when a zone goes down?

**Host:** It's Saturday morning at a bicycle rental shop. A customer has picked a blue bike for eleven. She presses Reserve. The team has deployed two copies of its booking app in Azure. Then the power goes out in one availability zone. Before we say whether she gets the bike, what would you ask the team?

**Learner:** Where did you put the two copies? I used to hear “two servers” and assume the second one was a spare. If they share the part that just failed, I could lose both.

**Host:** Exactly. A datacenter is a facility that houses equipment. In an Azure region that offers zones, each availability zone is a group of one or more datacenters with its own power, cooling and networking. Both app servers in our example are in the same zone. What did the second server buy the shop?

**Learner:** More room for bookings on a busy morning. It could also keep serving if only one server failed and traffic reached the other. The zone outage is a different problem. Both servers are inside it.

**Host:** Let's move one server to another zone and assume customers can reach the healthy copy. Now the home page opens. The customer presses Reserve again, and the page hangs. The only database that can accept a booking was in the first zone. What would count as evidence that the shop is back?

**Learner:** I'd make a test reservation and look it up again. Seeing a bicycle on the screen proves the catalog loaded. Seeing my reservation saved proves the app could reach the database and finish the job.

**Host:** Follow the arrows in the companion diagram aloud. A customer submits a request. It reaches an app with capacity. The app saves the booking in the database. Then the customer gets confirmation. For each arrow, ask what happens when that zone disappears. A zonal resource is placed in one zone. For a zone-redundant resource, the service distributes or replicates it across zones. Check what your particular service supports and how you deployed it.

**Learner:** Here's a numbers check. We now have a database that can handle a zone failure. Each of the two app servers can take sixty bookings a minute. Eighty customers a minute arrive. One zone goes down. Pause here and work out how many bookings a minute the remaining app can handle, and how far that is from demand.

**Host:** Sixty fit. Demand exceeds that by twenty bookings every minute. Separate locations helped keep the app reachable. Serving everyone also takes enough capacity in the surviving location. Test the design under the load that will actually arrive.

**Learner:** Now change the promise on the shop door. Bookings must continue even if the whole Azure region goes offline. Would a third zone in that same region meet the new promise? Take a moment to explain where a working copy would have to live.

**Host:** All those zones are still inside that region. A recovery location outside it needs an app that works, usable booking data and a way for customers to reach them. Azure pairs some regions, and some services use those pairs. A region appearing beside another on a map tells us nothing about whether this shop has configured its booking database to copy records there. Check the chosen services and rehearse the complete reservation.

**Learner:** I can explain the difference to the shop owner now. Adding capacity helps with a busy day. Distributing the work helps with a failed location. I can tell whether either choice worked by trying to reserve a bike.

## Next steps

**Learner:** Before moving on, explain the distinctions from this episode without looking at your notes. Use the original practice questions in the study pack to find gaps.

**Host:** Then check the current official sources and complete the relevant hands-on work. This conversation covers selected objectives; listening alone is not evidence of readiness or complete exam coverage.

## Show notes

These registered sources are pinned through the study package's input fingerprints.

- **Can the booking desk stay open when a zone goes down?** — [List of Azure regions](https://learn.microsoft.com/en-us/azure/reliability/regions-list), [Azure paired and nonpaired regions](https://learn.microsoft.com/en-us/azure/reliability/regions-paired), [Azure reliability documentation](https://learn.microsoft.com/en-us/azure/reliability/). Guide sections: Regions, availability zones, and datacenters; Design from geography to resource; Separate the cloud benefits.
