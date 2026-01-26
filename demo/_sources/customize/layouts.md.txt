# Page layouts

{{ project }} supports multiple page layouts suitable for different kinds of documentation, or parts of documentation. Layouts change overall page structure.

## Default layout

Traditional three‑column: global table of contents (ToC) on the left, document content center, local ToC ("On this page") on the right.

:::{image} images/default-layout.webp
:::

## Compact layout

Two‑column: no global ToC; local ToC on the right. Suitable for README‑style or single‑page docs where a global ToC would be empty.

:::{image} images/compact-layout.webp
:::

## Changing layout

If you want to change layout, you can set it for a whole documentation or individual pages only.

:::{rubric} Set layout globally
:::

1. In `conf.py`'s `html_theme_options`, set `default_layout` option to layout name.

   :::{code-block} python

   html_theme_options = {
       "default_layout": "compact"
   }
   :::

:::{rubric} Set layout per page (override global)
:::

1. Add `layout` metadata at the top of the Markdown or reStructuredText document.

   ::::{tab-set-code}
   :::{code-block} rst
   
   :layout: compact

   Welcome to my project!
   ----------------------
   
   :::
   :::{code-block} md
   
   ---
   layout: compact
   ---
   
   # Welcome to my project!
   
   :::
   ::::