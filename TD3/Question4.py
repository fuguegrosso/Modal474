# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

a = 6.

theta = a

n = int(1e6)

ech = np.random.randn(n)

##Monte-Carlo Classique
p_emp_MC = np.mean(ech>a)

erreur_MC = 1.96*np.sqrt(p_emp_MC*(1-p_emp_MC)/n) 

##Importance sampling
ech_IS = ((ech+theta)>a) * np.exp(-theta*ech)

p_emp_IS = np.mean(ech_IS)*np.exp(-(theta**2)/2)

moment2_emp_IS = np.mean(ech_IS*ech_IS)*np.exp(-theta**2)

erreur_emp_IS = 1.96*np.sqrt(moment2_emp_IS - p_emp_IS**2)/np.sqrt(n)

p_theorique = 1-norm.cdf(a)

print "Proba theorique = %1.3e \n" %p_theorique

print "Proba empirique naive = %1.3e, (intervalle de confiance : +/-%1.3e)" %(p_emp_MC,erreur_MC)
print "Erreur relative*100 = %1.2f \n" %(100*2*erreur_MC/p_theorique)

print "Proba empirique avec IS = %1.3e, (intervalle de confiance : +/- %1.3e)" %(p_emp_IS, erreur_emp_IS)
print "Erreur relative*100 = %1.2f \n" %(100*2*erreur_emp_IS/p_theorique)
