import numpy as np
import scipy.stats as sps

###############################################################################
## Question 1.5
###############################################################################
print "-" * 40
print "Question 1.5 Cas Gaussien"
print "-" * 40

##nombre de simulations de X
n = 1000
##nombre de repetitions de l'estimation (pour IC)
m = 100
X = np.random.randn(m,n)
X.sort(axis=1)

#Vraie valeur de la VaR
alpha = 1.e-2
##on pourra diminuer alpha jusqu'a 1.e-6, 1.e-7...
u = 1-alpha
Q_u = sps.norm.ppf(u)

#quantiles empiriques
Q_n_u = np.array(X[:,int(np.ceil(n*u))-1])

#Intervalle de confiance
sigmaSquare = sum(Q_n_u*Q_n_u)/np.double(m) - (sum(Q_n_u)/np.double(m))**2
sigma = np.sqrt(sigmaSquare)
# On peut aussi prendre sigma=np.std(Q_n_u)
rayonIntervalleConfiance = 1.96*sigma

#Un peu de formattation de l'affichage
print "Vraie VaR au niveau alpha={:1.4f}: {:1.4f} \n".format(alpha, Q_u)
##la commade %1.xf permet de choisir le nombre de chiffres significatives
print "Valeur estimee et demi largeur de l'intervalle de confiance: {:1.4f} +- {:1.4f} \n" .format(Q_n_u[0],rayonIntervalleConfiance)

flag = np.logical_and(Q_u < Q_n_u[0]+rayonIntervalleConfiance, Q_n_u[0]+rayonIntervalleConfiance)
print "Vraie valeur dans l'intervalle: " ,flag, "\n"

print "Erreur relative*100: {:1.4f} \n".format(rayonIntervalleConfiance*100/Q_u)

print "-" * 40
print "Question 1.5 Cas Gamma"
print "-" * 40

##Parametres de la loi Gamma
shape=2
scale=3
print "Parametres de la Gamma : shape={}, scale={}\n".format(shape,scale)

##nombre de simulations de X
n = 1000
##nombre de repetitions de l'estimation (pour IC)
m = 100
X = np.random.gamma(shape,scale=scale,size=(m,n))
X.sort(axis=1)

#Vraie valeur de la VaR
alpha = 1.e-2
##on pourra diminuer alpha jusqu'a 1.e-6, 1.e-7...
u = 1-alpha
Q_u = sps.gamma.ppf(u,shape,scale=scale)

#quantiles empiriques
Q_n_u = np.array(X[:,int(np.ceil(n*u))-1])

#Intervalle de confiance
sigmaSquare = sum(Q_n_u*Q_n_u)/np.double(m) - (sum(Q_n_u)/np.double(m))**2
sigma = np.sqrt(sigmaSquare)
# On peut aussi prendre sigma=np.std(Q_n_u)
rayonIntervalleConfiance = 1.96*sigma

#Un peu de formattation de l'affichage
print "Vraie VaR au niveau alpha={:1.4f}: {:1.4f} \n".format(alpha, Q_u)
##la commade %1.xf permet de choisir le nombre de chiffres significatives
print "Valeur estimee et demi largeur de l'intervalle de confiance: {:1.4f} +- {:1.4f} \n" .format(Q_n_u[0],rayonIntervalleConfiance)

flag = np.logical_and(Q_u < Q_n_u[0]+rayonIntervalleConfiance, Q_n_u[0]+rayonIntervalleConfiance)
print "Vraie valeur dans l'intervalle: " ,flag, "\n"

print "Erreur relative*100: {:1.4f} \n".format(rayonIntervalleConfiance*100/Q_u)