import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


m = int(3e2)

n1 = int(1e5)

n2 = int(1e5)

a = 7.

Si = np.linspace(a/2, 3*a, m)

G = np.random.randn(n1)

V = []

for si in Si:
    V.append( np.mean( (si**2)*(abs(si*G)>a) * np.exp(-(si**2-1)*G*G) ) )
    
#Remarque : cette etape peut etre realisee sans boucle a l'aide d'un produit matriciel,
#mais on peut se heurter alors au probleme de la taille de la memoire (on doit en effet
#manipuler des matrices de taille n1 par n1)

## on determine le meilleur parametre dans la grille 
hat_si_star = Si[V.index(min(V))]
plt.plot(Si,V)

##on ne reutilise pas les n1 tirages deja faits
ech = np.random.randn(n2)

##Monte-Carlo classique
p_emp_MC = np.mean(abs(ech)>a)
erreur_MC = 1.96*np.sqrt(p_emp_MC*(1-p_emp_MC)/n2)

##IS avec hat_si_star
ech_IS = (abs(hat_si_star*ech)>a)*np.exp(-(hat_si_star**2-1)*ech*ech/2)
p_emp_ISsigmastar = hat_si_star*np.mean(ech_IS)
moment2_emp_ISsigmastar = hat_si_star*hat_si_star*np.mean(ech_IS*ech_IS)
erreur_emp_ISsigmastar = 1.96*np.sqrt(moment2_emp_ISsigmastar - p_emp_ISsigmastar**2) / np.sqrt(n2)


##IS avec Sigma = a
ech_ISa = (abs(ech)>1)*np.exp(-(a**2-1)*ech**2/2)
p_emp_ISa = a*np.mean(ech_ISa)
moment2_emp_ISa = a*a*np.mean(ech_IS*ech_IS)
erreur_emp_ISa = 1.96*np.sqrt(moment2_emp_ISa - p_emp_ISa**2) / np.sqrt(n2)

## Valeur theorique
p_theorique = 2*(1-norm.cdf(a))

print("\n"+"a = "+str(a)+"\n")
print "Proba theorique = %1.3e \n" %p_theorique

print "Proba empirique naive = %1.3e, (intervalle de confiance : +/-%1.3e)" %(p_emp_MC,erreur_MC)
print "Difference relative*100 = %1.2f \n" %(100*2*erreur_MC/p_theorique)

print "Sigma* = %1.2f " %hat_si_star

print "Proba empirique avec IS(Sigma=Sigma*) = %1.3e, (intervalle de confiance : +/- %1.3e)" \
        %(p_emp_ISsigmastar, erreur_emp_ISsigmastar)
print "Erreur relative*100 = %1.2f \n" %(100*2*erreur_emp_ISsigmastar/p_theorique)

print "Proba empirique avec I(Sigma=a) = %1.3e, (intervalle de confiance : +/- %1.3e)" \
        %(p_emp_ISa, erreur_emp_ISa)
print "Erreur relative*100 = %1.2f \n" %(100*2*erreur_emp_ISa/p_theorique)

