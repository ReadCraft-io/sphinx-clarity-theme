{#custom-article-footer}
# Article footer

The article footer appears directly after page content. It’s empty by default, but you can inject custom actions, links, or messages (any HTML) by overriding Jinja blocks.

<img src="images/article-footer.webp">

:::{rubric} Customize article footer
:::

The footer consists of two blocks: `article_footer_left` and `article_footer_right`.

:::{seealso} List of all [](#reference-templates-and-blocks) you can override.
:::

1. In `conf.py` set `templates_path = ["_templates"]`.
1. Create `_templates/partials/article-footer.html`.
1. Extend the original template and override desired blocks. Example:

   ```html+jinja
   {% extends "!partials/article_footer.html" %}
   
   {% block article_footer_left %}
     Do you have a question? Ask on
     <a href="https://discord.gg/uaEa43HB">Discord</a>
   {% endblock %}
   
   {% block article_footer_right %}
     Edit this page on
     <a href="https://github.com/your-repo/{{ pagename }}.md?edit">GitHub</a>
   {% endblock %}
   ```
