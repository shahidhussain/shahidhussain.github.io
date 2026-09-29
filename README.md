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
| `_layouts/` | Page skeletons: `default.html` (all pages), `page.html` (standard content), `essay.html` (one essay) |
| `_posts/` | **Essays.** One Markdown file each. |
| `writing/index.html` | `/writing/` — forwards to the newest essay. Never needs editing. |
| `writing/all/index.html` | `/writing/all/` — the index of every essay. Never needs editing. |
| `index.html` | Homepage, served at `/` |
| `zoe-and-zephy/index.html` | Book page, served at `/zoe-and-zephy/` |
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

## Adding a page

Create an HTML file with front matter setting `layout`, `permalink`, `title` and
`description`. For a standard content page use `layout: page` and write the body
directly; the layout supplies the heading and section wrapper. Then add it to
`_data/navigation.yml` if it belongs in the nav.

## Publishing an essay

1. Create `_posts/YYYY-MM-DD-your-slug.md`. The date is the publication date;
   the slug becomes the URL: `/writing/your-slug/`.
2. Put front matter at the top:

   ```yaml
   ---
   title: "Your title"
   description: "One sentence. Shown in Google results, link previews, the index and the RSS feed."
   # image: /images/writing/your-slug/cover.jpg   # optional: link-preview image only
   ---
   ```

3. Write the body in Markdown underneath. Start section headings at `##` —
   the title is already the page's `<h1>`.

   **Pictures** are plain Markdown too; no HTML needed. Put the file in
   `images/writing/your-slug/` and write, on a line of its own:

   ```markdown
   ![Describe the picture for people who can't see it](/images/writing/your-slug/photo.jpg)
   ```

   Several on the same line sit side by side. To let readers click through to
   the full-size file, wrap it in a link:
   `[![Description](/images/.../photo.jpg)](/images/.../photo.jpg)`.

   On wide screens a picture sits to the right of the text, **level with the
   paragraph that follows it** — so put it just before the text it belongs
   beside. On narrower screens it appears in the text where you wrote it.
   Pictures are never enlarged beyond their own size.
4. Commit and push.

That's all. On the next build the essay gets its own page, `/writing/` starts
forwarding to it, the previous newest essay gains a link to it, and it's added
to `/writing/all/`, `sitemap.xml` and `feed.xml`. Nothing else needs editing.

To preview first: `bundle exec jekyll serve`, then open
<http://localhost:4000/writing/>.

**Things that will catch you out:**

- **Don't rename an essay's file after publishing.** The filename *is* the URL,
  so renaming it breaks every link anyone has shared. Fix a title by changing
  `title:`, not the filename.
- **Future dates don't publish.** Jekyll skips essays dated after the build,
  and GitHub only builds when you push. An essay dated tomorrow won't appear
  until your first push *on or after* tomorrow. Preview one locally with
  `bundle exec jekyll serve --future`.
- **Revising an essay?** Add `last_modified_at: YYYY-MM-DD` to its front
  matter. It shows an "Updated" date and tells search engines it changed.

### Previous and Next

Essays are read newest-first, so the buttons are named in *reading* order:
**Previous** goes to the newer essay, **Next** to the older one. That is the
reverse of Jekyll's own `page.next` / `page.previous`, which are chronological
— so `_layouts/essay.html` deliberately swaps them. See the comment there
before changing it.

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
