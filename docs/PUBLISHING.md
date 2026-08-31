# Publishing

Repository publication and GitHub Pages deployment are separate milestones. The searchable static-site scaffold exists, but deployment remains intentionally inactive until its content, visual design, accessibility, and repository settings are reviewed.

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

## Build and preview locally

Install the pinned site dependency, generate the allowlisted source tree, and start the preview server:

```bash
python -m pip install -r requirements-site.txt
python scripts/prepare_site.py
python -m mkdocs serve --config-file .site-build/mkdocs.yml
```

Rerun `prepare_site.py` after changing a canonical guide, catalog, homepage template, or site asset. Generated `.site-build/` and `site/` files are disposable.

The production-equivalent validation is:

```bash
python scripts/prepare_site.py
python -m mkdocs build --strict --config-file .site-build/mkdocs.yml
python scripts/validate_site.py
```

## Enable GitHub Pages after review

The configuration targets `https://cterpening.github.io/certification-study-library/`. Confirm that repository owner and name before adding the deployment workflow, then:

1. Add a workflow that repeats the strict build, uploads `site/` with the official Pages artifact action, and deploys it with the official Pages deployment action.
2. Open **Settings → Pages**.
3. Under **Build and deployment**, choose **GitHub Actions**.
4. Run the Pages deployment workflow.
5. Protect the `github-pages` environment so only the default branch can deploy.

Do not use `mkdocs gh-deploy`; the reviewed GitHub Actions artifact should be the only deployment path.

## Protect `main`

Require pull requests and the repository-validation check. If scheduled monitors will create pull requests, allow the repository `GITHUB_TOKEN` to do so or change the workflow to create issues only.

## Public review

Confirm before launch:

- [ ] No credentials, employer data, customer data, or private sources exist.
- [ ] The AI-assisted and unofficial-project disclosures are visible.
- [ ] The content and exam-integrity policy is linked.
- [ ] All applicable local validation passes.
- [ ] The strict site build and generated-link validation pass.
- [ ] The configured GitHub Pages URL, repository name, and owner are correct.
- [ ] Keyboard navigation, focus visibility, color contrast, light/dark modes, mobile layout, and print output have been reviewed.
- [ ] Generated navigation includes every active catalog exam and no unapproved document.
- [ ] The canonical exam links resolve.
- [ ] The work-mirror process has been reviewed separately.

## Custom domain

A custom domain is optional. Configure and verify it through GitHub Pages settings; do not assume a committed `CNAME` file alone completes the configuration.
