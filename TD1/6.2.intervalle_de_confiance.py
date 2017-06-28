import numpy as np
import numpy.random as npr
import scipy.stats as sps

n = 100
m = 600
X = npr.rand(m, n)

# Calcul des moyennes et de l'ecart type empirique
M = np.mean(X, axis=1)

S = np.sqrt(1. / (n - 1) * np.sum(np.power(X - M.reshape(-1, 1), 2), axis=1))
# On peut aussi utiliser une fonction de numpy
# ddof=1 est necessaire pour avoir l'estimateur sans biais
# S = np.std(X, axis=1, ddof=1)

# Niveau de l'intervalle de confiance
alpha = 0.05
# Quantile de la gaussienne standard
q_alpha = sps.norm.ppf(1 - alpha / 2)

# Moyenne du nombre de fois que 0.5 est dans l'intervalle de confiance
error = np.abs(M - 0.5)
alpha_empirique = np.mean(error < q_alpha * S / np.sqrt(n))

print("\nProbabilite de couverture demandee = {}".format(1. - alpha))
print("Probabilite de couverture empirique = {}".format(alpha_empirique))
