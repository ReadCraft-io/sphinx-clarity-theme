# Footer

Customize the footer copyright notice using standard Sphinx options.

:::{rubric} Change copyright statement 
:::

1. In `conf.py` set `copyright` (Sphinx ≥ 8.1: `%Y` expands to current year).
1. Ensure `html_show_copyright` isn’t `False`.
   ```py
   copyright = "%Y, Documatt.com, s.r.o."
   ```

:::{tip}
Avoid duplication: reuse `author` with an f‑string.

```py
author = "Documatt.com, s.r.o."
copyright = f"%Y, {author}"
```
:::

:::{rubric} Disable copyright statement
:::

1. Set `html_show_copyright = False`.
