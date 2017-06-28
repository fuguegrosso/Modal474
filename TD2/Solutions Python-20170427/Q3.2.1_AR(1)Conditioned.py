# -*- coding: utf-8 -*-
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sps

##nombre de tirages
n = int(5e3)

rho=0.99
tau=np.sqrt(1-rho**2)

#Loi conditionnelle cible: Loi de X|X>a pour
a=.8

## On fait un premier tirage de la loi de X|X>a
X=np.random.randn(1)

while X[0]<=a:
    X=np.random.randn(1)

## Simulation du processus AR(1) conditionnel
Y=np.random.randn(n)

for i in range(int(n)):
    newX = rho*X[-1]+tau*Y[i]
    X = np.append(X,newX*(newX>a) + X[-1]*(newX<=a))

MinX, MaxX = a, max(X)
L = MaxX-MinX
sigma = np.sqrt(np.var(X))


#Choix du nombre de colonnes:   
N = round(n**(1./3.)*L/(3.49*sigma))

#Densité conditionnelle
x = np.linspace(MinX, MaxX, 100)
f_x = sps.norm.pdf(x)/sps.norm.sf(a)
plt.plot(x, f_x, "r", linewidth=1.5, label="Densite conditionnelle")

#Affichage histogramme
plt.hist(X, bins=N, normed=True,histtype='step',label="Histogramme")

#On choisit la position de la legende
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2, fancybox=True, shadow=True)
plt.show()

