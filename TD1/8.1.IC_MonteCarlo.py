import numpy as np
import numpy.random as npr
from numpy.linalg import norm
import scipy.stats as sps

import matplotlib.pyplot as plt

plt.close("all")

# Nombre de tirages monte-carlo
n = 10000
# Dimension
d = 10
# Niveau de confiance asymptotique
alpha = 0.05
# Tirage d'uniformes
U = npr.rand(n, d)

# Calcul de la fonction
f_U = np.pi ** 2 * np.sum(U, axis=1) ** 2 * norm(U, axis=1)

# Estimation de l'integrale
I = np.mean(f_U)
# Ecart type empirique
sigma = np.std(f_U, ddof=1)

# Quantile de la gaussienne
q_alpha = sps.norm.ppf(1 - alpha / 2)
# Demi largeur de l'intervalle de confiance
b = q_alpha * sigma / np.sqrt(n)

print("Intervalle de confiance au niveau {} : [{}, {}]"
      .format(1 - alpha, I - b, I + b))

n_min = round((2 * q_alpha * sigma / (0.02 * I)) ** 2)
print("Pour avoir un precision de 2% il faut environ {} observations"
      .format(n_min))
