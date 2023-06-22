---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Andros, Bahamas

Jupyter Book also lets you write text-based notebooks using MyST Markdown.
See [the Notebooks with MyST Markdown documentation](https://jupyterbook.org/file-types/myst-notebooks.html) for more detailed instructions.
This page shows off a notebook written in MyST Markdown.

## What would the aquifer look like if we could see beneath the surface?

Electrical resistivity imaging (ERI) is a non-invasive technique in the field of hydrogeophysics that
provides structural and electric information about the subsurface. It is based on the physical property
known as “resistivity”. Different materials will exhibit different values of resistivity based on their
intrinsic capacity to conduct electricity. This contrast is especially strong in coastal aquifers like Andros,
where the resistivity values represent the combined rock and water properties – being influenced by
both the porosity of the rock and the presence of water with different properties. In addition, ERI can
help locate important features like sinkholes and fracture conduits in rocks.
For all the above, ERI is used, among other applications, to investigate groundwater, helping to
understand the distribution of saline water, freshwater, mixing zones, the geology that controls the
flow of subsurface water and provide more insights into hydrogeological parameters (Rubin and
Hubbard, 2005). Porosity is one of those fundamental parameters -especially for transport models-
because it provides volumetric storage. If supplementary information like pore geometry and
heterogeneity is provided, it allows determining parameters such as permeability and hydraulic
conductivity that, among others, define the flow in an aquifer (Kazakis et al., 2016). Limitations of ERI
are examined by Costall et al. (2020).
Examples of the ERI images collected recently on Northern North Andros during Phase II of the project
are shown in Figure 8. ERI results are plotted as cross-sections in which the x-axis is the distance of
the transect, the y-axis is the depth the survey is reaching, and the color represents the resistivity
value measured in Ohm-m. All plots shown in this report represent preliminary images with color
scales that differ between images (to be corrected after careful post-processing).

```{code-cell}
print(2 + 2)
```

TYPICAL EXAMPLES OF ERI IMAGES. THE UPPER ERI TRANSECT SHOWS SIMPLE , STRATIFIED MEDIA ( COMBINED
ROCK AND WATER PROPERTIES ), AND THE LOWER IMAGE SHOWS A HETEROGENOUS DISTRIBUTION OF WATER /ROCK
PROPERTIES, POSSIBLY REFLECTING KARST FEATURES .


In practice, to obtain an ERI image it is necessary to place a transect with electrodes in the ground.
Changing the spacing between electrodes allows imaging to different depths and show features at
different resolution. Once the transect is placed, the response of the subsurface can be measured with different electrical arrangements, each of which provides complementary information on the
resistivity distribution. Two very common electrical arrangements are the dipole-dipole and Wenner.

IMAGE


F IGURE 9: D ISTRIBUTION OF THE 73 ERI TRANSECTS CARRIED OUT IN A RANGE OF DIFFERENT GEOMORPHOLOGICAL AND
HYDROLOGICAL ZONES ACROSS NORTHERN N ORTH A NDROS .

For ERI acquisition (terrestrial, marine, and terrestrial-marine) an AGI SuperSting R8 with 56 passive
electrodes was used. A total of 73 electrical resistivity imaging transects (Figure 9) were collected
during the two geophysics fieldwork seasons (Nov 3rd - December 14th, 2022, and 14th - 26th January
2023).
ERI Data acquisition was organized in seven subprojects. (1) Calibration – comparing ERI with
conductivity profiles from wells with different vadose zone and freshwater thicknesses. (2) Old Well
Field ERI mapping - to identify lens thickness variations between wells and identify karst (risk of
collapse). (3) Freshwater lens West – to understand lens thickness variations where well coverage is
minimal and to understand discharge to the west coast. (4) Fossil Creek - to characterize the “electrical
footprint” around fossil creeks and infer associated rock properties. The study of fossil creeks is critical
to assessing the impact of rising sea levels on the island’s groundwater island. It potentially contributes
to engineering delays in the dissection of the lens on sea level rise. (5) Tidal creeks - understanding
how flows in tidal creeks may interact with the freshwater lens. (6) Karstic development – effect of
cave systems on lens thickness. (7) Spatial variation of rock properties – to evaluate how
representative a single ERI line may be and how the models change with the different volumes of
aquifer that are analyzed.
At targeted locations, ERI profiles were compared with vertical logs of specific electrical conductivity
(fluid salinity) and well diameter (caliper logs) from wells that penetrate through the mixing zone into
the top of the underlying saline zone. Figure 10 compares ERI images from different electrical arrays
in the same transect, both with 6 m spacing of electrodes, supporting interpretation of geoelectrical
model and assignment of hydrological units from ERI survey.


IMAGE

F IGURE 10: REPRESENTATIVE EXAMPLE OF THE RESULTS OF SUBPROJECT 1 CALIBRATION (ON THE CAUSEWAY TO RED
B AYS). C OMPARISON WITH DOWNHOLE DATA FROM WELL BW1 (RIGHT) SHOWS GOOD CORRELATION WITH FLUID
CONDUCTIVITY PROFILES ( PURPLE ) AND ROCK PROPERTIES ( CALLIPER LOG - BLUE ).


The BW1 area is especially important as it corresponds to the area where the tidal response switches
from being governed by the tidal signal at the east coast to a more rapid yet lower amplitude tides on
the north coast. Further investigation in this area using ooverlapping ERT profiles that allow imaging
to different depths reveal lateral heterogeneity in Red Bays Causeway area near well BW1 and suggest
possible fracture/fault control linked to surface pond topography (Figure 11).


IMAGE

F IGURE 11: REPRESENTATIVE EXAMPLE OF THE RESULTS OF SUBPROJECT 3, FRESH WATER LENS WEST . I NDIVIDUAL AND
PRELIMINARY RESULTS OF THREE ERI TRANSECTS OVER THE SAME AREA AS WELL BW1 ( LOCATED ON CAUSEWAY TO RED
B AYS). FUTURE WORK WILL WORK ON GENERATING A SINGLE MODEL FOR THE ENTIRE TRANSECT .
Blue holes are far less common in the northern part of the island than further south, but well-known
karst features in this area include Conch Sound ocean hole and Uncle Charlies blue hole onshore. Close
examination of satellite imagery and ground-based exploration reveals these two features are the
most obvious and accessible amongst a number of less spectacular (5-50+ m diameter) karst
landforms that define an approximately east-west oriented “karst corridor” between Uncle Charlies
in the west and Conch Sound in the east (Figure 12).

IMAGE

F IGURE 12: DISTRIBUTION OF TRANSECTS FOR SUBPROJECT 6, KARSTIC DEVELOPMENT . LOCATION OF ERT TRANSECTS (RED
LINES ) RELATIVE TO KARST FEATURES ( BLUE CIRCLES ) ALONG AN EAST - WEST ORIENTED KARST CORRIDOR . D ATA FOR T15
( HIGHLIGHTED IN YELLOW RECTANGLE ) ARE GIVEN IN FIGURE 14.

ERI surveys were carried out offshore in the area of Conch Sound ocean hole, which had been explored
originally by a British Cave Diving Expedition (Farr & Palmer, 1984), and more recently has been
reported known length of the cave up to 1.9 km, plus 0.45 km of associated passages (Kakuk, 2006,
no survey provided). This site is known to exhibit strong tidally-reversing currents with exchange of
seawater and groundwater and is representative of a number of ocean holes along the east coast of
North Andros that provide routes for the net discharge of fluids that are not fresh or brackish, but
rather marginally elevated in salinity relative to local seawater (Whitaker and Smart 1990, 1993). A 3D
bathymetric map was generated using a CHIRP sonar for the area around the cave entrance, and close
to this we carried out a Marine Electrical Resistivity Tomography. This shows a broad ellipsoid of very
low resistivity (<2 Ohm-m) that is considerably larger than the surveyed cave passage, within the
generally low resistivity values measured (maximum 14 Ohm-m) (Figure 13).



IMAGE

F IGURE 13: REPRESENTATIVE EXAMPLE OF THE RESULTS OF SUBPROJECT 6, KARSTIC DEVELOPMENT IN THE MARINE
PORTION . A) 3D BATHYMETRIC MAP OF CAVE ENTRANCE FROM CHIRP SONAR SURVEY , B) COMPASS AND TAPE SURVEY
FROM BRITISH C AVE D IVING E XPEDITION 1982 (FARR & P ALMER , 1984), AND C) M ARINE E LECTRICAL RESISTIVITY
T OMOGRAPHY AT C ONCH SOUND BLUE H OLE .

The onshore section of the “karst corridor” was the target of a large number of densely-spaced ERT
profiles (Figure 12). Despite rapid transmission of the tidal signal between onshore features along this
corridor (Figure 6), ERT profiles provide no evidence of a single major conduit in the shallowest 25m.
However, some of these transects do show significant lateral variability in resistivity (Figure 14). ERT
profiles suggest that in these areas the layer of more dense rock within the freshwater lens is
punctuated by low resistivity features a few m across. This area also displays more significant lateral
variations in resistivity at depth. This ERT response occurs in areas of dense pit cave development (eg
to the north of T15, Figure 14), which can be recognized from characteristic surface textures apparent
in satellite imagery.


IMAGE

F IGURE 14: REPRESENTATIVE EXAMPLE OF THE RESULTS OF SUBPROJECT 6 AND 7, KARSTIC DEVELOPMENT . N ORTH -SOUTH
ERT PROFILE SHOWING A ZONE OF HIGH RESISTIVITY AT A DEPTH OF 3-9 M BELOW GROUND LEVEL THAT IS LATERALLY
MORE CONTINUOUS TO THE SOUTH BUT BECOMES MORE BROKEN UP TO THE NORTH OF THE TRANSECT . T HIS APPEARS TO
CORRESPOND TO AN AREA THAT IS CHARACTERISED BY A HIGH DENSITY OF METER - SCALE KARST PITS , THAT SHOW
PREFERENTIAL ORIENTATION TO THE NE-SW ( BLACK LINES ) AND N-S ( ORANGE LINES ).

The degree to which surface textures apparent from satellite imagery can be used to indicate
subsurface complexity in electrical response that likely reflects cave development was further
evaluated in areas away from the “karst corridor”. The value of this approach is illustrated in Figure
15 in which the more northerly transect shows low resistivity patches that may accord with caves and
zones of very high resistivity at depths of 25-35 m (up to 50 m) that may reflect sediment filled cavities.
This contrasts with the simple distribution of properties in the transect from an area where no
complex surface textures are apparent from satellite imagery.
Future work will involve the re-processing of all ERI images and data quality assessment, using
numerical analysis and modeling, inversion of data, and open-source software (e.g., ResIPy).


IMAGE


F IGURE 15: REPRESENTATIVE EXAMPLE OF THE RESULTS OF SUBPROJECT 2 AND 7, O LD WELL FIELD MAPPING . TEXTURES
APPARENT FROM SATELLITE IMAGERY AND ASSOCIATED SUBSURFACE COMPLEXITY IN ELECTRI CAL RESPONSE .



When your book is built, the contents of any `{code-cell}` blocks will be
executed with your default Jupyter kernel, and their outputs will be displayed
in-line with the rest of your content.

```{seealso}
Jupyter Book uses [Jupytext](https://jupytext.readthedocs.io/en/latest/) to convert text-based files to notebooks, and can support [many other text-based notebook files](https://jupyterbook.org/file-types/jupytext.html).
```

## Create a notebook with MyST Markdown

MyST Markdown notebooks are defined by two things:

1. YAML metadata that is needed to understand if / how it should convert text files to notebooks (including information about the kernel needed).
   See the YAML at the top of this page for example.
2. The presence of `{code-cell}` directives, which will be executed with your book.

That's all that is needed to get started!

## Quickly add YAML metadata for MyST Notebooks

If you have a markdown file and you'd like to quickly add YAML metadata to it, so that Jupyter Book will treat it as a MyST Markdown Notebook, run the following command:

```
jupyter-book myst init path/to/markdownfile.md
```
