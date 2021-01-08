#!/usr/bin/env python3
#  topographic maps segmentation
#
#     Huriel Reichel - huriel.ruan@gmail.com     
#     Nils Hamel - nils.hamel@bluewin.ch
#     
#     Copyright (c) 2020 Republic and Canton of Geneva
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np
import matplotlib
import scipy.misc
import scipy.ndimage
import skimage.filters

#import sklearn.metrics
import imageio
from skimage import color
import argparse

# create argument parser #
pm_argparse = argparse.ArgumentParser()

# argument and parameter directive #
pm_argparse.add_argument( '-i', '--input', type=str  , help='processing png path'    )
pm_argparse.add_argument( '-g', '--groundtruth', type=str  , help='groundtruth png path'    )
pm_argparse.add_argument( '-o', '--output' , type=str  , help='segmented png output path' )
pm_argparse.add_argument( '-l', '--li' , type=int, default=0  , help='use li threshold instead of minimum (1 to True and 0 to False). Default to 0' )
pm_argparse.add_argument( '-b', '--black' , type=int, default=0  , help='use = 1 if background is black and houses are blue. Default to 1' )

# read argument and parameters #
pm_args = pm_argparse.parse_args()
    
# Process image
grayscale = color.rgb2gray(imageio.imread(pm_args.input))
#grayscale = 255 - grayscale

# Process groundtruth
groundtruth = imageio.imread(pm_args.groundtruth)

# Take a look on data
#plt.subplot(1, 3, 1)
#plt.imshow(255 - grayscale, cmap='gray')
#plt.title('grayscale')
#plt.axis('off')
#plt.subplot(1, 3, 2)
#plt.imshow(grayscale, cmap='gray')
#plt.title('inverted grayscale')
#plt.axis('off')
#plt.subplot(1, 3, 3)
#plt.imshow(groundtruth, cmap='gray')
#plt.title('groundtruth binary')
#plt.axis('off')

# Use median filtering and plot
median_filtered = scipy.ndimage.median_filter(grayscale, size=4)
#plt.imshow(median_filtered, cmap='gray')
#plt.axis('off')
#plt.title('median filtered image')

# Result of the filtering and segmentation
result = skimage.filters.thresholding.try_all_threshold(median_filtered)

if (pm_args.li == 0):
    
    threshold = skimage.filters.threshold_minimum(median_filtered)
    
else:
    
    threshold = skimage.filters.threshold_li(median_filtered)
    
# Plot of results
#print('Threshold value is {}'.format(threshold))
predicted = np.uint8(median_filtered > threshold) * 255
#plt.imshow(predicted, cmap='gray')
#plt.axis('off')
#plt.title('minimum predicted binary image')

# change values to 0 and 255
if (pm_args.black == 0):
    predicted = np.where(predicted == predicted.min(), 0, 255)
    
else:
    predicted = np.where(predicted == predicted.min(), 255, 0)

# Export resulting image
matplotlib.image.imsave(pm_args.output, predicted) 

# Multiplying arrays 
#groundtruth_1d = np.array(groundtruth.flatten())  = 255
#predicted_1d = predicted.flatten() 
  
# printing result 

#print('f1_score: ', sklearn.metrics.f1_score(groundtruth_1d, predicted_1d))

#print('accuracy: ', sklearn.metrics.accuracy(groundtruth_1d, predicted_1d))
