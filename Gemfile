# Gemfile — Ruby dependencies for building this site locally.
#
# We deliberately use the `github-pages` gem rather than plain `jekyll`.
# That gem pins Jekyll and every plugin to the EXACT versions GitHub Pages
# runs on its servers. The upshot: if `bundle exec jekyll build` succeeds
# locally, it will succeed on GitHub Pages too. No "works on my machine".
source "https://rubygems.org"

gem "github-pages", group: :jekyll_plugins

# Windows/JRuby timezone data — harmless elsewhere, required there.
gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby]
