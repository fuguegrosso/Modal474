# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sps



##horizon de temps
n = int(5e2)

rho=.7
tau=np.sqrt(1-rho**2)

##gaussiennes centrees reduites
Y = np.random.randn(n)

X = tau*np.cumsum(np.append([0], Y*(rho**(-np.arange(1,n+1)))))

X+=np.random.randn(1)

X *= rho**np.arange(n+1)

MinX, MaxX = min(X), max(X)
L=MaxX-MinX

#Choix du nombre de colonnes
N=round(n**(1./3.)*L/3.49)


#Densité 
x = np.linspace(MinX,MaxX,1000)
f_x = sps.norm.pdf(x)
plt.plot(x,f_x,"r",linewidth=1.0,label="Densite gaussienne")

##Affichage histo
plt.hist(X, bins=N, normed=True,histtype='step',label="Histogramme")

plt.axvline(x=X[0], color="g",linewidth=1.5, label="X_0")

#On choisit la position de la legende
plt.legend(bbox_to_anchor=(0.5, -0.05), ncol=2, fancybox=True, shadow=True)
plt.show()

