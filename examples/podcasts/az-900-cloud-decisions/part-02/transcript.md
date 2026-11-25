# AZ-900 study conversation — Part 2

> Independent AI-assisted resource — AI-GENERATED DRAFT; HUMAN REVIEW PENDING.

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) is authoritative.

Series scope: Two decisions in Azure fundamentals: keeping reservations available during a location failure and choosing who maintains a ticketing application. These cases cover selected public objectives.

Baseline: Skills measured as of July 20, 2026. Recorded blueprint check: 2026-10-28.

This is a production script, not an assertion that audio has been generated or listened to.

[Companion study guide, practice questions and visual aids](<../../../study-packs/az-900-cloud-decisions/study-guide.md>)

[Full source study guide](<../../../../guides/AZ-900-microsoft-azure-fundamentals.md>)

## Introduction

**Host:** Welcome to part 2 of 2 of our AZ-900 study conversation. Who patches the ticket counter? Both voices are synthetic. This independent, AI-assisted material is awaiting human review. The show notes link to the official exam blueprint and list the dates used for this episode.

**Learner:** We will work through the ideas, compare common choices, and pause for recall. The linked guide and show notes contain the sources and visual aids.

## Who patches the ticket counter?

**Host:** The lights go down at seven. At six, the theater's ticket counter is printing seat assignments. The manager tells you, “We're moving ticketing to the cloud, so take patching off the calendar.” Before you erase that appointment, what is the theater actually buying?

**Learner:** I need the order form. Are they buying a ticketing application, a place to run their own application, or a machine to maintain? All three might put tickets on the printer.

**Host:** First order form. A provider offers a finished booking application. Staff sign in, enter the seat map, set prices and sell tickets. The theater only needs the features on offer. Which service model does that describe?

**Learner:** Software as a service. The provider operates the finished application. The theater still decides which employees can issue refunds and who should see customer details. When the treasurer leaves, someone at the theater needs to remove that access.

**Host:** Second order form. The theater writes a special seating rule that the finished app can't implement. The development team has a web application that runs on a supported Azure App Service runtime. They need to deploy the code. The application has no requirement to administer the operating system. Who takes which job?

**Learner:** I'd consider platform as a service. With App Service hosting our code, Microsoft maintains the underlying operating system. Our developers still maintain the app and the libraries they ship. Our team is also responsible for the data, who can reach it and the settings we choose.

**Host:** Here's something the manager can check on a Monday. A library the developers bundled with their ticketing app needs updating. Pause and say whose name belongs on that work item. Then decide who maintains the operating system underneath the managed web platform.

**Learner:** The team's name goes on the library. A platform update can't repair a bug in the theater's custom seating code either. Microsoft maintains the underlying operating system. There are still two jobs on the calendar, and different people own them.

**Host:** Change one detail. The ticket vendor now requires a special driver installed in the guest operating system on the same machine as the booking application. The vendor supports that arrangement on a suitable Azure virtual machine. Pause and choose a hosting model. What new work comes back to the theater?

**Learner:** Infrastructure as a service is a candidate. An Azure virtual machine gives the theater control inside the guest operating system, so its administrators can install the supported driver. They now own guest maintenance, including arranging patches and testing that ticketing still works after an update. Microsoft still maintains the physical host.

**Host:** Picture the three rows of the companion diagram. The first starts with a finished tool and ends with configuring how the theater uses it. The second starts with custom code and ends with deploying it to a managed platform. The third starts with that operating-system driver and ends with a virtual machine the theater administers. In each row, point to the requirement that made you choose it.

**Learner:** Here's how I'd answer the manager. If we buy the finished service, keep staff access and customer records on our calendar. If we run our code on App Service, add our code and its dependencies. If we need that driver in our own virtual machine, add the guest operating system too. Now the maintenance schedule can say who actually does each job.

## Next steps

**Learner:** Before moving on, explain the distinctions from this episode without looking at your notes. Use the original practice questions in the study pack to find gaps.

**Host:** Then check the current official sources and complete the relevant hands-on work. This conversation covers selected objectives; listening alone is not evidence of readiness or complete exam coverage.

## Show notes

These registered sources are pinned through the study package's input fingerprints.

- **Who patches the ticket counter?** — [Shared responsibility in the cloud](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility), [Choose an Azure compute service](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree), [Azure Virtual Machines overview](https://learn.microsoft.com/en-us/azure/virtual-machines/overview). Guide sections: Shared responsibility; IaaS, PaaS, SaaS, and serverless; Turn a cloud requirement into a responsibility decision; Select compute by control, orchestration, and workload shape.
