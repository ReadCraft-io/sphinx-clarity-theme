# Quickstart

This guide walks you through installing and enabling {{ project }} so you can start building fast, attractive documentation with the [Sphinx](https://www.sphinx-doc.org/) static site generator.

## Obtaining the theme

The theme is distributed as a Python wheel file (`.whl`), the standard binary distribution format for Python packages. A wheel file is named like `sphinx_<name>_theme-<version>-py-none-any.whl` and contains the theme's HTML, CSS, JavaScript, and Python code.

Payments and wheel file delivery are handled by Lemon Squeezy, a third‑party provider.

1. After successful payment, you will be redirected to an order page with a URL like `https://app.lemonsqueezy.com/my-orders/<order-id>`.
2. Download the wheel file from the order page to your computer.
   <img alt="Lemon Squeezy download" src="/images/lemonsqueezy-download.png" width="50%">

## Installation

Install the theme wheel file using your preferred Python package manager - we will describe pip and uv. Theme files and dependencies are placed where Sphinx can automatically find them.

1. Copy a wheel file to `vendors/` folder in your Sphinx project folder (a folder with `conf.py`). The wheel folder name is only recommendation.
1. Add the wheel as a dependency to virtual environment or Python project where do you manage Sphinx itself.

   ::::{tab-set}
   
   :::{tab-item} Using pip
   :sync: pip

   For [pip](https://pip.pypa.io/en/stable/), the most common package installer:
      
   ```bash
   pip install vendors/sphinx_clarity_theme-<version>-py3-none-any.whl
   ```

   :::
   
   :::{tab-item} Using uv
   :sync: uv

   For [uv](https://docs.astral.sh/uv/), a fast Python package manager:
   
   **Option 1: Add to existing project** (modifies `pyproject.toml` dependencies):
   
   ```bash
   uv add vendors/sphinx_clarity_theme-<version>-py3-none-any.whl
   ```
   
   **Option 2: Install without adding to project**:
   
   ```bash
   uv pip install vendors/sphinx_clarity_theme-<version>-py3-none-any.whl
   ```

   :::
   
   ::::

1. Verify installation. Check that the theme was installed successfully. You should see version information and the installation location.


   ::::{tab-set}
   
   :::{tab-item} Using pip
   :sync: pip

   ```bash
   pip show sphinx-clarity-theme
   ```

   :::
   
   :::{tab-item} Using uv
   :sync: uv
   
   ```bash
   uv pip show sphinx-clarity-theme
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