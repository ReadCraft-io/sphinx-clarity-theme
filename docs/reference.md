# Reference

Technical reference for {{ project }}: theme options, template blocks, and CSS variables you can override.

{#reference-html-theme-options}
## HTML theme options

:::{list-table}
:header-rows: 1

- - Option
  - Default
  - Description
- - `default_layout`
  - `"default"`
  - Page layout used when no per‑page override (`"default"` or `"compact"`).
- - `logo_dark`
  - `""`
  - Path/URL to dark mode logo variant.
- - `logo_dark_invert`
  - `false`
  - Automatically invert light logo for dark mode when true.
- - `logo_url`
  - `""`
  - Override default root link target for logo/text.
- - `header_menu`
  - `[]`
  - List of navigation items (`label`, `url`, optional `as="button"`).
- - `language_select`
  - `{}`
  - Mapping of language codes to display names for selector.
- - `language_url`
  - `""`
  - URL pattern with placeholders `{language}` and `{page}`.
:::



{#reference-templates-and-blocks}
## Jinja templates and blocks

:::{list-table}
:header-rows: 1

- - Template
  - Block
  - Description
- - `layout.html`
  - `html_tag_attrs`
  - Add attributes to `<html>` tag.
- - `layout.html`
  - `head_tag_end`
  - Inject code before closing `</head>`.
- - `layout.html`
  - `body_tag_attrs`
  - Add attributes to `<body>` tag.
- - `layout.html`
  - `body_tag_start`
  - Immediately after opening `<body>`.
- - `layout.html`
  - `body_tag_content`
  - Main page content (between start/end blocks).
- - `layout.html`
  - `body_tag_end`
  - Inject code before closing `</body>`.
- - `partials/head.html`
  - `title_tag`
  - Content of `<title>` tag.
- - `partials/article_footer.html`
  - `article_footer_left`
  - Left column of [article footer](#custom-article-footer).
- - `partials/article_footer.html`
  - `article_footer_right`
  - Right column of [article footer](#custom-article-footer).

:::

{#reference-css-variables}
## CSS variables

Many aspects of {{ project }} are driven by CSS variables. Override defaults to adapt branding and visuals.

:::{seealso} Practical example: [customizing theme colors](#customization-colors).
:::

:::{tip} Learn variable names via browser dev tools: [](#howto-css-variable-in-browser).
:::

### Colors

The majority of CSS variables is related to colors used across the website.

% sass lexer used only for nicer highlighting

```sass
/* Base background color */
--color-base-100:

/* Secondary background color, slightly darker than base-100 */
--color-base-200:

/* Tertiary background color, darker than base-200 */
--color-base-300:

/* Text color for content on base backgrounds */
--color-base-content:

/* Primary brand color for main actions and emphasis */
--color-primary:

/* Text color for content on primary background */
--color-primary-content:

/* Secondary brand color for complementary elements */
--color-secondary:

/* Text color for content on secondary background */
--color-secondary-content:

/* Accent color for highlights and special emphasis */
--color-accent:

/* Text color for content on accent background */
--color-accent-content:

/* Neutral color for borders and subtle elements */
--color-neutral:

/* Text color for content on neutral background */
--color-neutral-content:

/* Informational message color (typically blue) */
--color-info:

/* Text color for content on info background */
--color-info-content:

/* Success state color (typically green) */
--color-success:

/* Text color for content on success background */
--color-success-content:

/* Warning state color (typically yellow/orange) */
--color-warning:

/* Text color for content on warning background */
--color-warning-content:

/* Error state color (typically red) */
--color-error:

/* Text color for content on error background */
--color-error-content:

/* Heading color */
--article-heading--color: 

/* Regular text color */
--article-text--color:

/* Color of code examples */
--article-mono--color: 
```

{#reference-css-vars-fonts}
### Fonts

The theme uses only a few font families which you can change using the following CSS variables.

:::{seealso} [Customizing theme fonts](#customization-fonts)
:::

```sass
/* Font family for general text. */
--font-sans:

/* Font family for source code examples */
--font-mono:

/* Font family for article headings */
--article-heading--font:

/* Regular text font family */
--article-text--font:
```

### Miscellaneous

CSS variables related to Sphinx documents generated from reStructuredText or Markdown source files.

```sass
/* Heading scale ratio */
--article-heading--scale:
```