import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

a = 6.0
theta = a
n = int(1E6)

X = np.random.randn(n)

p_MC = np.mean(X > a)

e_MC = 1.96 * np.sqrt(p_MC * (1 - p_MC) / n)

X_IS = ((X + theta) > a) * np.exp(- theta * X)

p_IS = np.mean(X_IS) * np.exp(- theta ** 2 / 2.)

d = np.mean(p_IS * p_IS) * np.exp(- theta ** 2) - p_IS ** 2

e_IS = 1.96 * np.sqrt(d / n)

p_theorique = 1 - norm.cdf(a)

print "Proba theorique = %1.3e \n" %p_theorique

print "Proba empirique naive = %1.3e, (intervalle de confiance : +/-%1.3e)" %(p_MC,e_MC)
print "Erreur relative*100 = %1.2f \n" %(100*2*e_MC/p_theorique)

print "Proba empirique avec IS = %1.3e, (intervalle de confiance : +/- %1.3e)" %(p_IS, e_IS)
print "Erreur relative*100 = %1.2f \n" %(100*2*e_IS/p_theorique)