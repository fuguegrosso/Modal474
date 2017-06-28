# -*- coding: utf-8 -*-
import numpy  as np
import  matplotlib.pyplot as plt
import scipy.stats as sps

la = 1.0
T = 1.0
alpha = 0.5
esperance = la*T*alpha
variance = la*T*alpha**2
rho = 5; # 1, 5, 20

x = esperance + rho*np.sqrt(variance)

thetax = np.log(x/esperance)/alpha

GammaT = la*T*(np.exp(alpha*thetax) - 1)


# nombre max de points dans la somme de MC
NbrMax =  int(2e5)
# nombre de réalisations independantes de l'estimateur
NbrEstim = int(1e2)

estim_mc = np.zeros((NbrEstim, NbrMax))
estim_is = np.zeros((NbrEstim, NbrMax))

for n_iter in np.arange(NbrEstim):
    # Tirer des Poisson, cas MC et cas IS
    N_mc = np.random.poisson(lam=la*T, size=(1,NbrMax))
    N_is = np.random.poisson(lam=la*T*np.exp(alpha*thetax), size=(1,NbrMax))
    
    # cas IS : calculer le ratio d'importance
    ratio_is = np.exp(-thetax*alpha*N_is + GammaT)
    
    # Calcul des estimateurs
    seuil = x/alpha

    estim_mc[n_iter,:] = np.cumsum(N_mc>seuil) / np.arange(1,NbrMax+1,dtype=float)
    
    estim_is[n_iter,:] = np.cumsum(ratio_is*(N_is>seuil)) / np.arange(1,NbrMax+1,dtype=float)

##############################
# Affichage d'une trajectoire
##############################
plt.figure(1)
plt.plot(estim_mc[1,:],'b', linewidth=2.)
plt.plot(estim_is[1,:],'r', linewidth=2.)

valeur_theorique = sps.poisson.sf(x/alpha,mu=la*T)
plt.hlines(valeur_theorique, 0, NbrMax, 'g', linewidth=2.)

plt.title("Valeur de rho :" + str(rho))
plt.legend(['Monte Carlo','Imp Sampl'], loc="best")
plt.xlabel("M")
plt.grid()

############################
# Affichage des boxplots
############################
plt.figure(2)
M1, M2, M3 = int(1e2),int(1e4),int(NbrMax)

bloc1 = np.transpose(estim_mc[:,[M1-1,M2-1,M3-1]])
bloc2 = np.transpose(estim_is[:,[M1-1,M2-1,M3-1]])
bloc = np.concatenate((bloc1,bloc2))

plt.hlines(valeur_theorique, 0, NbrMax, 'g', linewidth=2.)
plt.title(str(NbrEstim)+" estim.,  M = "+str(M1)+', '+str(M2)+', '+str(M3))
plt.boxplot(np.transpose(bloc[[0,3,1,4,2,5],:]), positions=[1,2,4,5,7,8], labels = ['MC','IS','MC','IS','MC','IS'])
plt.ylim(0,4*valeur_theorique)

plt.show()