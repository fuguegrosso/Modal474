# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import scipy.stats as sps

a=5
seuil=0.1
rho=0.7
tau=np.sqrt(1-rho**2)

### Pour trouver les niveaux de splitting, on propose deux possibilites
##Possibilite 1

def estimation(b,a,rho,n): # Estime la probabilité que X>b sachant que X>a avec n variables
## On fait un premier tirage de la loi de X|X>a
    tau=np.sqrt(1-rho**2)
    X=np.random.randn(1)
    while X[0]<=a:
        X=np.random.randn(1)    
    ## Simulation du processus AR(1) conditionnel
    Y=np.random.randn(n)
    for i in range(int(n)):
        newX = rho*X[-1]+tau*Y[i]
        X = np.append(X,newX*(newX>a) + X[-1]*(newX<=a))
    return np.mean(X>b)
    
def TrouverNiveaux(a,seuil,rho,n): #Permet de trouver les niveaux de splitting approximatifs en utiliser (7)
##nombre de tirages
    av=[0]
    while 1:
        x=np.linspace(av[-1],a,10) #On subdivise l'intervalle qui reste juqu'a a en 10 sous-intervalles
        probas=np.array([estimation(z,av[-1],rho,n) for z in x])
       # print(probas[-1])
        if probas[-1]>seuil or probas[-1] >=a:
            break
        else:
            av.append(x[np.size(probas[probas>seuil])])
    av.append(a)
#[sps.norm.sf(av[i+1])/sps.norm.sf(av[i]) for i in range(len(av)-1)]
    av=av[1:]
    return av
    

## Possibilite 2 en utilisant la section 1
def TrouverNiveauxBis(a,seuil,rho,n): 
##nombre de tirages
    av=[-5]
    while av[-1]<a:
        tau=np.sqrt(1-rho**2)
        X=np.random.randn(1)
        while X[0]<=av[-1]:
            X=np.random.randn(1)
    ## Simulation du processus AR(1) conditionnel
        Y=np.random.randn(n)
        for i in range(int(n)):
            newX = rho*X[-1]+tau*Y[i]
            X = np.append(X,newX*(newX>av[-1]) + X[-1]*(newX<=av[-1]))
        X.sort()
        #print(X[np.ceil((1-seuil)*n)])
        av.append(X[int(np.ceil((1-seuil)*n))]) 
        avp=av[1:-1]
        avp.append(a)
    return avp
    
    
print "On trouve les niveaux de splitting approximatifs"
av=TrouverNiveaux(a,seuil,rho,100) 
#av=TrouverNiveauxBis(a,seuil,rho,100) 
print "Les niveaux de splitting sont "+str(av)
    

## On met en oeuvre le splitting

n = int(8e4)
Y = np.random.randn(n)
X = np.random.randn(1)

## Niveau 0: pas de rejet
for i in range(n):
    X = np.append(X, rho*X[-1]+tau*Y[i])
    
P = [np.mean(X>av[0])]   

## Niveau l pour l=1,..,k
k=len(av)
for l in range(1,k):
    aprime = av[l-1]
            
    ##on recupere la premiere valeur de la chaine au niveau l 
    ##qui depasse le niveau l+1:
    ##pour initialiser la chaine au niveau l+1
    startingPoint = X[X > aprime][0]
    
    X = np.array([startingPoint])
    Y = np.random.randn(n)

    for i in range(n):
        x = rho*X[-1] + tau*Y[i]
        X = np.append(X, x*(x>aprime) + X[-1]*(x<=aprime))
    
    P.append(np.mean(X>av[l]))

#Splitting method gives:    
Proba_emp_split = np.prod(P)

#Simple Monte Carlo gives:
Proba_emp_MonteCarlo = np.mean(np.random.randn(k*n)>a)

#Exact value
p=sps.norm.sf(a)

print "-"*40

print "Exact probability = "+str(p)

print "Splitting method gives = "+str(Proba_emp_split)

print "Simple Monte Carlo gives = "+str(Proba_emp_MonteCarlo)

print "-"*40

print "Splitting method relative error (percentage) = "+str(100*abs(Proba_emp_split-p)/p)

print "Simple Monte Carlo relative error (percentage) = "+str(100*abs(Proba_emp_MonteCarlo-p)/p)