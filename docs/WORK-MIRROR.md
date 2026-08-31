# Updating the work mirror

The personal public repository is the canonical project. The work repository is an optional downstream copy and does not require GitHub Actions.

```text
Personal public repository and GitHub Pages
                    ↓
          Work repository mirror
```

## Website behavior in the work mirror

Mirroring the repository copies the website source, build scripts, and `.github/workflows/deploy-pages.yml`, but it does **not** copy or enable GitHub Pages repository settings, environments, permissions, runners, organization policies, domains, or access controls. The default work mirror is therefore a Markdown/content repository, not a second deployed website.

The public Pages workflow and MkDocs `site_url` target the personal GitHub.com repository. Do not assume that workflow is portable to GitHub Enterprise Server, another GitHub organization, or a host without Actions or Pages. Action versions, runner availability, allowed-action policy, Pages support, URL structure, authentication, and publication visibility may all differ.

If the work host does not provide GitHub Actions or GitHub Pages:

- use the Markdown directly in the repository;
- continue using the public website for the public portion of the material when employer policy permits;
- optionally run the MkDocs preview locally for private review; and
- publish a generated `site/` directory only through an employer-approved internal hosting process.

The mirrored public deployment workflow should remain disabled when it cannot or should not publish. Prefer an organization/repository workflow setting or a private overlay/import rule that omits the workflow; do not edit the canonical public workflow merely to satisfy an internal host. If an internal site is added later, keep its workflow, compatible action versions, internal `site_url`, access model, branding, and publication controls in the private overlay.

Never place an internal hostname, organization name, runner label, credential, or proprietary deployment instruction in the public repository. Document those values only in the private work overlay.

## Boundaries

- Keep the personal repository authoritative.
- Do not place customer, employer, internal, or proprietary material in the public repository.
- Do not copy work-only subscriptions, transcripts, training, or credentials into the public project.
- Treat the work copy as read-only unless a separate internal overlay is deliberately created.
- Keep work-specific formatting, navigation, branding, and presentation logic in the private overlay; the public Markdown remains independent.
- Confirm employer policy before creating or updating the work repository.
- Do not grant the personal account work access merely to simplify synchronization.

## Certification inventory for imports

`config/exams.json` is the canonical exam registry and should be used when an
import needs all structured metadata. [`CERTIFICATIONS.txt`](../CERTIFICATIONS.txt)
is a generated, tab-separated seed file intended for a downstream Python script
that queries or enriches certification information. Its header is
`vendor_id`, `exam_code`, and `title`. Those stable identity fields make a useful
search key without presenting public-library review state, guide paths, or URLs
as input facts the enrichment process must preserve.

Do not edit the text export directly. After adding or changing an exam in
`config/exams.json`, regenerate it and run validation:

```bash
python scripts/generate_certification_list.py
python scripts/validate_repository.py
```

Validation fails if the seed file is missing or no longer matches the canonical
catalog. A private overlay can read it with `csv.DictReader(..., delimiter="\t")`
and write discovered or internal metadata elsewhere without changing the public
input list.

## Account separation with SSH

Use different SSH keys and host aliases in `%USERPROFILE%\.ssh\config` on Windows:

```sshconfig
Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
    IdentitiesOnly yes

Host github-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_work
    IdentitiesOnly yes
```

## Recommended work checkout

Clone the work repository using the work identity:

```bash
git clone git@github-work:WORK-ORG/certification-study-library.git
cd certification-study-library
```

Register the public personal repository as read-only upstream:

```bash
git remote add upstream https://github.com/PERSONAL-NAME/certification-study-library.git
git remote -v
```

Expected roles:

```text
origin    Work repository
upstream  Personal public repository
```

Because the personal repository is public, the work account normally needs no collaborator permission to fetch it.

## Safe update procedure

Before synchronization:

```bash
git status
git switch main
git fetch origin
git pull --ff-only origin main
git fetch upstream
```

Review what would change:

```bash
git log --oneline main..upstream/main
git diff --stat main..upstream/main
```

Update only when the work branch can move forward without divergence:

```bash
git merge --ff-only upstream/main
python3 -m unittest discover -s tests -v
python3 scripts/validate_repository.py
git push origin main
```

If `--ff-only` fails, stop. Determine whether someone changed the work copy before merging or rebasing. Do not force-push over work changes.

## Why not `git push --mirror`

`git push --mirror` force-synchronizes all refs and can delete destination branches. Do not use it for routine updates. The fetch, review, fast-forward, validate, and push workflow is safer and auditable.

## Work-specific additions

Store internal links, proprietary sources, or employer-specific guidance in a separate private overlay repository. Do not merge that overlay back into the public project. A public-safe improvement should be recreated through the personal account after confirming its provenance and ownership.

The overlay may also transform the public guides into the work repository's preferred format. Perform that transformation downstream—for example during a private build or import step—so routine formatting changes do not create divergence in the synchronized public content.

## Future automation

Manual synchronization is the starting point. Automated personal-to-work pushes would require a narrowly scoped work credential stored outside the source and explicit employer approval. The absence of GitHub Actions in the work account does not prevent manual synchronization.

Website deployment is a separate decision from repository synchronization. A successful mirror proves only that the source arrived; it does not imply that Pages is enabled or that an internal website exists.
