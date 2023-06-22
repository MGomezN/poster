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

**Authors:**
[Santiago Soler](https://github.com/santisoler),
[Andrea Balza Morales](https://github.com/andieie),
[Agustina Pesce](https://github.com/aguspesce),
[Leonardo Uieda](https://github.com/leouieda)

    
In this tutorial, we will walk through the steps of transforming observed absolute gravity measurements into a grid of residual gravity disturbances at a constant height. On our way there, we will showcase some of the core utilities of many of our open-source libraries:

1. Fetch and cache the data using [Ensaio](https://github.com/fatiando/ensaio) or [Pooch](https://github.com/fatiando/pooch)
1. Calculate the gravity disturbance using [Boule](https://github.com/fatiando/boule)
1. Interpolate data and apply map projections to grids using [Verde](https://github.com/fatiando/verde)
1. Perform topographic correction and equivalent-source interpolation using [Harmonica](https://github.com/fatiando/harmonica)

+++ {"tags": []}

## Video

You can watch a video of our tutorial, "Processing gravity data with Harmonica," streamed live on Apr 22, 2021.
```{note}
Remember that the Youtube tutorials may differ slightly from the ones presented on this website, which contains the more recent version of our tutorials
```

```{code-cell} ipython3
:tags: [remove-input]

from ipywidgets import widgets
out1 = widgets.Output()
with out1:
  from IPython.display import YouTubeVideo
  video = YouTubeVideo(id="d0AGgIdL3nw", width=854, height=480, fs=1, rel=0)
  display(video)

out = widgets.Tab([out1])
out.set_title(0, 'Youtube')
display(out)
```

## Study area

The **Bushveld Igneous Complex** is located in South Africa and is the largest known layered igneous intrusion. It has been tilted and eroded forming the outcrops around what appears to be the edge of a great geological basin: the Transvaal Basin. It is approximately 2 billion years old and is divided into four different limbs: the northern, southern, eastern, and western limbs. The Bushveld Complex comprises the Rustenburg Layered suite, the Lebowa Granites and the Rooiberg Felsics, that are overlain by the Karoo sediments. See
 {cite}`webb` for an overview and previous interpretations of the Bushveld in depth.

```{figure} ../images/bushveld_igneous_complex_geology.jpg
---
width: 1000px
name: bushveld-fig
---
The Bushveld Igneous Complex.
```
