# Publishing

Repository publication and GitHub Pages deployment are separate concerns. The searchable static site is built, validated, and deployed from the default branch by the dedicated Pages workflow.

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

## GitHub Pages deployment

The configuration targets `https://cterpening.github.io/certification-study-library/`. Pull requests to `main` run the build and validation job without publishing. On pushes to `main`, `.github/workflows/deploy-pages.yml` also:

1. runs the unit tests and repository validation;
2. prepares and strictly builds the allowlisted site;
3. validates generated links;
4. uploads `site/` as the official Pages artifact; and
5. deploys that artifact to the `github-pages` environment.

Repository **Settings → Pages → Build and deployment** must use **GitHub Actions**. The deployment job is restricted to artifacts produced by the preceding build job. Keep the `github-pages` environment limited to the default branch if environment protection rules are changed.

This deployment configuration is specific to the personal public repository. Downstream work mirrors do not inherit Pages settings and should follow the separate [work-mirror website guidance](https://github.com/cterpening/certification-study-library/blob/main/docs/WORK-MIRROR.md#website-behavior-in-the-work-mirror).

Do not use `mkdocs gh-deploy`; the reviewed GitHub Actions artifact should be the only deployment path.

## Protect `main`

Require pull requests and the repository-validation check. If scheduled monitors will create pull requests, allow the repository `GITHUB_TOKEN` to do so or change the workflow to create issues only.

## Public review

Confirm before launch:

- [x] No credentials, employer data, customer data, or private sources exist.
- [x] The AI-assisted and unofficial-project disclosures are visible.
- [x] The content and exam-integrity policy is linked.
- [x] All applicable local validation passes.
- [x] The strict site build and generated-link validation pass.
- [x] The configured GitHub Pages URL, repository name, and owner are correct.
- [ ] Keyboard navigation, focus visibility, color contrast, light/dark modes, mobile layout, and print output have been reviewed.
- [x] Generated navigation includes every active catalog exam and no unapproved document.
- [x] The canonical exam links resolve.
- [ ] The work-mirror process has been reviewed separately.

## Custom domain

A custom domain is optional. Configure and verify it through GitHub Pages settings; do not assume a committed `CNAME` file alone completes the configuration.
