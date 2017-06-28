# -*- coding: utf-8 -*-
"""
Created on Fri May 12 14:30:49 2017

@author: Yitao
"""

from pylab import *
import numpy as np
import scipy.stats as sps
import time
import matplotlib.pyplot as plt

n = 20
M = int(1e5)
a = 4 * np.sqrt(n)
la1 = a / float(n+1)
la2 = 2 * a / float(n * (n-1))

N = 100 # independent test
Stock = np.zeros((N, 5))

StartTime = time.time()


print("-" * 45)
print("\t Valeur theorique")
print("\t La proba exact est" + str(sps.norm.cdf(-c)))



for k in range(N):
    print("run" + str(k+1) + " sur" + str(N))
    Y = np.random.randn(M, n)
    print("-" * 45)
    print("\t Monte Carlo naive")
    Z = np.sum(Y, axis = 1)
    p_mc = np.mean(Z >= a)
    delta = 1.96 * sqrt(p_mc * (1 - p_mc) / M)
    print("Intervalle de confiance = " + str(p_mc) + "+-" + str(delta))
    
    Stock[i, 0] = p_mc
    
    print("-" * 45)
    print("\t Selection et mutation des trajectoires")
    
    X = np.array([np.zeros(M), Y[:,0]])
    X = X.T #initialisation
    
    
    indices = np.zeros(M) #les indices selected
    right = 1
    
    for i in range (1,n):
        G = np.exp(la1 * (X[:,1] - X[:,0]))
        right = right *np.mean(G)
        values = np.arange(0, M)
        indices = np.random.choice(values, p = G / np.sum(G), size = M)
        X[:, 0] = X[indices, 1]
        X[:, 1] = X[:, 0] + Y[:, i]
        
    left = np.mean((X[:,1] >=a) * np.exp(-la1 * X[:,0]))
    right_theorique = np.exp((n-1) * (la1 ** 2) / 2)
    est1_theorique = left * right_theorique
    est_1 = left * right
    
    print("\t Constante normalisation exacte est: " + str(right_theorique))
    print("\t Constante normalisation estimee est: " + str(right))
    print("\t erreur relative est: " + str(np.abs(right - right_theorique) / right_theorique))
    print("\n \t Estimation exacte est: " + str(est1_theorique))
    print("\t estimation estimee est: "+ str(est_1))
    
    Stock[i, 1] = est1_theorique
    Stock[i, 2] = est_1
    
    print("-" * 45)
    print("En poderant en trajectoires hautes")
    
    X = np.zeros((M, n))
    X[:, 0] = Y[:, 0]
    indices = np.zeros(M)
    right = 1
    
    for i in range(0, n-1):
        G = np.exp(la2 * X[:, i])
        right = right * np.mean(G)
        values = np.arange(0, M)
        indices = np.random.choice(values, p = G / np.sum(G), size = M)
        X = X[indices, :]
        X[:, i+1] = X[:, i] + Y[:,i+1]
    
    left = np.mean((X[:, -1] >= a) * np.exp(-la2 * np.sum(X[:, :-1], axis = 1)))
    right_theorique = np.exp(n*(n-1)*(2*n-1)**(la2 ** 2) / 12)
    est2_theorique = left * right_theorique
    est_2 = left * right
    
    Stock[i, 3] = est2_theorique
    Stock[i, 4] = est_2

plt.close(1)
    
 
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    