# Giovanni Scala — academic website source

This branch contains the Hugo/Wowchemy authoring source for
<https://giovanniscala.github.io/>. The generated production site lives on the
`master` branch and must not be edited by hand.

## Pinned toolchain

- Hugo Extended 0.83.1
- Go 1.17.13 (the module declares compatibility with Go 1.15)
- Wowchemy modules pinned in `go.mod` at commit `89d079bcf055`

## Build and validate

```bash
python3 scripts/generate_publications.py
site_build_dir="$(mktemp -d)"
hugo --gc --minify --destination "$site_build_dir"
python3 scripts/validate_site.py "$site_build_dir"
```

A fresh destination is required because this historical source branch still
contains an old tracked `public/` snapshot. That snapshot is not edited or used
as the validation target.

The publication generator is the canonical structured ledger for 24 journal
articles, seven active preprints, and three conference/proceedings records. It
also generates matching BibTeX files and preserves attached author-owned
posters and slides.

## Publishing policy

Changes are reviewed on a branch targeting `website-source`. Deployment is a
separate, explicit step that generates the site from a validated source commit
and updates the production branch.

## Windows local development

Use the pinned legacy Hugo Extended executable for this branch, not the newer
Hugo used by the Hugo Blox experiment. Download the Windows 64-bit **Extended**
release from [Hugo v0.83.1](https://github.com/gohugoio/hugo/releases/tag/v0.83.1)
and extract it to a dedicated directory. Install Go 1.17.13 separately if
needed; do not replace your current Hugo or Go installation globally.

From a fresh checkout of this branch, in PowerShell:

```powershell
& "C:\Tools\hugo-0.83.1\hugo.exe" version
go version
& "C:\Tools\hugo-0.83.1\hugo.exe" server --disableFastRender
```

Adjust the executable path to the actual extracted location. For the exact
validated production environment, see the GitHub Actions workflow.
Tailwind CSS, npm global launchers and Node.js are not required for this branch.

See [the modern migration plan](docs/modern-hugo-migration.md) before starting
a Hugo Blox upgrade.
