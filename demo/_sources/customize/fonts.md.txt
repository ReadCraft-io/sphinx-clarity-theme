{#customization-fonts}
# Fonts

Switch the fonts used across UI and article content by [overriding CSS variables](#howto-css-variables) in a [custom CSS file](#howto-add-custom-css-js). Only a few core variables control typography, making changes straightforward.

:::{rubric} Example: Change default and heading fonts
:::

{{ project }} uses a small set of font families — for example `--font-sans` (UI + article body text) and `--article-heading--font` (article headings). If you want different fonts, create a custom CSS file, import the fonts (via `@import` or `@font-face`), then set the variables.

:::{seealso} Complete list of [font-related CSS variables](#reference-css-vars-fonts) you can override.
:::

The example below uses font files hosted by [Google Fonts](https://fonts.google.com), but local fonts work the same way.

1. Create `_static/styles/custom.css` next to `conf.py`.
1. In `conf.py`, ensure `html_static_path = ["_static"]`.
1. At the very beginning of `custom.css`, add an `@import` rule for the fonts (imports must precede other rules), then set variables:
   ```css
   @import url("https://fonts.googleapis.com/css2?family=Bitter:ital,wght@0,100..900;1,100..900&family=Oswald:wght@200..700&display=swap");

   :root {
     --font-sans: "Bitter", sans-serif;
     --article-heading--font: "Oswald", sans-serif;
   }
   ```
1. Result:
   ![](images/customizing-fonts-example.webp)
