# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 18:31:36 2017

@author: Ruodan NI Yitao ZHANG
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

n = 2000000
rho = 0.3
a = -1.96
b = 1.96
# A = [0.3, 1]

X = []
while True:
    x_0 = np.random.randn()
    if((x_0 >= a) & (x_0 <= b)):
        break 
X.append(x_0)
print x_0

for i in range(n):
    u = rho * X[-1] + np.sqrt(1 - rho ** 2) * np.random.randn()
    if((u >= a) & (u <= b)):
        x = u
    else:
        x = X[-1]
    X.append(x)

x= np.linspace(np.min(X), np.max(X), 100)
f_x = np.exp(- x ** 2 / 2) / (np.sqrt(2 * np.pi)) / (norm.cdf(b) - norm.cdf(a))

n_bins = 2 * int(n ** (1. / 3.))
plt.hist(X, normed = True, bins = n_bins, label = "Histo empirique")
plt.plot(x, f_x, "r", label = "conditional normal distribution")
plt.legend(loc = "best")
plt.show()
