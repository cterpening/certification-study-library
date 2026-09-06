# Vendor adapters

Adapters discover and normalize public objective pages without embedding vendor-specific HTML behavior in the guide format.

`scripts/objective_adapter_registry.py` is the canonical adapter inventory. Repository
validation requires every catalog assignment and every implementation to match that registry,
and requires this generated view to remain current.

<!-- BEGIN GENERATED ADAPTER INVENTORY -->
| Adapter | Vendor catalog entries | Public extraction contract |
| --- | --- | --- |
| `aws-exam-guide` | AWS | AWS exam identity, capability summary, weighted domains, and lifecycle signals. |
| `cisco-certification` | Cisco | Cisco exam topics, domain weights, version identifiers, and lifecycle signals. |
| `comptia-certification` | CompTIA | CompTIA exam code, lifecycle details, and weighted objective summary. |
| `cpp-institute-certification` | C++ Institute | C/C++ Institute syllabus sections, exam metadata, and lifecycle signals. |
| `databricks-certification` | Databricks | Databricks weighted coverage map, assessment details, and lifecycle signals. |
| `fortinet-certification` | Fortinet | Fortinet exam topics, product-version scope, delivery details, and lifecycle signals. |
| `google-cloud-certification` | Google Cloud | Google Cloud exam-guide sections, product scope, and lifecycle signals. |
| `hashicorp-developer` | HashiCorp | HashiCorp exam baselines, objective lists, product versions, and lifecycle signals. |
| `ibm-certification` | IBM | IBM certification API objectives, assessment metadata, and lifecycle signals. |
| `isaca-certification` | ISACA | ISACA content domains, weights, exam metadata, and lifecycle signals. |
| `isc2-certification` | ISC2 | ISC2 domains, weights, exam outline metadata, and lifecycle signals. |
| `js-institute-certification` | JS Institute | JS Institute syllabus sections, exam metadata, and lifecycle signals. |
| `linux-foundation-certification` | Linux Foundation | Linux Foundation and CNCF domains, competencies, format, versions, and lifecycle signals. |
| `microsoft-learn` | GitHub, Microsoft | Microsoft Learn skills versions, weighted objective sections, and announced changes. |
| `microsoft-office-specialist` | Microsoft Office Specialist | Microsoft Office Specialist objective groups, exam metadata, and lifecycle signals. |
| `mongodb-certification` | MongoDB | MongoDB public exam contracts and objective lines exposed without authentication. |
| `nvidia-certification` | NVIDIA | NVIDIA exam topics, weights, certification metadata, and lifecycle signals. |
| `oracle-learning-path` | Oracle | Oracle learning-path objectives, exam references, product scope, and lifecycle signals. |
| `palo-alto-networks-certification` | Palo Alto Networks | Palo Alto Networks blueprint domains, weights, versions, and lifecycle signals. |
| `python-institute-certification` | Python Institute | Python Institute syllabus sections, exam metadata, and lifecycle signals. |
| `red-hat-exam` | Red Hat | Red Hat performance tasks, tested product versions, and lifecycle signals. |
| `salesforce-certification` | Salesforce | Salesforce exam-guide topics, weights, credential metadata, and lifecycle signals. |
| `servicenow-certification` | ServiceNow | ServiceNow blueprint scope, weights, delivery details, and lifecycle signals. |
| `snowflake-certification` | Snowflake | Snowflake exam-guide domains, weights, exam metadata, and lifecycle signals. |
| `splunk-certification` | Splunk | Splunk blueprint topics, exam metadata, product versions, and lifecycle signals. |
<!-- END GENERATED ADAPTER INVENTORY -->

Each implementation produces normalized objective text plus a status record containing
baseline labels and future announcements. Keep retrieval, comparison, snapshots, reports,
and review workflow common; keep page markers and extraction rules provider-specific.

An adapter may retrieve public metadata and objective text. It must not access authenticated training, assessments, subscriptions, or private material.
