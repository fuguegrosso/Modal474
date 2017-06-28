import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz
import scipy.stats as sps

# Nombre de tirages monte-carlo
n = 30000
# Dimension
d = 4
# Quantile de la gaussienne
alpha = .05

###################
# Question 8.3.c. #
###################
# Level of correlation between variables
rho = 0.95
m = np.zeros(d)
cov = toeplitz(rho ** np.arange(1, d + 1))
X = np.random.multivariate_normal(m, cov, size=n)
X_cummax = np.maximum.accumulate(X, axis=1)
# Ou sont les records ?
records = (X == X_cummax)
# Nombre de paires de records consecutifs par ligne
R = np.sum(np.logical_and(records[:, 1:], records[:, :-1]), axis=1)
# Nombre moyen de ces paires
I = np.mean(R)
# Ecart type
s = np.std(R)
# Quantile de la gaussienne
q_alpha = sps.norm.ppf(1 - alpha / 2)
# Bornes de l'intervalle de confiance
b = s * q_alpha / np.sqrt(n)
print("Intervalle de confiance pour la probabilite au niveau {} : [{:.4f}, "
      "{:.4f}]".format(1 - alpha, I - b, I + b))

n_min = int((2 * q_alpha * s / (0.04 * I)) ** 2)
print("Pour avoir un precision de 4% il faut environ {} observations"
      .format(n_min))

counts = np.bincount(R)
counts = np.array(counts, dtype="double")
counts /= np.sum(counts)
plt.figure()
plt.bar(left=np.arange(len(counts)), height=counts, width=1.)
plt.title("Loi du nombre de paires consecutives de records pour un vecteur "
          + "gaussien non-standard")
plt.show()
