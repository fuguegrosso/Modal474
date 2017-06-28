import numpy as np
from numpy import sqrt as sqrt
import scipy.stats as sps

###############################################################################
## Question 2.1 
###############################################################################
print "-" * 40
print "Question 2.1"
print "-" * 40


n = 1000
sigma = 2.

X = np.random.randn(n)
X = sigma*X

xSquare = X*X
sumSquare = np.sum(xSquare)

###############################################################################
## IC non asymptotique
###############################################################################

# Quantiles de la loi chi^2(n-1) de niveau 0.975 et 0.025
quantileHaut = sps.chi2.ppf(q=0.975, df=n)
quantileBas = sps.chi2.ppf(q=0.025, df=n)

ICnonAsymptotique = (sqrt(sumSquare/quantileHaut), sqrt(sumSquare/quantileBas))

print "Vraie valeur de sigma:", sigma, "\n"
print "Taille de l'echantillon:" , n, "\n"
print "Intervalle de confiance non asymptotique [{:1.3f},{:1.3f}],".format(ICnonAsymptotique[0],ICnonAsymptotique[1]), \
        "de largeur {:1.3f} \n".format(ICnonAsymptotique[1]-ICnonAsymptotique[0])

###############################################################################
## IC asymptotique
###############################################################################
meanSquare = sumSquare/n
estimSigma = sqrt(meanSquare)

rayonIC = 1.96*estimSigma/sqrt(2*n)

print "Valeur estimee par moyenne empirique: {:1.2f} \n".format(estimSigma)
print "Intervalle de confiance asymptotique [{:1.4f},{:1.4f}],".format(estimSigma-rayonIC, 
    estimSigma+rayonIC), "de largeur {:1.3f} \n".format(2*rayonIC)