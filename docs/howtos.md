# How-tos

This section collects concise how‑to guides for common Sphinx theme tasks. Not every guide is specific to {{ project }}, but each is compatible with it and useful when customizing your documentation.

{#howto-jinja-blocks}
## Overriding template blocks (e.g., adding tracking codes)

With {{ project }} you can easily integrate marketing and analytics tools (Google Analytics, Google Tag Manager, Hotjar, etc.). These tools typically require you to embed tracking code in the page `<head>` or `<body>`.

Sphinx themes use the [Jinja templating engine](https://jinja.palletsprojects.com/). Jinja *blocks* let you override portions of a template by extending it from a directory listed in the `templates_path` setting. See [Sphinx’s templating documentation](https://www.sphinx-doc.org/en/master/development/theming.html#templating) for details.

{{ project }} exposes blocks suitable for injecting tracking code:

- `head_tag_end` (right before the closing `</head>` tag)
- `body_tag_end` (right before the closing `</body>` tag)

See the complete list at [](#reference-templates-and-blocks).

:::{rubric} Example: Insert tracking code via template blocks
:::

1. In `conf.py`, add `templates_path = ["_templates"]`.
1. Create an `_templates/` folder next to `conf.py`.
1. Create a `layout.html` file inside it. The initial `{% extends %}` line is mandatory. Then override the suitable block(s) with `{% block <name> %}`.

   For example, inserting GTM:
   
   ```html+jinja
   {% extends "!layout.html" %}

   {% block head_tag_end %}
       <!-- Google Tag Manager -->
       <script>(function(w,d,s,l,i){...})(window,document,'script','dataLayer','GTM-A6755KNG');</script>
       <!-- End Google Tag Manager -->
   {% endblock %}
 
   {% block body_tag_end %}
       <!-- Google Tag Manager (noscript) -->
       <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-A6755KNG" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
       <!-- End Google Tag Manager (noscript) -->
   {% endblock %}
   ```

:::{seealso} Alternative to adding custom JavaScript is described in [](#howto-add-custom-css-js).
:::

{#howto-add-custom-css-js}
## Adding custom CSS or JS files

Sphinx provides simple ways to include custom JavaScript, CSS, or HTML in your documentation website. {{ project }} fully supports these mechanisms, allowing you to extend or style your site as needed—for example, adding a custom font or changing the background color with a small snippet of CSS.

:::{rubric} How to add a custom CSS or JS file
:::

1. Create a folder for extra files next to `conf.py` (conventionally `_static/`).
1. Add extra files like `styles/custom.css` or `scripts/custom.js` under `_static/`.
1. In `conf.py` use `html_css_files` or `html_js_files`. These lists of CSS/JS files are injected into every page. Paths can be relative to `_static/` or external (CDN) URLs. For example:
   
   ```
   html_static_path = ["_static"]
   html_css_files = ["styles/custom.css"]
   html_js_files = ["scripts/custom.js"]
   ```
1. {{ project }} injects:
  - CSS files just before the closing `</head>` tag
  - JS files just before the closing `</body>` tag.

   :::{seealso}
  If you need a different injection location, override the respective template block (for example `body_tag_start`) as described in [](#howto-jinja-blocks).
   :::

:::{rubric} Example: Change headings with custom CSS
:::

1. Continuing the above steps, in your `_static/styles/custom.css`, add some style rules. E.g.,
   ```css
   h2 {
     background-color: light-dark(#a470d9, #edadb7);
   }
   ```
  :::{seealso} For a description of the `light-dark()` function see [](#howto-light-dark-fn).
   :::
1. Rebuild and test.

   :::{video} images/custom-css-example.mp4
   :::


{#howto-light-dark-fn}
## Handling light and dark mode variants in custom CSS

When styling your {{ project }} documentation with custom CSS, you may need to differentiate dark and light mode variants—especially when choosing colors.

With the `light-dark()` CSS function you can specify different values for light and dark color schemes in a single declaration: `light-dark(lightValue, darkValue)`. The theme ensures these styles switch automatically based on the current mode.

For example, this will apply `#a470d9` in light mode and `#edadb7` in dark mode.

```css
h2 {
  background-color: light-dark(#a470d9, #edadb7);
}
```

You can also use it when overriding variables (see [](#howto-css-variables)). For example:

```css
:root {
  --main-bg-color: light-dark(#f5f5f5, #a470d9);
  --main-text-color: light-dark(#222, #edadb7);
}
```

{#howto-css-variables}
## Overriding CSS variables

Many aspects of the {{ project }} design are controlled by CSS variables. This makes it easy to update colors, fonts, spacing, or other design tokens in one place. You override them with standard CSS to adapt the branding of your documentation.

A CSS variable (also called a custom property) lets you define reusable values in your stylesheets. CSS variables are defined using the `--variable-name` syntax and accessed with the `var()` function. For example:

```css
:root {
  --main-bg-color: #f5f5f5;
  --main-text-color: #222;
}

body {
  background: var(--main-bg-color);
  color: var(--main-text-color);
}
```

:::{seealso} Complete list of [](#reference-css-variables).
:::

:::{seealso} Practical usage of CSS variable overrides for configuring [](#customization-colors) or [](#customization-fonts).
:::

{#howto-css-variable-in-browser}
### How to find out variable name to override

1. Open your documentation website in a web browser.
1. Right-click on the element you want to customize and select {guilabel}`Inspect` (or press {kbd}`F12` to open Developer Tools).
1. In the {guilabel}`Elements` or {guilabel}`Inspector` tab, select the HTML element whose style you want to change.
1. In the {guilabel}`Styles` panel, look for CSS rules applied to that element. CSS variables are shown as `var(--variable-name)`.

For example, the warning admonition uses `--color-warning` and `--color-warning-content` CSS variables. Have a look how to find out these variable names in Chrome DevTools.

:::{video} images/howto-css-variable-in-browser.mp4
:::


% TODO:
% Combine your and theme Tailwind CSS
% =========================================
% *Tailwind CSS variables*: Since the theme is based on Tailwind CSS, any [Tailwind CSS theme variables](https://tailwindcss.com/docs/theme) can be overriden too. E.g., a spacing system or responsive breakpoints.

