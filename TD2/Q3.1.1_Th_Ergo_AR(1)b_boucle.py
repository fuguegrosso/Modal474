# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sps



##horizon de temps
n = int(5e3)

rho=.7
tau=np.sqrt(1-rho**2)


Y=np.random.randn(n)

X=np.random.randn(1)
    

for i in range(n):
    X = np.append(X, rho*X[-1] + tau*Y[i])


MinX, MaxX=min(X), max(X)
L=MaxX-MinX

#Choix du nombre de colonnes
N=round(n**(1./3.)*L/3.49)


#Densité
x = np.linspace(MinX,MaxX,1000)
f_x = sps.norm.pdf(x)
plt.plot(x,f_x,"r",linewidth=1.0,label="Densite gaussienne")

#Affichage histo
plt.hist(X, bins=N, normed=True,histtype='step',label="Histogramme")

 

#On choisit la position de la legende
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2, fancybox=True, shadow=True)
plt.show()

