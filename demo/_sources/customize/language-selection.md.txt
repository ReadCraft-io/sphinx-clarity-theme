# Language selection

If your documentation is translated into multiple languages, {{ project }} provides a locale dropdown for quick switching.

<img src="images/language-select.gif" width="50%">

:::{rubric} Enable language selection
:::

The selector is disabled by default. Define available locales and a pattern for locale URLs to enable it.

1. Define available translations with `html_theme_options`'s `language_select` option. Translations are a dict of _\<language-code\>: \<language-name\>_. For example, in `conf.py`:

   ```py
   html_theme_options = {
      "language_select": {
         "en": "English",
         "cs": "čeština",
         "ua": "Українська",
      }
   }
   ```
1. Define a URL pattern with `html_theme_options`'s `language_url` option. Each language version must live at distinct URL address. For example:
   - `/docs/en/latest/quickstart.html`
   - `/docs/cs/latest/quickstart.html`
   - `/docs/ua/latest/quickstart.html`

   URL pattern can use placeholders:
   - `{language}` → <em>\<language-code\></em> from `language_select`
   - `{page}` → current page path

   For the example above: `/docs/{language}/latest/{page}`.

   ```py
   html_theme_options = {
      "language_select": {
         "en": "English",
         "cs": "čeština",
         "ua": "Українська",
      },
      "language_url": "/docs/{language}/latest/{page}",
   }
   ```
