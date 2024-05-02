#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 22:35:04 2024

@author: reggiehacker
"""

## Example 2
import numpy as np
import matplotlib.pyplot as plt

#velocity
v0 = 10

#define list of masses
mass = [10, 50, 100]

#plot data
objects = ['Book','Dumbbell','Man']

#define list for KE
KE = []

#Find kinetic energy
for m in mass:
    x = 0.5*m*(v0**2)
    KE.append(x)

#plot
positions = range(len(KE))

plt.bar(positions, KE)
plt.xticks(positions, objects)
plt.ylabel('Kinetic Energy')

plt.show()


