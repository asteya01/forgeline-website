# Forgeline website

Static website for **Forgeline** ("Forge ahead.") and its two products,
**Newton** (AI in your terminal) and **Freezeframe** (copy code from coding videos).

## Build

```sh
./package.sh
```

This runs `build.py` (Python 3, no packages needed), copies `assets/`, `site.css`,
`site.js`, `theo.js` and `img/` into `dist/`, and makes `../forgeline-website.zip`.
The zip always includes `newton.zip` (kept in `assets/`).

## Deploy (Cloudflare Pages)

- **Upload assets:** upload the contents of `dist/` (or the zip) in one deployment.
- **Git integration:** build command `sh package.sh`, output directory `dist`.

## Layout

| Path | What it is |
| --- | --- |
| `build.py` | Shared header, footer, theme script and the Newton page |
| `pages/` | One file per page (home, Freezeframe, about, founders, invest, donate, privacy, terms, 404) |
| `site.css`, `site.js`, `theo.js` | Styles, interactions, and the "Ask Theo" helper |
| `assets/` | Videos, captions, icons, share image, `newton.zip`, the Freezeframe extension zip |
| `img/` | Freezeframe screenshots |

## To fill in before launch

- Real founder name (Founders page). The contact email is `CONTACT_EMAIL` in `site.js` (also in `theo.js`, `pages/privacy.py`, `pages/terms.py`)
- `SITE_URL` at the top of `build.py` once the domain is chosen
- A donation method on the Donate page
- Chrome Web Store link for Freezeframe
- A lawyer's review of Privacy and Terms
