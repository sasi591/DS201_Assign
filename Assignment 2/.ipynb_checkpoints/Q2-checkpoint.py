#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:23:09 2021

@author: sasi
"""

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

img = Image.open('image-36.jpg')
hist = img.histogram()
img = np.asarray(img).astype('int64')

R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]

avgimg = (R+G+B)//3
H, W = np.shape(avgimg)

avgimg = avgimg.flatten()
histogram = np.zeros(256, dtype=float)
for i in range(avgimg.size):
        histogram[avgimg[i]] += 1.

plt.plot(histogram, color='black')
plt.show()

cdf = np.zeros(256, dtype=float)
cdf[0] = histogram[0]
for i in range(1, len(histogram)):
    cdf[i] = cdf[i-1] + histogram[i]

plt.plot(cdf)
plt.show()

mapping = np.zeros(256, dtype=float)
for i in range(len(histogram)):
     mapping[i] = max(0, round((256*cdf[i])/(H*W))-1)