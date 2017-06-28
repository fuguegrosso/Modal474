import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
plt.close()

K=1.
N=int(5e4)
ns=np.arange(99,N,100) # entiers espaces de 100
nbriter_max=1e2
eps=5e-2


#Notons que la formule choisie pour f s'applique aussi dans le cas ou x est un vecteur
def f(x):
    y=np.exp(x)-K
    return .5*(abs(y)+y)



# Calcul de Mn(0) en des valeurs theta definies par ns  
# et trace en bleu
G=np.random.randn(N)
M=np.cumsum(f(G))/np.arange(1,N+1)
plt.plot(ns,M[ns-1],"b",label="M_n(0)")



def Vn(n,theta):
    return np.exp(theta**2/2)*np.mean(f(G[:n])**2*np.exp(-theta*G[:n]))
        
def absGn(n,theta):
    return np.exp(theta**2/2)*abs(np.mean(f(G[:n])**2*(theta-G[:n])*np.exp(-theta*G[:n])))
        
def UpdateT(n,theta):
    return np.sum(f(G[:n])**2*(theta**3+(1.-2.*theta**2)*G[:n]+theta*G[:n]**2)*np.exp(-theta*G[:n]))/np.sum(f(G[:n])**2*(1.+(theta-G[:n])**2)*np.exp(-theta*G[:n]))

def FctM(n,theta):
    return np.exp(-theta**2/2)*np.mean(f(G[:n]+theta)*np.exp(-theta*G[:n]))




# pour differentes valeurs de n
# on calcule la limite du Newton perturbe et puis on evalue M en ce point
Madapt=[]
T=0. 
for n in ns: 
    k=0                               
    while ((absGn(n,T)>eps) & (k < nbriter_max)):
        T=UpdateT(n,T)
        k+=1
    Madapt.append(FctM(n,T))
    
# On trace l evolution de M
plt.plot(ns,Madapt,"g",label="M_n(theta_n)")
# on compare a la vraie valeur
theoricalexp=np.exp(.5)*norm.cdf(1-np.log(K))-K*norm.cdf(np.log(K))
plt.axhline(theoricalexp, color="r") 

plt.xlabel("n")

#plt.legend(loc="lower right")

plt.show()