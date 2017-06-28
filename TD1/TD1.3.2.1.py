# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:47:30 2017

@author: Yitao
"""

import numpy as np

n = 20
m = 10000
p = 0.2
seuil = 5

X = np.random.rand(m, n)
X = np.cumsum(X, axis = 1)

indicatrices = (X < seuil) #boolean matrix of trues and falses
index_proba = np.mean(indicatrices, axis = 0)
n_0 = np.min(np.argwhere(index_proba <= p))

print("\nn_0={}".format(n_0 + 1))



