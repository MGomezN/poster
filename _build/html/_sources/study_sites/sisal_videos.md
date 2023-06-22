---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"tags": []}

# Sisal



## Sisal in images



```{code-cell} ipython3
:tags: [remove-input]

from ipywidgets import widgets
out1 = widgets.Output()
with out1:
  from IPython.display import YouTubeVideo
  video = YouTubeVideo(id="pUA4VlW96XM", width=854, height=480, fs=1, rel=0)
  display(video)

out = widgets.Tab([out1])
out.set_title(0, 'Youtube')
display(out)
```