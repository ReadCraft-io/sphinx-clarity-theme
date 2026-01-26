# Dark mode

Dark mode in {{ project }} improves readability, reduces eye strain, and aligns with modern user expectations. Users can switch instantly, and your styles adapt automatically.

:::{important} Dark mode cannot be deactivated.
:::

## How dark mode selection works

- On first visit, the color mode matches the user's OS preference.
- Users can switch modes any time using the toggle button.
- The selected mode is stored in `localStorage` for future visits.

## Different images for dark/light mode

You can differentiate images per color mode using built‑in CSS classes, or automatically invert a light image for dark mode:

1. Same image for both modes: do nothing.
1. Distinct light/dark variants: use `light-only` and `dark-only` classes.
1. No dark variant available: try automatic inversion with `invert-on-dark`.

Examples:

   :::::{tab-set-code}
   ::::{code-block} rst
   
   .. image:: /_static/georgy.jpg  
      :class: dark-only

   .. image:: /_static/flouffy.jpg  
      :class: light-only

   .. image:: /_static/mattes.jpg  
      :class: invert-on-dark

   ::::
   ::::{code-block} md
   
   :::{image} /_static/georgy.jpg
   :class: dark-only
   :::

   :::{image} /_static/flouffy.jpg
   :class: light-only
   :::

   :::{image} /_static/mattes.jpg
   :class: invert-on-dark
   :::
      
   ::::
   :::::