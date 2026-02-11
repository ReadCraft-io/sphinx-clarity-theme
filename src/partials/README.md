# Template Partials Structure

This directory contains modular template components for the Sphinx Clarity theme. The main `layout.html` template has been refactored into smaller, reusable partials following Jinja and Sphinx theme best practices.

## File Structure

### Core Components

- **`head.html`** - Document head section with meta tags, CSS links, and favicon
  - Handles charset, viewport, and canonical URLs
  - Includes CSS files and custom CSS variables
  - Manages dark mode script loading

- **`header.html`** - Main site header with logo, navigation, and toolbar
  - Logo with dark mode support
  - Desktop and mobile navigation menus
  - Search button, language selector, and mode switcher

- **`footer.html`** - Main site footer with copyright and theme credits
  - Displays copyright information
  - Links to Sphinx and theme documentation

### Navigation Components

- **`breadcrumb.html`** - Breadcrumb navigation showing document hierarchy
  - Shows path from root to current document
  - Displays parent documents with links

- **`article-nav.html`** - Previous/Next article navigation
  - Links to previous and next documents in the TOC
  - Responsive layout for desktop and mobile

- **`sidebar-toggles.html`** - Mobile sidebar toggle buttons
  - Primary drawer toggle (Table of Contents)
  - Secondary drawer toggle (On This Page)

### Content Components

- **`article-footer.html`** - Article-specific footer with community links
  - Links to GitHub, Discord, or other community platforms
  - Edit on GitHub link

- **`search-modal.html`** - Search dialog/modal component
  - Full-page search modal with keyboard shortcuts
  - Search form with enter key support

- **`scroll-to-top.html`** - Scroll to top button
  - Fixed position button for easy navigation

### Utility Components

- **`macros.html`** - Reusable Jinja macros
  - `logo()` - Logo component with dark mode variants
  - `language_selector()` - Language switcher dropdown
  - `mode_switcher()` - Light/dark mode toggle
  - `primary_drawer_content()` - Global TOC (site navigation)
  - `secondary_drawer_content()` - Local TOC (on this page)

- **`scripts.html`** - JavaScript includes and configuration
  - Scroll spy configuration
  - Sphinx-generated script files
  - Custom theme scripts

## Usage in Main Layout

The main `layout.html` template includes these partials using:

```jinja
{% include "partials/head.html" %}
{% include "partials/header.html" %}
{% include "partials/breadcrumb.html" %}
{% include "partials/article-nav.html" %}
{% include "partials/footer.html" %}
{% include "partials/search-modal.html" %}
{% include "partials/scripts.html" %}
```

Macros are imported using:

```jinja
{% from "partials/macros.html" import primary_drawer_content, secondary_drawer_content %}
```

## Benefits of This Structure

1. **Maintainability** - Each component has a single responsibility and is easier to update
2. **Reusability** - Components can be included in multiple templates
3. **Testing** - Isolated components are easier to test and debug
4. **Collaboration** - Multiple developers can work on different components simultaneously
5. **Customization** - Users can override specific partials without modifying the entire layout
6. **Code Organization** - Logical grouping makes the codebase more navigable

## Sphinx Theme Override Path

Users can override any partial by creating a file with the same name in their project's `_templates/partials/` directory. Sphinx will automatically use the custom version instead of the theme's default.

Example:
```
project/
  _templates/
    partials/
      header.html      # Custom header override
      footer.html      # Custom footer override
```

## Best Practices

- Keep partials focused on a single component or section
- Use meaningful comments to explain complex logic
- Pass data via Jinja context variables rather than hardcoding
- Use macros for reusable UI elements that need parameters
- Include accessibility attributes (aria-label, role, etc.)
- Maintain consistent naming conventions (kebab-case for files)
