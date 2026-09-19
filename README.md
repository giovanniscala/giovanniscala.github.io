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
hugo --gc --minify
python3 scripts/validate_site.py public
```

The publication generator is the canonical structured ledger for 24 journal
articles, five active preprints, and three conference/proceedings records. It
also generates matching BibTeX files and preserves attached author-owned
posters and slides.

## Publishing policy

Changes are reviewed on a branch targeting `website-source`. Deployment is a
separate, explicit step that generates the site from a validated source commit
and updates the production branch.
