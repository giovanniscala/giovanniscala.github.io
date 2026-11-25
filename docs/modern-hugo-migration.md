# Modern Hugo Blox migration

## Baseline

The existing site uses Hugo Extended 0.83.1, Go 1.17.13 and Wowchemy commit
89d079bcf055. The source is on website-source; master contains generated
production pages. The September 19, 2026 source validation and deployment
succeeded. The source branch also contains historical generated snapshots.
Do not copy those snapshots into the new source.

## Stage 1: establish a styled starter locally

The owner's experimental my-site checkout uses Hugo Extended 0.152.2 and
blox-tailwind v0.9.0. Its package manifest, module versions and lockfile
must be inspected before changing versions. Tailwind v4 separates the
compiler (@tailwindcss/cli) from the CSS library (tailwindcss). Install
both in the **project** alongside @tailwindcss/typography and all starter
dependencies; the CSS resolver cannot rely on a global npm or npx cache.
Prefer the starter's declared package manager and lockfile. Do not
create a custom global batch wrapper. Use the local dependency executable
and test a clean build before importing content.

For the documented starter in the older v4 line, the manifest contains
tailwindcss, @tailwindcss/cli, @tailwindcss/typography, preact and pagefind.
The exact package versions should come from the selected starter's lockfile.
Reference:
https://github.com/HugoBlox/hugo-theme-academic-cv/blob/main/package.json

## Stage 2: migrate content on an isolated source branch

- Preserve the canonical publication ledger and the BibTeX/Markdown
  generator; adapt its output to the selected starter's front matter.
- Convert content/home widget pages to the selected Blox landing page blocks.
- Convert the author profile to the selected version's author schema.
- Keep original CV, photos, PDFs, slides, aliases, publication slugs and
  other existing URLs; do not overwrite the new starter's theme/config
  wholesale with the 2021 versions.
- Remove all starter demo content and unused assets.
- Migrate profile, projects, grants, open positions, teaching, talks,
  software and contact pages. Keep the official institutional links.
- Inspect the rendered CSS, navigation, mobile layout, search and math.
- Keep the original branch and public site unchanged while developing.

## Stage 3: build and deploy

Use a clean clone and the pinned Hugo, Go, Node and package-manager versions.
Install dependencies from the committed lockfile, build to a fresh output
directory, run the adapted publication and link validators, and verify
that the stylesheet is nonempty and contains actual generated utilities.
Commit authoring files only, not node_modules, the build cache, or output.
Run a preview build in GitHub Actions on the migration branch.

Only after the replacement passes review, configure GitHub Pages to use
the validated build from the approved source branch. The current legacy
workflow uses a manual/explicit deployment policy; do not change the
production branch or Pages settings while the migration is unverified.

## Outstanding inputs

Obtain the exact current my-site source checkout (without node_modules,
public, resources, .git or private files) or a clean Git branch containing
its authoring source and lockfile. Confirm which new starter version will
be the migration target. No local Windows installation changes are needed
until the chosen source and manifest have been inspected.
