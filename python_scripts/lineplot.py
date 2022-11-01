# -*- coding: utf-8 -*-
"""
Created on Tue May 10 13:38:58 2022

@author: Matt
"""

    
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots()

a = np.arange(0,50)
b = a**2
  
plt.plot(a, b)
plt.title("Test plot")
fig