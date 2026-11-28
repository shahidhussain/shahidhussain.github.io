---
# Publication date and URL come from this file's name:
#   2025-11-01-moving-from-wordpress-to-github-pages.md
#   ->  1 November 2025, /writing/moving-from-wordpress-to-github-pages/
# Do not rename this file once published; the name is the URL.
title: "Moving from WordPress to GitHub Pages"
description: "My personal website is no longer running on WordPress. Here's the new setup, and how to do it yourself."
---

My personal website here is no longer running on WordPress. Why: it’s become harder to maintain, harder to use, and moving eliminates hosting costs.

This is the new setup:

- The site is now hosted on [GitHub Pages](https://pages.github.com), which is free.
- There’s no CMS, just static HTML / CSS / JS files and assets.
- Custom domains are supported with a few DNS records ([GitHub’s instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)).

This setup avoids local development, because GitHub Codespaces provides a cloud dev box (with a free monthly allowance that’s plenty for a personal site). So you don’t have to bother with changes to your local machine OR dealing with repo authentication. (I wasn’t planning a blog, so I skipped more comprehensive solutions like Jekyll. But if you do go that way, support is easily available inside Codespaces.)

Here’s how to set this up.

- Create a new codespace by going [here](https://github.com/codespaces), then New Codespace, select your `your-username.github.io` repo to clone into it.
- Download a static site template from somewhere like [HTML5 UP](https://html5up.net) or [Start Bootstrap](https://startbootstrap.com/theme/personal), then upload it into your codespace that is connected to the repo. (Uploading a folder structure directly into the repo through GitHub’s website can be awkward, so use the codespace instead.)
- Make your edits in the codespace, git push it to the repo, and it’s live. For the strange people among you who don’t like shipping straight to prod, the codespace can also give you a private preview of the site before pushing it live.

Once it's in GitHub, you can of course connect Claude Code or whatever you prefer to it, and ship changes without ever seeing the code again.

*Update: I’ve since moved the site to Jekyll, which GitHub Pages builds for you, to support this blog.*
