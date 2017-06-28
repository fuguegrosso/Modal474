import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
plt.close()

d=5
K=1.
N=int(1e3)
Nech=int(1e3)
nbriter_max=5e1
eps=1e-1

def f(x):
    y=np.mean(np.exp(x),axis=0)-K
    return .5*(abs(y)+y)
#Notons que la formule choisie pour f s'applique aussi dans le cas ou x est un vecteur
    
    
    
    
G=np.random.randn(d,N,Nech)
M=np.mean(f(G),axis=0)
plt.hist(M,bins=round(np.sqrt(Nech)), histtype="step", normed=True,color="blue")
x=np.linspace(np.min(M),np.max(M),1000)
plt.plot(x, norm.pdf(x,loc=np.mean(M), scale=np.std(M)), "b--")


def Vn(n,theta):
    return np.exp(np.inner(theta,theta)/2)*np.mean(f(G[:,:,n])**2*np.exp(-np.dot(theta,G[:,:,n])))
        
def Gn(n,theta):
    thetaP=np.reshape([theta]*N,(N,d)).T #duplique theta dans les colonnes d'une matrice de taille d x N
    return np.exp(np.inner(theta,theta)/2)*np.mean(f(G[:,:,n])**2*(thetaP-G[:,:,n])*np.exp(-np.dot(theta,G[:,:,n])), axis=1)
    
def Hn(n,theta):
    return np.exp(np.inner(theta,theta)/2)*np.mean(\
    np.array([f(G[:,i,n])**2*( np.eye(d)+np.matrix(theta-G[:,i,n]).T*np.matrix(theta-G[:,i,n]) )*np.exp(-np.inner(theta,G[:,i,n])) for i in range(N)])\
    , axis=0)#ici, le recours a la boucle pourrait etre evitable en calculant une fois pour toute la liste des np.matrix(G[:,i,:]).T*np.matrix(G[:,i,:]) 
    #(avec une boucle, mais realisee une seule fois dans l'ensemble du programme)
        
def UpdateT(n,theta):
    return theta-np.reshape(np.array(np.linalg.inv(Hn(n,theta))*np.matrix(Gn(n,theta)).T),d)

def FctM(n,theta):
    thetaP=np.reshape([theta]*N,(N,d)).T #duplique theta dans les colonnes d'une matrice de taille d x N
    return np.exp(-np.inner(theta,theta)/2)*np.mean(f(G[:,:,n]+thetaP)*np.exp(-np.dot(theta,G[:,:,n])))






Madapt=[]
T=np.zeros(d)

for n in range(Nech):
    k=0                               
    while ((np.linalg.norm(Gn(n,T))>eps) & (k < nbriter_max)):
        T=UpdateT(n,T)
        k+=1
    Madapt.append(FctM(n,T))

plt.hist(np.array(Madapt),bins=round(np.sqrt(Nech)), histtype="step", normed=True,color="green")
x=np.linspace(np.min(Madapt),np.max(Madapt),1000)
plt.plot(x, norm.pdf(x,loc=np.mean(np.array(Madapt)),scale=np.std(np.array(Madapt))), "g--")

if d==1:
    theoricalexp=np.exp(.5)*norm.cdf(1-np.log(K))-K*norm.cdf(np.log(K))
    plt.axvline(theoricalexp, color="r")

plt.show()