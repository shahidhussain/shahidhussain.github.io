# Verification results

Run against `_site/` produced by `bundle exec jekyll build` (Jekyll 3.10.0 via
the `github-pages` gem, i.e. the exact version GitHub Pages runs).

## 1. Build
Clean. No errors or warnings.

## 2. Pre-existing URLs — 52/52 resolve
Every URL the site served before the refactor still resolves in the build,
checked programmatically against `urls-before.txt`. Includes:
- `/`
- `/zoe-and-zephy/`
- `/zoe-and-zephy/assets/zzpresskit.pdf` (retired from the page, URL kept alive)
- all 48 image assets

## 3. Content preservation
Checked against the before-snapshots in `before/`.
- Homepage: all copy, both banner buttons, all three spotlights, the Formspree
  endpoint (`mqaerpek`) — present.
- Zoe: all copy, the Vimeo embed, all four retailer links, all three Goodreads
  reviews, every image — present.
- Outbound links: all preserved except three absolute self-links
  (`https://shahidhussain.com`, `/`, `/#contact`) intentionally rewritten as
  root-relative now that it is one site. Same destinations.

## 4. No duplicate metadata
Every page has exactly one `<h1>`, one `<title>`, one canonical, one
`og:title`, one nav, one analytics beacon. Verified across all four pages.

## 5. Custom domain
`CNAME` (`shahidhussain.com`) is present in the build output — the custom
domain is unaffected.

## 6. Sitemap
Lists exactly the four real pages. The press kit PDF is excluded (retired) but
still served.

## Intentional changes
- `/index-demo.html` now returns 404 (theme demo page, deleted by agreement).
- Press kit link and MailerLite form removed from the Zoe page.
- Zoe gains an `h1` (it previously had none) and section headings become `h2`.
- Homepage gains the shared footer, which it did not have before.
- Both pages gain the nav.
