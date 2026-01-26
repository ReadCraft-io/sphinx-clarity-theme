{#customization-colors}
# Colors

Adjust any color used by the theme — backgrounds, text, accents, admonitions — by [overriding CSS variables](#howto-css-variables) inside a [custom CSS file](#howto-add-custom-css-js). {{ project }} gives you complete control while keeping the defaults sensible.

:::{rubric} Example: How to change website background
:::

The page background is determined by CSS varaible `--color-base-100`. If you change it, also adjust article text and heading colors (`--article-text--color` and `--article-heading--color`) so they match and maintain good contrast.

:::{seealso} Complete list of [available CSS variables](#reference-css-variables) you can override.
:::

To support both color modes, supply values with the `light-dark()` function as described in [](#howto-light-dark-fn).

1. Create `_static/styles/custom.css` next to `conf.py` (other paths work too; but this is the convention).
1. In `conf.py`, ensure `html_static_path = ["_static"]` (or your chosen folder).
1. In `custom.css` add overrides:
   ```css
   :root {
     --color-base-100: light-dark(#ffe066, #5fbdff);
     --article-text--color: light-dark(#ff6f61, #ffd60a);
     --article-heading--color: light-dark(#ff6f61, #ffd60a);
   }
   ```
1. Result:
   :::{video} images/customizing-colors.mp4
   :::
