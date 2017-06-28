import numpy as np
from numpy import sqrt as sqrt
import scipy.stats as sps

###############################################################################
## Question 2.2
###############################################################################
print "-" * 20
print "Question 2.2"
print "-" * 20

n = 10000
sigma = 1.
X = np.random.randn(n)
X = sigma*X

#Vraie valeur quantile 
u = 0.9999
Q_u = sps.norm.ppf(u, loc=0, scale=sigma)

############################################################
## Estimation de sigma + inversion de la fct de repartition
############################################################
print "-" * 60
print "Estimation de sigma + inversion de F(x,sigma)"
print "-" * 60

xSquare = X*X
meanSquare = np.mean(xSquare)
meanSigma = sqrt(meanSquare)

quantile = sps.norm.ppf(u, loc=0, scale=meanSigma)

rayonIC2 = 1.96*quantile/sqrt(2*n)

print "u:", u
print "Vraie valeur du quantile Q(u): {:1.4f}".format(Q_u)
print "Taille de l'echantillon: " , n, "\n"

print "Quantile par estimation de sigma: {:1.4f} \n".format(quantile)
print "Intervalle de confiance [{:1.4f},{:1.4f}]".format(quantile-rayonIC2,quantile+rayonIC2), "de demi largeur {:1.3f}".format(rayonIC2)
print "Vraie valeur dans l'IC: ", (quantile-rayonIC2 < Q_u) and (quantile < Q_u+rayonIC2)
print "Erreur relative(%):", rayonIC2/Q_u*100, "\n"

###################################################
## Quantile empirique
###################################################
print "-" * 60
print "Quantile empirique"
print "-" * 60

X.sort()
Q_u_n = X[int(np.ceil(n*u))-1]

s = sqrt(u*(1.-u))/sps.norm.pdf(Q_u, loc=0, scale=sigma)
rayonIC_quantileEmpirique = 1.96*s/sqrt(n)

print "Quantile empirique: {:1.4f} \n".format(Q_u_n)
print "Intervalle de confiance [{:1.4f},{:1.4f}]".format(Q_u_n-rayonIC_quantileEmpirique,Q_u_n+rayonIC_quantileEmpirique), ", de demi largeur {:1.3f}".format(rayonIC_quantileEmpirique)
print "Vraie valeur dans l'IC: ", (Q_u_n-rayonIC_quantileEmpirique < Q_u) and (Q_u < Q_u_n+rayonIC_quantileEmpirique)
print "Erreur relative(%):", rayonIC_quantileEmpirique/Q_u*100, "\n"

###################################################
## On peut aussi verifier le calcul de la variance
## dans le TCL pour Q(u,sigma_n)
###################################################
testFlag = 0
if testFlag:
	m = 2000
	X = np.random.randn(m,n)
	X = sigma*X
	
	xSquare = X*X
	meanSquare = np.mean(xSquare, axis=1)
	meanSigma = sqrt(meanSquare)

	quantiles = np.zeros(m)
	for i, sigmaValue in enumerate(meanSigma):
		quantiles[i] = sps.norm.ppf(u, loc=0, scale=sigmaValue)

	from pylab import plot,hist,show
	
	erreurNormalisee = sqrt(2*n)*(quantiles - Q_u)/Q_u
	x = np.linspace(-5,5,100)
	densiteGaussienne = sps.norm.pdf(x)
	plot(x, densiteGaussienne, linewidth=1.5)
	hist(erreurNormalisee,bins=int(sqrt(m)),normed="true")
	show()