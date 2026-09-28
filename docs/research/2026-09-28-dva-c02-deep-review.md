# DVA-C02 deep review — September 28, 2026

The complete guide, all **101 detailed skills**, technologies, in-scope services and version 2.1 revisions were reviewed. Broad scored domains match the accepted baseline. Emerging AI topics remain possible unscored pretest content. The live credential page still gives December 1 as the last C02 date while the September announcement says November 30; C03 registration/objectives are announced for October 27. No additional retirement notice was found.

## Learner changes

- Repair the order scenario with an atomic state/outbox write, durable relay and idempotent consumers. Add failures between commit/publication and publication/acknowledgement to the proposed lab.
- Separate standard SQS, FIFO and Kinesis partial-batch behavior. Explain per-entry publication errors despite HTTP 200 and the difference between timeout recommendations and validation.
- Add 40 answer explanations and four original worked decisions covering replay, acknowledgement, compute usage and retry multiplication.
- Flag X-Ray SDK/daemon maintenance and link the OpenTelemetry migration overview. Current HTML gives no maintenance end date; no X-Ray service retirement is inferred.
- Qualify paid-provider claims and keep Places to learn last.

## Article assessment

The [Powertools TypeScript article](https://aws.amazon.com/blogs/compute/implementing-idempotent-aws-lambda-functions-with-powertools-for-aws-lambda-typescript/) is useful for stable keys and persistence states. Its older examples were read, not executed; remote side effects still need an idempotency/reconciliation contract.

The [September 9 Lambda Managed Instances article](https://aws.amazon.com/blogs/compute/announcing-90-minute-function-timeout-on-aws-lambda-managed-instances/) adds useful execution-mode context. Its contradictory synchronous timeout wording and broad stream-retry statement were not adopted. Current limit documentation and the specific Kinesis/SQS retry pages support the guide's narrower explanation. The outbox source's sample acknowledgement handling also needs per-entry API checks; vendor examples are not copied as production-ready code.

## Validation and limits

Ten local assertions checked arithmetic and expected retry sets. Eight AWS labs remain proposed; no cloud resources, paid lessons or current Powertools package were executed. Independent human review remains pending. The [operational receipt](https://github.com/cterpening/certification-study-library/blob/main/ADLC_Docs/operations/2026-09-28-dva-c02-deep-review.json) records dated fetches, hashed objectives, section mapping, source limitations and completed repository/site gates. Accepted objective snapshots were preserved.
