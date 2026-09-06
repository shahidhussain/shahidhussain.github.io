# shahidhussain.com

A static site built with [Jekyll](https://jekyllrb.com/) and hosted on GitHub
Pages. No CMS, no build pipeline to babysit — push to `main` and GitHub builds
and publishes it.

## Why Jekyll

Every page used to carry its own copy of the `<head>`, the script tags and the
page skeleton. Now they live in one place each and every page renders through
them, so a change to the nav is a one-line edit rather than a find-and-replace.

## Where things live

| Path | What it is |
|---|---|
| `_config.yml` | Site-wide settings: URL, title, analytics token, plugins. **Restart `jekyll serve` after editing this** — it is the only file that does not hot-reload. |
| `_data/navigation.yml` | **The nav.** Single source of truth. Edit here, it changes everywhere. |
| `_includes/` | Reusable fragments: `head.html`, `header.html` (nav), `footer.html`, `scripts.html`, `analytics.html` |
| `_layouts/` | Page skeletons: `default.html` (all pages), `page.html` (standard content), `essay.html` (essays) |
| `_posts/` | Essays. One Markdown file each. |
| `index.html` | Homepage, served at `/` |
| `zoe-and-zephy/index.html` | Book page, served at `/zoe-and-zephy/` |
| `writing/index.html` | Essay index, served at `/writing/` |
| `assets/` | The Hyperbolic theme (CSS, JS, fonts) — **do not edit `main.css`** |
| `assets/css/custom.css` | All local styling changes go here |
| `_verification/` | Pre-refactor page snapshots, kept for reference. Excluded from the built site by its leading underscore. |

## Adding a nav item

Edit `_data/navigation.yml`:

```yaml
- title: About
  url: /about/
```

It appears on every page and in the mobile menu automatically — the mobile menu
is generated from the desktop list by `assets/js/main.js`.

## Publishing an essay

Create `_posts/YYYY-MM-DD-your-slug.md`, fill in the front matter, write the
body in Markdown, commit and push. It publishes to `/writing/your-slug/` and is
added to `/writing/` and `sitemap.xml` automatically.

Copy `_posts/2026-09-06-how-to-publish-an-essay.md` as your starting point — it
is annotated and explains every field.

## Running it locally

```bash
bundle install          # once
bundle exec jekyll serve
```

Then open <http://localhost:4000>. It rebuilds as you save.

## Two rules worth keeping

1. **Never hand-write `<title>`, meta description, canonical or Open Graph tags
   in a page.** `jekyll-seo-tag` generates all of them from front matter. Adding
   your own produces duplicates, and two canonical tags is worse than none. Set
   `title:`, `description:` and `image:` in front matter instead.
2. **Never edit `assets/css/main.css`.** It is the unmodified theme stylesheet.
   Put overrides in `assets/css/custom.css`, which loads after it.

## Theme

[Hyperbolic](https://pixelarity.com/hyperbolic) by Pixelarity, used under
licence. `main.css` is unmodified so the theme can be updated cleanly.
