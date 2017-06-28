import numpy as np
import scipy.stats as sps

# Nombre de tirages monte-carlo
n = 30000
# Niveau de confiance asymptotique
alpha = 0.05
# Le vecteur doit etre dans l'intervalle [a, b]
a = -5
b = 3

# diagonale de la matrice de covariance
diag = [1., 2, 3, 4, 5, 4, 3, 2, 1]
# Dimension du vecteur gaussien
d = len(diag)
# Esperance
m = np.zeros(d)

# Construction de la matrice de covariance
cov = np.diag(diag)
for i in range(d):
    for j in range(d):
        cov[i, j] += 1. / (10 * (i + j + 2))

# Simulation des vecteurs gaussiens
X = np.random.multivariate_normal(m, cov, size=n)

# Les vecteurs gaussiens sont-ils dans [a, b]^9 ? (X a taille n*d)
indicatrices = np.all((X >= a) & (X <= b), axis=1)

# Estimation de la probabilite
I = np.mean(indicatrices)
# Ecart type
s = np.std(indicatrices)

# Quantile de la gaussienne
q_alpha = sps.norm.ppf(1 - alpha / 2)
# Demi-largeur de l'intervalle de confiance
b = q_alpha * s / np.sqrt(n)

print("Intervalle de confiance pour la probabilite au niveau {} : [{:.4f}, "
      "{:.4f}]".format(1 - alpha, I - b, I + b))

n_min = int((2 * q_alpha * s / (0.04 * I)) ** 2)
print("Pour avoir un precision de 4% il faut environ {} observations"
      .format(n_min))
