import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
plt.close()

d=2
K=1.
N=int(1e5)
ns=np.arange(99,N,100)
nbriter_max=5e1
eps=1e-1



def f(x):
    y=np.mean(np.exp(x),axis=0)-K
    return .5*(abs(y)+y)
    
#Notons que la formule choisie pour f s'applique aussi dans le cas ou x est un vecteur
    
G=np.random.randn(d,N)
M=np.cumsum(f(G))/np.arange(1,N+1)
plt.plot(ns,M[ns-1],"b",label="M_n(0)")




def Vn(n,theta):
    return np.exp(np.inner(theta,theta)/2)*np.mean(f(G[:,:n])**2*np.exp(-np.dot(theta,G[:,:n])))
        
def Gn(n,theta):
    thetaP=np.reshape([theta]*n,(n,d)).T #duplique theta dans les colonnes d'une matrice de taille d x n
    return np.exp(np.inner(theta,theta)/2)*np.mean(f(G[:,:n])**2*(thetaP-G[:,:n])*np.exp(-np.dot(theta,G[:,:n])), axis=1)
    
def Hn(n,theta):
    return np.exp(np.inner(theta,theta)/2)*np.mean(\
    np.array([f(G[:,i])**2*( np.eye(d)+np.matrix(theta-G[:,i]).T*np.matrix(theta-G[:,i]) )*np.exp(-np.inner(theta,G[:,i])) for i in range(n)])\
    , axis=0) #ici, le recours a la boucle pourrait etre evitable en calculant une fois pour toute la liste des np.matrix(G[:,i]).T*np.matrix(G[:,i]) 
    #(avec une boucle, mais realisee une seule fois dans l'ensemble du programme)
        
def UpdateT(n,theta):
    return theta-np.reshape(np.array(np.linalg.inv(Hn(n,theta))*np.matrix(Gn(n,theta)).T),d)

def FctM(n,theta):
    thetaP=np.reshape([theta]*n,(n,d)).T #duplique theta dans les colonnes d'une matrice de taille d x n
    return np.exp(-np.inner(theta,theta)/2)*np.mean(f(G[:,:n]+thetaP)*np.exp(-np.dot(theta,G[:,:n])))



Madapt=[]
T=np.zeros(d)

for n in ns+1:
    k=0                               
    while ((np.linalg.norm(Gn(n,T))>eps) & (k < nbriter_max)):
        T=UpdateT(n,T)
        k+=1
    Madapt.append(FctM(n,T))

plt.plot(ns,Madapt,"g",label="M_n(theta_n)")

if d==1:
    theoricalexp=np.exp(.5)*norm.cdf(1-np.log(K))-K*norm.cdf(np.log(K))
    plt.axhline(theoricalexp, color="r") 

plt.xlabel("n")

plt.show()