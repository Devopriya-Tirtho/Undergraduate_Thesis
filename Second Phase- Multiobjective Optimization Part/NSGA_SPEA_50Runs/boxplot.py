# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 21:34:23 2021

@author: Hp
"""


# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
  




dataset=pd.read_csv('HyperVolume50Runs.csv')

dataset.dropna(inplace=True)

NSGAII=[]

SPEA2=[]

for i in range(0,dataset.shape[0]):
    NSGAII.append(dataset.at[i,'NSGAII'])
    SPEA2.append(dataset.at[i,'SPEA2'])


data = [NSGAII, SPEA2]
  
fig = plt.figure(figsize =(10, 7))
  
# Creating axes instance
ax = fig.add_axes([0, 0, 1, 1])
 # x-axis labels
ax.set_xticklabels(['NSGAII', 'SPEA2']) 
# Creating plot
bp = ax.boxplot(data)
  
# show plot
#plt.show()










############################3

# Import libraries
import matplotlib.pyplot as plt
import numpy as np
  


data = [NSGAII, SPEA2]
  
fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)
  
# Creating axes instance
bp = ax.boxplot(data, patch_artist = True,
                notch ='True', vert = 0)
  
colors = ['#0000FF', '#00FF00', 
          '#FFFF00', '#FF00FF']
  
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
  
# changing color and linewidth of
# whiskers
for whisker in bp['whiskers']:
    whisker.set(color ='#8B008B',
                linewidth = 1.5,
                linestyle =":")
  
# changing color and linewidth of
# caps
for cap in bp['caps']:
    cap.set(color ='#8B008B',
            linewidth = 2)
  
# changing color and linewidth of
# medians
for median in bp['medians']:
    median.set(color ='red',
               linewidth = 3)
  
# changing style of fliers
for flier in bp['fliers']:
    flier.set(marker ='D',
              color ='#e7298a',
              alpha = 0.5)
      
# x-axis labels
ax.set_yticklabels(['NSGAII', 'SPEA2'])
  
# Adding title 
plt.title("Customized box plot")
  
# Removing top axes and right axes
# ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
      
# show plot
plt.show(bp)