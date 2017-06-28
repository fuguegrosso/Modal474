# -*- coding: utf-8 -*-
import numpy as np
import  matplotlib.pyplot as plt
import time

############;###################################################################
## Question 9
###############################################################################
plt.close()

C = 100.0
Lambda  = 30.0
T = 1.0
alpha = 30.0
la = 0.05
pVecteur = [0.1, 0.5, 0.9]
length_p = len(pVecteur)
K = 8

# Nombre de réalisations indépendantes de l'estimateur
NbrAlgo = 3
# Longueur de la chaîne pour chacun des niveaux
LengthTrajVecteur = [1.5e5, 8e4, 1.5e5]

# calcul des seuils successifs
BoundSplit = C*(1-((np.arange(K,dtype=float)+1)**2/K**2))
print("les seuils successifs envisagés pour le splitting sont \t")
print(BoundSplit)


TempsDepart = time.time()

StockProbaEnd = np.zeros((length_p,NbrAlgo))
# Boucle sur les valeurs de p
for n_p in np.arange(length_p):
     p = pVecteur[n_p]
     LengthTraj = LengthTrajVecteur[n_p]
     print("Lorsque p = "+ str(p) +" et lambda = " + str(la))   
     plt.clf()
     
     # Boucle sur les differents runs independants
     for n_algo in np.arange(NbrAlgo):
        print("Run "+ str(n_algo+1))
        
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
        plt.plot(Frequence/(np.arange(LengthTraj+1)+1)) 
            
        ## BOUCLE pour les AUTRES NIVEAUX
        for n_level in (1+np.arange(K-1)):
            print("\t Chaine "+ str(n_level+1))
            Frequence = np.zeros(LengthTraj+1)
            RateAccept = np.zeros(LengthTraj+1)
            PathPoisson = PathPoissonInit
            MinPath = np.zeros(LengthTraj+1)
            MinPath[0] = min(C+Lambda*np.concatenate([np.arange(1),PathPoisson])-alpha*np.arange(len(PathPoisson)+1))
            for n_chain in np.arange(LengthTraj):
                # Nombre de sauts dans le processus courant
                J = len(PathPoisson)
                # Quels sauts sont conserves
                JumpConserve = PathPoisson[np.random.uniform(0,1,size=J)<=p]
                # Combien en ajoute-t-on
                NbrAjoute = np.random.poisson((1-p)*la*T)
                # Instants de sauts ajoutés
                NewJump = T*np.random.uniform(0,1,NbrAjoute)
                # Processus candidat à être la nouvelle valeur de la chaine
                NewPathPoisson = np.sort(np.concatenate([NewJump,JumpConserve]))
                # Acceptation-rejet de ce candidat
                NewReserve = C+Lambda*np.concatenate([np.arange(1),NewPathPoisson])-alpha*np.arange(len(NewPathPoisson)+1)
                if min(NewReserve)<=BoundSplit[n_level-1]:    # on accepte
                    PathPoisson = NewPathPoisson    # mise à jour de la chaine
                    MinPath[n_chain+1] = min(NewReserve)    # stockage valeur minimale
                    RateAccept[n_chain+1] = RateAccept[n_chain]+1   # update du taux d'acceptation-rejet
                else:       # on refuse
                    MinPath[n_chain+1] = MinPath[n_chain]   #   stockage valeur minimale
                    RateAccept[n_chain+1] = RateAccept[n_chain] # update du taux d'acceptation-rejet
                # Calcul de l'estimateur de la probabilité
                if MinPath[n_chain+1]<=BoundSplit[n_level]:
                    Frequence[n_chain+1] = Frequence[n_chain]+1
                    PathPoissonInit = PathPoisson
                else:
                    Frequence[n_chain+1] = Frequence[n_chain]
            # Affichage
            NewProbaEnd = Frequence[-1]/LengthTraj
            ProbaEnd = ProbaEnd*NewProbaEnd
            print ("\t Pour le niveau " + str(n_level) +", la proba estimée est " + str(NewProbaEnd))    
            # Visualisation de la consistance de l'estimateur
            plt.figure(1)
            plt.plot(Frequence/(np.arange(LengthTraj+1)+1))  
            # Visualisation de l'évolution du taux d'acceptation-rejet
            plt.figure(2)
            plt.plot(RateAccept/(np.arange(LengthTraj+1)+1)) 
                    
        plt.figure(1)
        plt.title("Consistance des estimateurs des probabilites")
        plt.grid()
        plt.figure(2)
        plt.title("Evolution du taux d'acceptation-rejet")
        plt.grid()
    
        # Calcul de l'estimateur 
        print("Run "+ str(n_algo+1)+": la proba de ruine estimée est " + str(ProbaEnd))
        StockProbaEnd[n_p,n_algo] = ProbaEnd
    
    
plt.figure(3)
plt.title("Boxplot de " + str(NbrAlgo) +" estimateurs independants")
plt.boxplot(np.transpose(StockProbaEnd), positions=[1,3,5], labels = ['p=0.1','p=0.5','p=0.9'])

plt.figure(4)
M = np.mean(StockProbaEnd, axis=1)
S = np.std(StockProbaEnd, axis=1)
plt.plot(pVecteur, S/M, 'd-')
plt.xlabel("valeur de p", fontsize=15)
plt.ylabel("ratio ecart type/moyenne", fontsize=15)
plt.grid()

TempsFin = time.time()
print("Durée d'exécution "+str(TempsFin-TempsDepart))