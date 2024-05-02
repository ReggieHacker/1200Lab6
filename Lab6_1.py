#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 22:35:03 2024

@author: reggiehacker
"""

###Example 1
import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(2,7,50)

y_e = np.exp(x_values)
y_x = x_values**3.6


#Subplot creation
plt.subplots(1,3, figsize= (10, 5))

##Subplots
#Regular Plots
plt.subplot(1,3,1)
plt.plot(x_values, y_e, label = "e^x")
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(1,3,1)
plt.plot(x_values, y_x, label = "x^3.6")
plt.xlabel('x')
plt.ylabel('y')
plt.title('x^3.6 and e^x')

plt.legend()

#semilog plot
plt.subplot(1,3,2)
plt.semilogy(x_values, y_e, label = "e^x")
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(1,3,2)
plt.semilogy(x_values, y_x, label = "x^3.6")
plt.xlabel('x')
plt.ylabel('y')
plt.title('x^3.6 and e^x')

plt.legend()

#log log plot
plt.subplot(1,3,3)
plt.loglog(x_values, y_e, label = "e^x")
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(1,3,3)
plt.loglog(x_values, y_x, label = "x^3.6")
plt.xlabel('x')
plt.ylabel('y')
plt.title('x^3.6 and e^x')


plt.tight_layout()
plt.show()