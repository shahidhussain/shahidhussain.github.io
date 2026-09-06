---
# ============================================================================
#  WORKED EXAMPLE ESSAY — copy this file to start a new one.
#
#  Filename MUST be: _posts/YYYY-MM-DD-url-slug.md
#  The date comes from the filename, and the slug becomes the URL. This file
#  publishes to /writing/how-to-publish-an-essay/.
#
#  Front matter (the block between the --- markers) sets the metadata.
#  `layout` is NOT needed: _config.yml applies the essay layout to every post
#  automatically.
# ============================================================================

# Shown as the page's <h1>, in the browser tab, and in link previews.
title: "How to publish an essay on this site"

# Optional but recommended. Becomes the meta description and the summary shown
# on /writing/. Aim for roughly 120–160 characters. Without it, the first
# paragraph is used instead.
description: "The three-step process for adding a new essay, and what each piece of front matter does."

# Optional. Shown at the top of the essay and used as the social preview image
# for link unfurls. Delete these two lines if the essay has no image.
# image: /images/spotlight01edit.jpg
# image_alt: "Describe the image for screen readers"
---

Everything below the closing `---` is the body of the essay, written in
Markdown. Write normally — the theme handles all the styling.

## Publishing a new essay

Create a file in `_posts/` named `YYYY-MM-DD-your-slug.md`, fill in the front
matter at the top, write the body, then commit and push. That is the whole
process. The essay appears at `/writing/your-slug/`, is added to the list on
`/writing/`, and is added to `sitemap.xml` automatically.

## What you can write

Standard Markdown all works. **Bold**, *italic*, and [links](https://example.com)
behave as you would expect.

- Bulleted lists
- Work fine

1. So do numbered ones
2. Like this

> Blockquotes are styled by the theme, which is useful for pulling out a
> quotation or a key claim.

Fenced code blocks are syntax-highlighted:

```
git add _posts/2026-09-06-my-new-essay.md
git commit -m "Add essay on platform migrations"
git push
```

### Headings

Start body headings at `##`. The essay's `title` in the front matter is already
rendered as the page's `<h1>`, so using `#` in the body would create a second
one — which search engines and screen readers both dislike.

## Previewing before you publish

To see it locally before pushing:

```
bundle exec jekyll serve
```

Then open <http://localhost:4000>. The site rebuilds as you save, so you can
leave it running while you write.

## Drafts

To hold an essay back, put it in a `_drafts/` folder with no date in the
filename. Drafts are excluded from the built site. Preview them with
`bundle exec jekyll serve --drafts`.
