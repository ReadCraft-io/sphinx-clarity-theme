# Favicon

The favicon is the small icon shown in browser tabs, bookmarks, and history. Set it to reinforce branding.

:::{rubric} Set a favicon
:::

1. In `conf.py` set `html_favicon` to a path relative to `conf.py` (or an external URL).
   ```py
   html_favicon = "favicon.svg"
   ```
2. Use a square image (16×16, 32×32, or SVG). Prefer SVG for crisp scaling.
3. Rebuild to see it applied.
