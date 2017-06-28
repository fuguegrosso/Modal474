# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sps

##taille de l'echantillon
n = int(5e3)

##gaussiennes centrees reduites
X = np.random.randn(n)
MinX, MaxX = min(X), max(X)
L = MaxX-MinX

#Choix du nombre de colonnes: (dé)commenter selon son choix 
#N trop faible
N=round(n**(1./8.)*L/3.49)

#N trop élevé
#N=round(n**(5./8.)*L/3.49)

#N optimal
#N=round(n**(1./3.)*L/3.49)

#Densité
x = np.linspace(MinX, MaxX, 1000)
f_x = sps.norm.pdf(x)
plt.plot(x, f_x, "r", linewidth=1.0, label="Densite gaussienne")

#Affichage histogramme
plt.hist(X, bins=N, normed=True, histtype='step', label="Histogramme")

#On choisit la position de la legende
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2, fancybox=True, shadow=True)
plt.show()