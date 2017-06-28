import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
plt.close()

K=1.

n = int(1e4)

theta_min, theta_max=-1.,4.
Theta=np.linspace(theta_min, theta_max,100)
nbriter_max=100
eps=.05

def f(x):
    y=np.exp(x)-K
    return .5*(abs(y)+y)
    
# Notons que la formule choisie pour f s'applique aussi dans le cas ou x est un vecteur
   
   
   
G=np.random.randn(n)

def Vn(theta):
    return np.exp(theta**2/2)*np.mean(f(G)**2*np.exp(-theta*G))
    
def absGn(theta):
    return np.exp(theta**2/2)*abs(np.mean(f(G)**2*(theta-G)*np.exp(-theta*G)))
    
    
def UpdateT(theta):
    return np.sum(f(G)**2*(theta**3+(1.-2.*theta**2)*G+theta*G**2)*np.exp(-theta*G))/np.sum(f(G)**2*(1.+(theta-G)**2)*np.exp(-theta*G))


# On produit la suite de Newton bruitee, pour nbrinter_max iterations max et tant que le gradient est trop eleve
T=[3.]    
while ((absGn(T[-1])>eps) & (len(T) < nbriter_max)):
    T.append(UpdateT(T[-1]))
    
    
# Evaluation de la fonction Vn sur un intervalle
# et trace
Y=[Vn(theta) for theta in Theta]
plt.plot(Theta, Y, "b")
# Evolution de la suite de Newton bruitee
plt.plot(T,[Vn(t) for t in T], "r.")

# Affichage du critere d arret
print 'Valeur du gradient en le point final \n' +str(absGn(T[-1]))
print 'Nombre d iterations avant arret \n' + str(len(T))
print 'Valeur limite de la suite \n'+str(T[-1])
plt.show()