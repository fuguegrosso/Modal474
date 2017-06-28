# -*- coding: utf-8 -*-
from pylab import *
import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt


######################
# Parametres du pbme
######################
# horizon temporel
n = 20
# nombre de particules a chaque iteration
M = int(1E5)
#  definition du seuil
c = 4.0
a = c * sqrt(n)


####################
# Valeur theorique
####################
print "-" * 45
print "Valeur theorique"
print "\t La vraie valeur de la probabilite est :", sps.norm.cdf(-c)


# BOUCLE sur le nombre de realisations independantes
NbrIter = 100
Stock = np.zeros((NbrIter, 5))
for nn in arange(NbrIter):
    # Tirages de M n points N(0,1) pour Monte Carlo naif avec M points.
    # Tirages de M n points N(0,1) pour particulaire avec M trajectoires de longueur n
    # on prendra les memes tirages pour les deux methodes.
    Y = np.random.randn(M, n)

    print "RUN : ", nn, "sur ", NbrIter

    ##################
    # Methode naive
    ##################
    print "-" * 45
    print "Methode Monte Carlo naive"
    # M realisations de X_n
    Z = np.sum(Y, axis=1)
    p_naive = np.mean(Z >= a)
    rayonIC = 1.96 * sqrt(p_naive * (1 - p_naive) / M)

    print "\t Valeur par Monte Carlo naif :", p_naive, "avec precision au risque 5%:", rayonIC
    print "\t Amplitude relative Monte Carlo naif :", 2 * rayonIC / p_naive

    Stock[nn, 0] = p_naive

    ###########################################################################################
    # En ponderant les trajectoires croissantes : Estimation via G(X)=e^{alpha (X_p-X_{p-1}) }
    ###########################################################################################
    print "-" * 45
    print "Ponderation des trajectoires croissantes"
    # le calcul de ces poids necessite de garder en memoire
    # l'instant courant et le premier passe.

    # parametres des poids G_p
    la = a / (n + 1)
    # X stocke l'instant courant et le precedent pour chacune des M particules
    # initialisation de X : X0 = 0 et X1 suit une loi N(0,1)
    X = array([zeros(M), Y[:, 0]])
    X = X.T
    # on stocke les indices de selection de l'ancetre
    indices = np.zeros(M)

    estim_constante_normalisation = 1
    for i in range(1, n):
        "Selection puis mutation en ponderant les trajectoires croissantes"
        # Calcul des poids non normalisés Gp
        G = exp(la * (X[:, 1] - X[:, 0]))
        # Mise a jour de la constante de normalisation
        estim_constante_normalisation = estim_constante_normalisation * \
            np.mean(G)
        # Selection de M pères, indep, avec poids G; avec repetition
        valeurs = arange(0, M)
        indices = np.random.choice(valeurs, size=M, p=G / sum(G))
        # Mise a jour des particules approchant eta_(i+1)
        # On stocke l'instant précédent et l'instant courant
        X[:, 0] = X[indices, 1]
        X[:, 1] = X[:, 0] + Y[:, i]

    estimation_terme_1 = np.mean((X[:, 1] >= a) * exp(-la * X[:, 0]))
    # Ici, la constante de normalisation se calcule explicitement :
    constante_normalisation = exp((n - 1) * (la**2) / 2)
    # Estimateur particule, constante exacte
    estim_part_1 = estimation_terme_1 * constante_normalisation
    # Estimateur particule, constante estimee
    estim_part_1_aux = estimation_terme_1 * estim_constante_normalisation

    # Affichage
    print "\t Constante de normalisation exacte : ", constante_normalisation
    print "\t Constante de normalisation estimee : ", estim_constante_normalisation
    print "\t Erreur relative ", np.abs(constante_normalisation - estim_constante_normalisation) / constante_normalisation
    print "\n \t Estimation (avec normalisation exacte) : ", estim_part_1
    print "\t Estimation (avec normalisation estimee) : ", estim_part_1_aux

    # Stockage des estimateurs
    Stock[nn, 1] = estim_part_1
    Stock[nn, 2] = estim_part_1_aux

    ###############################################################################
    # En ponderant les trajectoires hautes : Estimation via G(X)=e^{alpha X_p}
    ###############################################################################
    print "-" * 45
    print "En ponderant les trajectoires hautes"

    la = 2 * a / (n * (n - 1))

    # Stockage des M particules successives, de longueur max n
    X = zeros((M, n))
    # Initialisation, approximation de eta_1
    X[:, 0] = Y[:, 0]
    indices = np.zeros(M)

    estim_constante_normalisation = 1
    for i in range(0, n - 1):
        "Selection puis mutation en ponderant les trajectoires hautes"
        # Calcul des poids des particules courantes
        G = exp(la * X[:, i])
        # Update de la constante de normalisation
        estim_constante_normalisation = estim_constante_normalisation * mean(G)
        # Selection de M ancêtres
        valeurs = arange(0, M)
        indices = np.random.choice(valeurs, size=M, p=G / sum(G))
        # Mise  a jour des particules, approximation de eta_(i+2)
        X = X[indices, :]
        X[:, i + 1] = X[:, i] + Y[:, i + 1]

    # Calcul de l'estimateur du 1er terme
    estimation_terme_1 = np.mean(
        (X[:, -1] >= a) * exp(-la * sum(X[:, :-1], 1)))

    # Ici, la constante de normalisation se calcule explicitement :
    constante_normalisation = exp(n * (n - 1) * (2 * n - 1) * (la**2) / 12)
    # Calcul de l'estimateur avec constante exacte
    estim_part_2 = estimation_terme_1 * constante_normalisation
    # Calcul de l'estimateur avec constante estimee
    estim_part_2_aux = estimation_terme_1 * estim_constante_normalisation

    # Affichage
    print "\t Constante de normalisation exacte ", constante_normalisation
    print "\t Constante de normalisation estimee ", estim_constante_normalisation
    print "\t Erreur relative ", np.abs(constante_normalisation - estim_constante_normalisation) / constante_normalisation
    print "\n \t Estimation (avec normalisation exacte) =", estim_part_2
    print "\t Estimation (avec normalisation estimee) =", estim_part_2_aux

    # Stockage des estimateurs
    Stock[nn, 3] = estim_part_2
    Stock[nn, 4] = estim_part_2_aux


plt.close(1)
plt.figure(1)
plt.title("Boxplot de " + str(NbrIter) + " estimateurs indépendants")
plt.boxplot(Stock[:, 1:5], positions=[1, 2, 4, 5],
            labels=['exact', 'estim', 'exact', 'estim'])
plt.hlines(sps.norm.cdf(-c), 0, 6, 'g')

plt.close(2)
plt.figure(2)
Mstock = np.mean(Stock, axis=0)
S = np.std(Stock, axis=0)
plt.plot(S / Mstock, 'r-o')
plt.grid()


plt.close(3)
plt.figure(3)
plt.title("Estimateur Monte Carlo naif, en fonction de M")
Z = (np.sum(Y, axis=1)) >= a
estim_mc = np.cumsum(Z, dtype=float) / arange(1, M + 1)
plt.plot(arange(1, M + 1), estim_mc, 'b')
plt.hlines(sps.norm.cdf(-c), 0, M, 'g')
plt.grid()
