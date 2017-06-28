import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt

###############################################################################
# Question 1.4
###############################################################################
print "-" * 40
print "Question 1.4 Cas Gaussien"
print "-" * 40

# nombre de simulations
n = 10000
# nombre de repetitions (pour l'histogramme)
m = 1000

# Vraie valeur du quantile
u = 0.99
Q_u = sps.norm.ppf(u)

X = np.random.randn(m, n)

# Evolution du quantile empirique (pour la premiere repetition)
Q_empirique_u = [np.sort(X[0, 0:i])[int(np.ceil(i * u)) - 1]
                 for i in range(1, n + 1)]

# Affichage: convergence du quantile empirique (pour la premiere repetition)
plt.figure(1)
plt.close()
plt.axhline(y=Q_u, color="r", linewidth=1.5, label="Quantile en u=" + str(u))
plt.plot(range(1, n + 1), Q_empirique_u, color="b",
         linewidth=1.0, label="Quantile empirique")
plt.ylim(Q_u * 0.5, Q_u * 1.5)
plt.legend(loc="best")
plt.show()

######################################
# Histogramme de l'erreur normalisee
######################################
plt.figure(2)
plt.close()

# echantillon des quantiles empiriques Q_n(u)
X.sort(axis=1)
Q_n_u = np.array(X[:, int(np.ceil(n * u) - 1)])
erreur = np.sqrt(n) * (Q_n_u - Q_u)

minE, maxE = min(erreur), max(erreur)

# choix du nombre de colonnes
N = m**(1. / 3) * (maxE - minE) / (3.5 * np.std(erreur))

plt.hist(erreur, bins=int(N), normed="true", label="Erreur * $\sqrt{n}$")

# Densite gaussienne de variance connue pour comparaison
s = np.sqrt(u * (1. - u)) / sps.norm.pdf(Q_u)
x = np.linspace(minE, maxE, 100)
gaussienneLimite = sps.norm.pdf(x, loc=0, scale=s)
plt.plot(x, gaussienneLimite, "r", linewidth=1.5,
         label="Densite gaussienne de variance connue $u(1-u)/f(Q(u))^2$")

# Pour faire apparaitre la legende en dehors du graphique
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
           fancybox=True, shadow=True, ncol=5)
plt.show()


print "-" * 40
print "Question 1.4 Cas Gamma"
print "-" * 40

# Parametres de la loi Gamma
shape = 2
scale = 3
print "Parametres de la Gamma : shape={}, scale={}\n".format(shape, scale)

# nombre de simulations
n = 10000
# nombre de repetitions (pour l'histogramme)
m = 1000

# Vraie valeur du quantile
u = 0.99
Q_u = sps.gamma.ppf(u, shape, scale=scale)
X = np.random.gamma(shape, scale=scale, size=(m, n))

# Evolution du quantile empirique (pour la premiere repetition)
Q_empirique_u = [np.sort(X[0, 0:i])[int(np.ceil(i * u)) - 1]
                 for i in range(1, n + 1)]

# Affichage: convergence du quantile empirique (pour la premiere repetition)
plt.figure(1)
plt.close()
plt.axhline(y=Q_u, color="r", linewidth=1.5, label="Quantile en u=" + str(u))
plt.plot(range(1, n + 1), Q_empirique_u, color="b",
         linewidth=1.0, label="Quantile empirique")
plt.ylim(Q_u * 0.5, Q_u * 1.5)
plt.legend(loc="best")
plt.show()

######################################
# Histogramme de l'erreur normalisee
######################################
plt.figure(2)
plt.close()

# echantillon des quantiles empiriques Q_n(u)
X.sort(axis=1)
Q_n_u = np.array(X[:, int(np.ceil(n * u) - 1)])
erreur = np.sqrt(n) * (Q_n_u - Q_u)

minE, maxE = min(erreur), max(erreur)

# choix du nombre de colonnes
N = m**(1. / 3) * (maxE - minE) / (3.5 * np.std(erreur))

plt.hist(erreur, bins=int(N), normed="true", label="Erreur * $\sqrt{n}$")

# Densite gaussienne de variance connue pour comparaison
s = np.sqrt(u * (1. - u)) / sps.gamma.pdf(Q_u, shape, scale=scale)
x = np.linspace(minE, maxE, 100)
gaussienneLimite = sps.norm.pdf(x, loc=0, scale=s)
plt.plot(x, gaussienneLimite, "r", linewidth=1.5,
         label="Densite gaussienne de variance connue $u(1-u)/f(Q(u))^2$")

# Pour faire apparaitre la legende en dehors du graphique
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
           fancybox=True, shadow=True, ncol=5)
plt.show()
