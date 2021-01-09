#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 11:50:56 2021

@author: benjamintenmann
"""

import numpy as np
from scipy.stats import uniform

n_cities = 500
coords = uniform.rvs(size=n_cities) + uniform.rvs(size=n_cities)*1j

def dist(a, b): # calculates distance between two points
    d = abs(a - b)
    return d
    
compute_dist = np.frompyfunc(dist, 2, 1) # vectorise distance function

D = compute_dist.outer(coords, coords).astype(np.float64)