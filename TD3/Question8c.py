import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
plt.close()

K=1.
N=int(5e3)
Nech=int(1e3)
nbriter_max=1e2
eps=5e-2

def f(x):
    y=np.exp(x)-K
    return .5*(abs(y)+y)
#Notons que la formule choisie pour f s'applique aussi dans le cas ou x est un vecteur
    
    
    
    
# PLusieurs realisation de M(0)
# et trace de l histogramme
G=np.random.randn(Nech,N)
M=np.mean(f(G), axis=1)
plt.hist(M,bins=round(np.sqrt(Nech)), histtype="step", normed=True,color="blue")

# on ajuste une densite gaussienne 
x=np.linspace(np.min(M),np.max(M),1000)
plt.plot(x, norm.pdf(x,loc=np.mean(M), scale=np.std(M)), "b--")



def Vn(n,theta):
    return np.exp(theta**2/2)*np.mean(f(G[n,:])**2*np.exp(-theta*G[n,:]))
        
def absGn(n,theta):
    return np.exp(theta**2/2)*abs(np.mean(f(G[n,:])**2*(theta-G[n,:])*np.exp(-theta*G[n,:])))
        
def UpdateT(n,theta):
    return np.sum(f(G[n,:])**2*(theta**3+(1.-2.*theta**2)*G[n,:]+theta*G[n,:]**2)*np.exp(-theta*G[n,:]))/np.sum(f(G[n,:])**2*(1.+(theta-G[n,:])**2)*np.exp(-theta*G[n,:]))

def FctM(n,theta):
    return np.exp(-theta**2/2)*np.mean(f(G[n,:]+theta)*np.exp(-theta*G[n,:]))


# On repete Nech fois
# le calcul de theta, puis de M en ce theta
Madapt=[]
T=0.
for n in range(Nech):
    k=0                               
    while ((absGn(n,T)>eps) & (k < nbriter_max)):
        T=UpdateT(n,T)
        k+=1
    Madapt.append(FctM(n,T))
    

# on fait l histogramme
plt.hist(np.array(Madapt), bins=round(np.sqrt(Nech)), histtype="step", normed=True,color="green")
# on superpose une densite gaussienne
x=np.linspace(np.min(Madapt),np.max(Madapt),1000)
plt.plot(x, norm.pdf(x,loc=np.mean(np.array(Madapt)),scale=np.std(np.array(Madapt))), "g--")


# on calcule la moyenne theorique et ila trace
theoricalexp=np.exp(.5)*norm.cdf(1-np.log(K))-K*norm.cdf(np.log(K))
plt.axvline(theoricalexp, color="r")

plt.show()