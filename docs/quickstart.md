# Quickstart

This guide walks you through installing and enabling {{ project }} so you can start building fast, attractive documentation with the [Sphinx](https://www.sphinx-doc.org/) static site generator.

## Obtaining the theme

The theme is dual-licensed under the free MIT or Commercial License. For commercial use, the Commercial License is recommended. It offers bonus assets, no attribution requirements, and priority support.

Consider purchasing a license at https://readcraft.io/sphinx-clarity-theme to fund the development 🙏

## Installation

Install the theme file using your preferred Python package manager - we will describe pip and uv. Theme files and dependencies are placed where Sphinx can automatically find them.

1. Add the theme package as a dependency to virtual environment or Python project where do you manage Sphinx itself.

   ::::{tab-set}
   
   :::{tab-item} Using pip
   :sync: pip

   For [pip](https://pip.pypa.io/en/stable/), the most common package installer:
      
   ```bash
   pip install sphinx_clarity_theme
   ```

   :::
   
   :::{tab-item} Using uv
   :sync: uv

   For [uv](https://docs.astral.sh/uv/), a fast Python package manager:
   
   **Option 1: Add to existing project** (if you have `pyproject.toml`, it adds it as dependency to it):
   
   ```bash
   uv add sphinx_clarity_theme
   ```
   
   **Option 2: Install to active environment** (doesn't modify or require `pyproject.toml`):
   
   ```bash
   uv pip install sphinx_clarity_theme
   ```

   :::
   
   ::::

## Configuration

Configure the theme in your Sphinx `conf.py`.

1. Enable the theme.

   ```py
   html_theme = "sphinx_clarity_theme"
   ```

2. (Optional) Most visual and behavioral customization lives in `html_theme_options`; some items (like `html_favicon`) use standard Sphinx variables.

   ```py
   html_favicon = "favicon.svg"
   html_theme_options = {
      # See later for customization options
   }
   ```

Rebuild your docs and you should see {{ project }} applied.