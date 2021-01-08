# median_filtering - image segmentation of houses in swisstopo's topographic maps
This a median filtering image segmentation procedure using scikit learn developed with the aim of getting the houses only from swisstopo topographic maps

# Overview

This part of STDL's RegBL project and this procedure's main aim is to segment houses from other targets in swisstopo's topographic maps. Unfortunately, to this point this is not enough automatized, though this is a work in progress and depending on its results, it may be improved in the near future. 

# Usage

First of all, the algorithm requires a groundtruth raster. For that one can create a polygon shapefile over some few houses. If the choice is well made, the same groundtruth can be used to all maps. Once the shapefile is created is must be converted to raster. **See auto-rasterize** (https://github.com/hurielreichel/auto-rasterize) for more information. 


As we are working with scikit learn, all .tif files must be converted to .png or .jpg, including the groundtruth one. A good way to batch do this is through imagemagick (https://imagemagick.org/index.php). Check link for installation guide in your OS. An example of how to batch convert all .tif files to png in a folder is:

```
$  mogrify -format png *.tif
```
Finally, run the python code:

```
$ python3 median-filter.py -i /path/to/input.png -o /path/to/output_segmented.png -g /path/to/groundtruth.png
```

As observed, the main arguments are the **input** image, the **output** segmented image and the **groundtruth** image. There's also an optional argument that will run medial_filter with a Li threshold in the place of the default minimum. Set it as 1 if you want to use it. This especially useful when minimum thresholding doesn not work, as it can make you run out of memory. See the example:

```
$ python3 median-filter.py -i /path/to/input.png -o /path/to/output_segmented.png -g /path/to/groundtruth.png -l 1
```

Another optional argument is the transformation of background and house colour when the base image has a black background, as some swisstopo maps. Fr that use the **black** argument, as below:
```
$ python3 median-filter.py -i /path/to/input.png -o /path/to/output_segmented.png -g /path/to/groundtruth.png -l 1 -b 1
```

# Preliminary results for the proof of concept


# Copyright and License

**rgb-from-geotiff** - Huriel Reichel, Nils Hamel <br >

# Copyright and License
Copyright (c) 2020 Republic and Canton of Geneva

This program is licensed under the terms of the GNU GPLv3. Documentation and illustrations are licensed under the terms of the CC BY-NC-SA.

# Dependencies

Python 3.8.5 of superior

Packages may be installed either by pip or conda

* Numpy 1.18.4

* matplotlib 3.3.0

* scipy 1.5.4

* skikit-image 0.18.1

* imageio 2.9.0
