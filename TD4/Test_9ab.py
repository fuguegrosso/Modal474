import numpy as np
import  matplotlib.pyplot as plt
import time

###############################################################################
## Question 9, pour un seul run de l'algo et une seule valeur de p
###############################################################################
plt.close()

C = 100.0
Lambda  = 30.0
T = 1.0
alpha = 30.0
la = 1
p = 0.5
K = 3

LengthTraj = 1e4

# calcul des seuils successifs
BoundSplit = C*(1-((np.arange(K,dtype=float)+1)**2/K**2))
print("Les seuils successifs envisagés pour le splitting sont \t")
print(BoundSplit); print("\n")


TempsDepart = time.time()

print("Lorsque p = "+ str(p) +" et lambda = " + str(la))   
plt.clf()
        
##----------
# NIVEAU 1
##----------
# Nombre de sauts sur [0,T], par points de la chaîne
NbrJump = np.random.poisson(lam=la*T,size=(1,LengthTraj))
Frequence = np.zeros(LengthTraj+1)
#Boucle pour simuler la chaine de Markov
print("\t Chaine 1")
for n_chain in np.arange(LengthTraj):
    # nombre de sauts du processus de Poisson courant
    jj = NbrJump[0,n_chain]
    TimeJump = np.sort(T*np.random.uniform(0,1,size=jj))
    Reserve = C+Lambda*np.concatenate([np.arange(1),TimeJump])-alpha*np.arange(jj+1)
    # on met a jour l'estimateur
    if min(Reserve)<=BoundSplit[0]:
        # on augmente le compteur
        Frequence[n_chain+1] = Frequence[n_chain]+1
        # on stocke ce point de la chaîne comme possible point de départ pour la chaine suivante
        PathPoissonInit = TimeJump
    else: 
        # on ne change pas le compteur
        Frequence[n_chain+1] = Frequence[n_chain]
#Affichage de l'estimateur de la proba pour ce niveau
ProbaEnd = Frequence[-1]/LengthTraj
print ("\t Pour le niveau 0, la proba estimée est " + str(ProbaEnd))
# Visualisation de la consistance de l'estimateur
plt.figure(1)
plt.plot(Frequence/(np.arange(LengthTraj+1)+1), label="niveau 1") 
plt.show()