#!/usr/bin/env python3
"""
Post-build checks for the site. Run after `bundle exec jekyll build`:

    python3 _verification/verify.py

Catches the classes of breakage that have actually happened here:
  - a page losing its front matter, so Jekyll emits it raw with no layout,
    no <head> and therefore NO STYLESHEET (the page renders unstyled)
  - a pre-existing URL disappearing
  - duplicate or missing SEO metadata
  - key content or third-party embeds being dropped

Exits non-zero if anything fails, so it can gate a commit.
"""
import re, glob, os, sys

FAIL = []

def check(name, ok, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{'' if ok else '  -> ' + str(detail)}")
    if not ok:
        FAIL.append(name)

print("URLs")
missing = []
for line in open('_verification/urls-before.txt'):
    u = line.strip()
    if not u:
        continue
    p = '_site' + u
    if not any(os.path.isfile(c) for c in [p, p + 'index.html', p.rstrip('/') + '/index.html']):
        missing.append(u)
check("every pre-existing URL still resolves", not missing, missing)

print("\nPer-page metadata (comments stripped so commented-out tags are not counted)")
bad = []
stubs = []
for f in sorted(glob.glob('_site/**/*.html', recursive=True)):
    raw = open(f, encoding='utf-8').read()
    # Redirect stubs (e.g. /writing/) are not pages anyone reads: no nav, no
    # stylesheet, no analytics. They get their own checks below instead.
    if 'http-equiv="refresh"' in raw:
        stubs.append((f, raw))
        continue
    s = re.sub(r'<!--.*?-->', '', raw, flags=re.S)
    counts = {
        'h1':        len(re.findall(r'<h1[ >]', s)),
        'canonical': len(re.findall(r'rel="canonical"', s)),
        'title':     len(re.findall(r'<title>', s)),
        'og:title':  len(re.findall(r'property="og:title"', s)),
        'nav':       len(re.findall(r'id="nav"', s)),
        # The stylesheet check is the one that catches a page which lost its
        # front matter: Jekyll copies it through verbatim, so it has no <head>.
        'stylesheet': len(re.findall(r'assets/css/main\.css', s)),
        'analytics': len(re.findall(r'cloudflareinsights', s)),
    }
    if set(counts.values()) != {1}:
        bad.append((f.replace('_site', ''), counts))
check("each page has exactly one of each", not bad, bad)

print("\nContent")
home = open('_site/index.html', encoding='utf-8').read()
zoe = open('_site/zoe-and-zephy/index.html', encoding='utf-8').read()
for label, needle, hay in [
    ("homepage tagline", "no-BS tech strategy", home),
    ("Formspree endpoint", "formspree.io/f/mqaerpek", home),
    ("contact anchor", 'id="contact"', home),
    ("all three spotlights", "hardware suite", home),
    ("Zoe Vimeo embed", "player.vimeo.com", zoe),
    ("Zoe retailer link", "amazon.com/dp/B0F8Z9Z8ML", zoe),
    ("Zoe reviews", "Goodreads", zoe),
]:
    check(label, needle in hay)

check("press kit still served", os.path.isfile('_site/zoe-and-zephy/assets/zzpresskit.pdf'))
check("CNAME present", os.path.isfile('_site/CNAME') and open('_site/CNAME').read().strip() == 'shahidhussain.com')

print("\nImages")
# Every <img> on every page must point at a file that exists in the build.
# Catches a typo in an image path, or an image referenced before it is added.
broken = []
for f in glob.glob('_site/**/*.html', recursive=True):
    for src in re.findall(r'<img[^>]+src="([^"]+)"', open(f, encoding='utf-8').read()):
        if src.startswith('http'):
            continue
        if not os.path.isfile('_site' + src.split('?')[0]):
            broken.append(f"{f.replace('_site', '')} -> {src}")
check("every image on every page exists", not broken, broken)

print("\nRedirect stubs")
for f, raw in stubs:
    m = re.search(r'url=([^"]+)"', raw)
    target = m.group(1) if m else None
    tp = '_site' + (target or '')
    ok = bool(target) and any(os.path.isfile(c) for c in [tp, tp + 'index.html'])
    check(f"{f.replace('_site', '')} forwards to a real page ({target})", ok, target)
    canon = re.search(r'rel="canonical" href="https://shahidhussain\.com([^"]+)"', raw)
    check(f"{f.replace('_site', '')} canonical matches its destination", bool(canon) and canon.group(1) == target,
          canon.group(1) if canon else None)

print("\nWriting")
posts = sorted(glob.glob('_posts/*.md'), reverse=True)   # newest first, by filename date
essay_pages = []
for post in posts:
    slug = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', os.path.basename(post))[:-3]
    page = f'_site/writing/{slug}/index.html'
    essay_pages.append((slug, page))
    exists = os.path.isfile(page)
    check(f"essay '{slug}' published at /writing/{slug}/", exists)
    if not exists:
        continue
    h = open(page, encoding='utf-8').read()
    check(f"essay '{slug}' shows a machine-readable date", '<time datetime="' in h)
    check(f"essay '{slug}' is marked up as a BlogPosting", '"@type":"BlogPosting"' in h)
    check(f"essay '{slug}' has a meta description", '<meta name="description"' in h)
    check(f"essay '{slug}' links to the index", 'href="/writing/all/"' in h)
    front = open(post, encoding='utf-8').read().split('---')[1]
    check(f"essay '{slug}' sets a description in front matter", re.search(r'^description:', front, re.M) is not None)

if essay_pages:
    newest = f'/writing/{essay_pages[0][0]}/'
    stub = open('_site/writing/index.html', encoding='utf-8').read() if os.path.isfile('_site/writing/index.html') else ''
    check("/writing/ forwards to the NEWEST essay", f'url={newest}"' in stub, newest)
    idx = open('_site/writing/all/index.html', encoding='utf-8').read() if os.path.isfile('_site/writing/all/index.html') else ''
    check("index page lists every essay", all(f'/writing/{sl}/' in idx for sl, _ in essay_pages))
    feed = open('_site/feed.xml', encoding='utf-8').read() if os.path.isfile('_site/feed.xml') else ''
    check("RSS feed lists every essay", all(f'/writing/{sl}/' in feed for sl, _ in essay_pages))
    sm = open('_site/sitemap.xml', encoding='utf-8').read()
    check("sitemap lists every essay and the index", all(f'/writing/{sl}/' in sm for sl, _ in essay_pages) and '/writing/all/' in sm)
    check("sitemap omits the /writing/ redirect", '<loc>https://shahidhussain.com/writing/</loc>' not in sm)

print()
if FAIL:
    print(f"{len(FAIL)} CHECK(S) FAILED")
    sys.exit(1)
print("All checks passed.")
