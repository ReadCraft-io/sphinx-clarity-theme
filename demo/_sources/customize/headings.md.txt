# Headings

Headings establish hierarchy and make pages scannable. Control their relative sizes with a single CSS scale variable and customize the permalink icon via Sphinx settings.

## Heading scale

A *heading scale ratio* is the mathematical relationship used to size heading levels (H1, H2, H3, etc.). Rather than picking arbitrary sizes, a ratio produces a harmonious, consistent hierarchy.

Ratios that are too large or too small make headings feel disjointed or indistinct. Recommended ratios for documentation typically range between 1.125 and 1.333. In {{ project }} the scale is controlled by the `--article-heading--scale` CSS variable.

:::{tip} There are many [online type scale calculators](https://baseline.is/tools/type-scale-generator/).
:::

:::{rubric} Change article heading type scale
:::

1. Create `_static/styles/custom.css` file for custom CSS in the directory with `conf.py`. You can use any folder and filename, but this is convention.
1. In `conf.py`, set `html_static_path = ["_static"]` (or different folder for your setup), if it's not already.
1. Override `--article-heading--scale` CSS variable.
   ```css
   :root {
     --article-heading--scale: 1.333;
   }
   ```

For example, from left to right: default scale 1.25, then 1.33, then 1.5:

<img src="images/heading-scale-example.webp" width="100%">

## Permalink icon

Hovering over a heading reveals a *permalink* (an anchor link to that section). By default, Sphinx uses `¶` (paragraph symbol); for a more modern look you might prefer `#` (hash symbol).

<img src="images/permalink-icon.gif" width="75%" class="mx-auto">

1. In `conf.py`, set `html_permalinks_icon` (often a single character).
1. Ensure `html_permalinks = True` (default) so the icon is rendered.
   ```py
   html_permalinks_icon = "#"
   ```
