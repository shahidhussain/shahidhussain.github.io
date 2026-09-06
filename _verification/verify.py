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
for f in sorted(glob.glob('_site/**/*.html', recursive=True)):
    s = re.sub(r'<!--.*?-->', '', open(f, encoding='utf-8').read(), flags=re.S)
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

print()
if FAIL:
    print(f"{len(FAIL)} CHECK(S) FAILED")
    sys.exit(1)
print("All checks passed.")
