# EX294 deep review — September 28, 2026

Same-context AI review; independent human review pending. [Study guide](../../guides/EX294-red-hat-certified-advanced-system-administrator-ansible.md).

## Scope and version evidence

Read all 56 current [public tasks](https://www.redhat.com/en/services/training/ex294-red-hat-certified-engineer-rhce-exam-red-hat-enterprise-linux), grouped 8/12/4/3/3/2/3/5/4/10/2. Eleven official groups map to eight teaching sections; Git and VS Code are retained explicitly. The objective and lifecycle monitor hashes are unchanged. The EX294V26K section of the [public version PDF](https://training-lms.redhat.com/public_content/redhat/training/Red%20Hat%20Certification%20Exam%20Objectives%20by%20Version.pdf) has identical ordered text after normalization. Same-day PDF bytes were reused from EX280 research; EX294 sections were separately read and compared. Accepted monitor snapshots were not replaced.

[AU294](https://www.redhat.com/en/services/training/au294-red-hat-linux-automation-with-ansible) explicitly names RHEL 10, core 2.16 and AAP 2.6. Remove the broader 2.5/2.6 course claim; AU094 remains an AAP 2.5 introduction. The [AAP lifecycle policy](https://access.redhat.com/support/policy/updates/ansible-automation-platform) distinguishes the default core from optional EE streams and product support from community maintenance. The guide does not assert that AAP 2.6 is the newest product release or that a course baseline assigns a candidate's exam version.

## Teaching repairs

Added a complete original inventory, playbook, Jinja template and Python candidate validator. Input assertions reject quoted booleans, invalid ports and malformed backend lists; candidate validation rejects invalid structure or values. A quoted false value would render true if assertions were bypassed, demonstrating why syntactic validity alone cannot prove intended behavior. Candidate validation follows the [template module contract](https://docs.ansible.com/projects/ansible-core/2.16/collections/ansible/builtin/template_module.html); actual target replacement was not executed.

Added configuration-file selection/inspection, an OR-versus-AND failure matrix, reporting versus side effects, rescue versus rollback, unreachable-host limits, handler suppression/flush behavior and check/diff/Vault output boundaries. These are grounded in versioned core 2.16 references linked at the relevant guide sections. Added answers to every one of the 40 knowledge checks and retained fresh-host/reboot validation as required practice.

## Blog and learning catalog

John Wadleigh's April 9, 2019 [deployment lessons](https://www.redhat.com/en/blog/adventures-ansible-lessons-learned-real-world-deployments) supports repeatable state and readable reusable roles. Its once-per-playbook handler claim is not adopted: the [handler reference](https://docs.ansible.com/projects/ansible-core/2.16/playbook_guide/playbooks_handlers.html) permits later notifications after a flush. Treat the blog as historical context, not current tool/API or dependency-version policy.

Both Udemy pages and the OReilly book page blocked automated access; previously observed runtimes, dates and counts are clearly unverified. Official public training pages were reread. Places to learn is the final guide section.

## Validation and limits

Executed 41 local checks using Jinja 3.1.6, PyYAML 6.0.3 and the original Python validator. Checks cover both host outputs, stable rerendering/permutations, precise port changes, invalid/missing input, strict undefined handling, output validation including duplicate/default/extra fields, and the four failure-expression outcomes. Validation leaves candidate bytes unchanged and produces no output. Two YAML blocks were parsed, one Jinja template rendered and one Python block executed.

These checks do not execute Ansible tasks or prove module validation hooks, inventory precedence, handler execution or idempotence on managed nodes. No ansible-playbook, navigator, EE, SSH, Vault, RHEL service/storage/security or fresh-host/reboot lab ran. All eight platform labs remain proposed; the earlier WSL startup blocker remains deferred. Repository validation, 175 unit tests, strict site build, generated-site validation, catalog consistency and diff checks are recorded in the operational receipt after execution.
