# Publishing

The repository can be published before the planned searchable site is implemented. Repository publication and GitHub Pages deployment are separate milestones.

## Create the personal public repository

From this local repository:

```bash
gh auth login
gh repo create certification-study-library \
  --public \
  --source=. \
  --remote=origin \
  --push
```

Before publishing, review the repository name, owner, license, public-content policy, and all files included in the initial commit.

## Enable GitHub Pages after the site scaffold exists

The seed repository does not yet contain the MkDocs configuration or Pages deployment workflow. After those files are added and validated:

1. Replace placeholder `site_url`, `repo_name`, and `repo_url` values in `mkdocs.yml`.
2. Open **Settings → Pages**.
3. Under **Build and deployment**, choose **GitHub Actions**.
4. Run the Pages deployment workflow.
5. Protect the `github-pages` environment so only the default branch can deploy.

The future workflow should build the site strictly, upload the static artifact, and deploy through the official Pages actions.

## Protect `main`

Require pull requests and the repository-validation check. If scheduled monitors will create pull requests, allow the repository `GITHUB_TOKEN` to do so or change the workflow to create issues only.

## Public review

Confirm before launch:

- [ ] No credentials, employer data, customer data, or private sources exist.
- [ ] The AI-assisted and unofficial-project disclosures are visible.
- [ ] The content and exam-integrity policy is linked.
- [ ] All applicable local validation passes.
- [ ] The strict site build passes when the site scaffold is present.
- [ ] Placeholder GitHub URLs are replaced.
- [ ] The canonical exam links resolve.
- [ ] The work-mirror process has been reviewed separately.

## Custom domain

A custom domain is optional. Configure and verify it through GitHub Pages settings; do not assume a committed `CNAME` file alone completes the configuration.
