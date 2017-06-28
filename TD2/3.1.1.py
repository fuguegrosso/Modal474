# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: Ruodan NI Yitao ZHANG
"""
import numpy as np
from numpy.linalg import norm
import scipy.stats as sps
import matplotlib.pyplot as plt

n = 5000

rho = 0.3
X = []
X.append(np.random.randn())
for i in range(n):
    for j in range(i):
        X.append(rho * X[-1] + np.sqrt(1 - rho ** 2) * np.random.randn())

x = np.linspace(np.min(X), np.max(X), 100)
f_x = np.exp(- x ** 2 / 2) / (np.sqrt(2 * np.pi))

n_bins = 2 * int(n ** (1. / 3.))
plt.hist(X, bins = n_bins, normed = True, histtype = "step", label = "histo")
plt.plot(x, f_x, "r", label = "Normal distribution")
plt.legend(loc = "upper right")
plt.show()
        
