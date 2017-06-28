# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:33:49 2017

@author: Yitao
"""

import numpy as np

n = 100
m = 10000

u = 0.8
seuil = 0.6
rang = int(np.floor(n * u)) #the element to choose

X = np.random.randn(m, n)
X = np.sort(X, axis = 1)

proba = np.mean(np.cos(X[:, rang]) < seuil)

print(proba)