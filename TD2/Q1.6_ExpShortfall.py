import numpy as np

###############################################################################
## Question 1.6
###############################################################################
print "-" * 40
print "Question 1.6 : cas Gaussien"
print "-" * 40

##nombre de simulations de X
n = 100000
X = np.random.randn(n)
X.sort()

alpha = 1.e-3
u = 1-alpha
Q_n_u = X[int(np.ceil(n*u)-1)]

echantillonExpectedSF = X[X>Q_n_u]
tailleEchantillonES = echantillonExpectedSF.size

moyenneES = np.mean(echantillonExpectedSF)

s = np.std(echantillonExpectedSF)
rayonIC = 1.96*s/np.sqrt(tailleEchantillonES)

print "Expected ShortFall (estime) au niveau alpha={:1.4f}: {:1.4f} \n".format(alpha, moyenneES)
print "Intervalle de confiance [{:1.4f},{:1.4f}]".format(moyenneES-rayonIC,moyenneES+rayonIC), "de demi largeur {:1.4f} \n".format(rayonIC)
print "Taille echantillon pour le calcul de l'ES: ", tailleEchantillonES, "\n"

print "Erreur relative*100: {:1.2f} \n".format(rayonIC*100/moyenneES)


print "-" * 40
print "Question 1.6 : cas Gamma"
print "-" * 40

##Parametres de la loi Gamma
shape=2
scale=3
print "Parametres de la Gamma : shape={}, scale={}\n".format(shape,scale)

n = 10000
X = np.random.gamma(shape,scale=scale,size=n)
X.sort()

alpha = 1.e-3
u = 1-alpha
Q_n_u = X[int(np.ceil(n*u)-1)]

echantillonExpectedSF = X[X>Q_n_u]
tailleEchantillonES = echantillonExpectedSF.size

moyenneES = np.mean(echantillonExpectedSF)

s = np.std(echantillonExpectedSF)
rayonIC = 1.96*s/np.sqrt(tailleEchantillonES)

print "Expected ShortFall (estime) au niveau alpha={:1.4f}: {:1.4f} \n".format(alpha, moyenneES)
print "Intervalle de confiance [{:1.4f},{:1.4f}]".format(moyenneES-rayonIC,moyenneES+rayonIC), "de demi largeur {:1.4f} \n".format(rayonIC)
print "Taille echantillon pour le calcul de l'ES: ", tailleEchantillonES, "\n"

print "Erreur relative*100: {:1.2f} \n".format(rayonIC*100/moyenneES)
