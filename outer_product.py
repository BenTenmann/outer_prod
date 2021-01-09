#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 21:05:10 2021

@author: benjamintenmann
"""
import time
import os
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def outer_prod(name, size, pr=False):
    
    u = random.sample(list(range(1, 1001)), size)
    v = random.sample(list(range(1, 1001)), size)
    
    ### FOR-LOOPS ###
    if name == 'for':    
        
        M = []
        for i in u:
        
            row = []
            for j in v:
                
                row.append(i * j)
            M.append(row)
    
    
    ### LIST-COMPREHENSIONS ###
    elif name == 'ls':
        
        M = [i * j for i in u for j in v]


    ### MAP ###
    elif name == 'map':
        
        M = list(map(lambda i, j: i * j,
                     [i for i in u for j in v],
                     v*len(u)))
    
    
    ### OUTER-PROD ###
    else:
        
        M = np.outer(u, v)

    if pr == True:
        
        print(M)



size = 1_000
times = []
for name in ['for', 'ls', 'map', 'np']:
    
    for i in range(1,size+1):
        
        start = time.time()
        
            
        outer_prod(name, i)
            
        end = time.time()
        times.append(end-start)
    
df = pd.DataFrame({'time':times,
                   'size':list(range(1,size+1))*4,
                   'method':np.repeat(['for-loops', 'list-comprehension',
                             'map', 'outer-product'], size)})


sns.set_theme()
g, ax = plt.subplots(figsize=(9,6))

sns.lineplot(data=df, x='size', y='time', hue='method', ax=ax, err_style=None)
fig = ax.get_figure()
fig.savefig(os.getcwd()+'/efficiency_plot.png', dpi=400)

