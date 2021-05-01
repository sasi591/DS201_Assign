#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:15:52 2021

@author: sasi
"""

import scipy as sp
import matplotlib.pyplot as plt

wave = sp.io.wavfile.read('test.wav')
x = range(len(wave[1]))
plt.plot(x, wave[1])

