# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 17:18:41 2017

@author: Yitao
"""
import numpy as np
import scipy.stats as sps
from matplotlib import pyplot as plt

a = 5
n = 10000

x = np.random.rand(n)
X = np.linspace(-5 * a, 5 * a, 1000)
x = a * np.tan(np.pi * x)
f_X = a/(np.pi * (X **2 + a**2))

plt.hist(x, normed = True, bins = 2 * int(n **(1. / 3.)), range = [-5 *a, 5 *a])
plt.plot(X, f_X, "r", label = "theory")
plt.show()



