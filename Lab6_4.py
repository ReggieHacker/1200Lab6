#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 22:35:05 2024

@author: reggiehacker
"""

##Example 4
#Importing libraries
import numpy as np
import matplotlib.pyplot as plt

#define the abundance of the most prevalent elements (numbers = percent)
Hydrogen = 74
Helium = 24
Oxygen = 1.04
Carbon = 0.46
Other = 0.5

#Create the pie chart and labels
slices = [Hydrogen, Helium, Oxygen, Carbon, Other]
labels = ['Hydrogen', 'Helium', 'Oxygen', 'Carbon', 'Other']

#Exploding the small slices so we can see the labels better
explode = [0,0,0.1,0.5,0.1]

plt.pie(slices, labels=labels, explode=explode)


#Create title
plt.title("Abundance of elements in the universe")
