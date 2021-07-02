# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 23:36:04 2021

@author: Hp
"""

# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


import scipy.stats


dataset=pd.read_csv('HyperVolume50Runs.csv')

dataset.dropna(inplace=True)

NSGAII=[]

SPEA2=[]

for i in range(0,dataset.shape[0]):
    NSGAII.append(dataset.at[i,'NSGAII'])
    SPEA2.append(dataset.at[i,'SPEA2'])

NSGAII=np.array(NSGAII)
SPEA2=np.array(SPEA2)

std_NSGAII=np.std(NSGAII)
std_SPEA2=np.std(SPEA2)
print(std_NSGAII)
print(std_SPEA2)
mean_NSGAII=np.mean(NSGAII)
mean_SPEA2=np.mean(SPEA2)
print(mean_NSGAII)
print(mean_SPEA2)

MannWhitney=scipy.stats.mannwhitneyu(NSGAII, SPEA2, use_continuity=True, alternative=None)



