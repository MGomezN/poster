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

# Puerto Morelos

Submarine groundwater discharges (SGD) play a critical role in the dynamics of coastal systems. Through these sites, significant amounts of freshwater flow from the continental aquifer into the ocean, and, under suitable tidal and hydraulic gradient conditions, reverse flows can also occur. The significant increase in sea level caused by climate change will force marine intrusion to advance inland rapidly, therefore threatening underground freshwater reserves in coastal aquifers. An understanding of the hydrogeological structure where SGD occur is essential to activate early warning procedures. The present work is located in the Caribbean Sea, in the state of Quintana Roo, Mexico, specifically in Puerto Morelos. This area was selected because previous research has identified seven locations where large volume groundwater discharges occur. Twenty profiles (~20km) parallel to the coast were acquired. The resistivity meter used was a SuperSting R8 Marine (Advanced Geoscience, Inc.) together with a towed array composed of 11 electrodes with
10-m spacing and dipole-dipole survey configuration. A Lowrance GPS and sonar
transducer were used to collect lat/long and depth data for the survey.
The union of the resistivity and GPS data, as well as the linearization of the profiles, was carried out with specifically tailored codes written in Python. The data inversion was made with Pérez-Flores 2021 algorithm written in Fortran as well as with open-source software.
Reproducibility of the methods and results is guaranteed, as the material is available in a GitHub repository. The results provide new information about the structure of these underwater structures in Puerto Morelos.

```{figure} ../images/SEGABSTRACT.png
---
width: 1000px
name: fig15
---
Resistivity marine model in Puerto Morelos, Mexico. A. Study Location. B. Study area on the sea. C. Preliminar 3D electrical resistivity model. Submarine groundwater discharges are shown in yellow.
```
Support: National Council of Science and Technology (CONACyT). LANRESC. Mario
Rebolledo-Vieyra.
Keywords: SGD, freshwater, marine intrusion, karst, hydrogeology, climate change.
Topics related: Near Surface Geophysics, Electric and Electromagnetic Methods, Data
Analytics.
References
Pérez-Flores, M., Méndez-Delgado, S., y Gómez-Treviño, Imaging low-frequency and dc
electromagnetic fields
using a simple linear approximation. Geophysics, v. 66, n. 4, p. 1067–1081, SEG, 2001.


## 3D model

You can watch a video of our tutorial, "Processing gravity data with Harmonica," streamed live on Apr 22, 2021.
```{note}
This model may look nice. However, there are different problems in how data was collected and inherent uncertainties.
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