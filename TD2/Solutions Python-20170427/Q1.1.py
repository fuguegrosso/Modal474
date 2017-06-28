import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sps

###############################################################################
## Question 1.1
###############################################################################
print "-" * 40
print "Question 1.1 Cas Gaussien"
print "-" * 40

##nombre de simulations
n = 1000
##gaussiennes centrees reduites
X = np.random.randn(n)

plt.figure(1)
plt.close()
#Fct de repartition 
x = np.linspace(min(X),max(X),100)
F_x = sps.norm.cdf(x)
plt.plot(x, F_x, "r", linewidth=1.0, label="Fct de rep gaussienne")

#Affichage de la fct de repartition empirique
X.sort()
F_x_n = np.arange(1,n+1,dtype=np.double)/n
plt.step(X, F_x_n, "b", label="Fct de rep empirique")

#On choisit la position de la legende
plt.legend(loc=4)
plt.show()


print "-" * 40
print "Question 1.1 Cas Gamma"
print "-" * 40

##nombre de simulations
n = 1000
##Parametres de la loi Gamma
shape=2
scale=3
print "Parametres de la Gamma : shape={}, scale={}\n".format(shape,scale)

X = np.random.gamma(shape,scale=scale,size=n)

plt.figure(1)
plt.close()
#Fct de repartition 
x = np.linspace(min(X),max(X),100)
F_x = sps.gamma.cdf(x,shape,scale=scale)
plt.plot(x, F_x, "r", linewidth=1.0, label="Fct de rep gaussienne")

#Affichage de la fct de repartition empirique
X.sort()
F_x_n = np.arange(1,n+1,dtype=np.double)/n
plt.step(X, F_x_n, "b", label="Fct de rep empirique")

#On choisit la position de la legende
plt.legend(loc=4)
plt.show()


