import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz
import scipy.stats as sps

###################
# Question 8.3.a. #
###################

# Nombre de tirages monte-carlo
n = 30000
# Dimension
d = 10
# On tire des uniformes
U = np.random.rand(n, d)
# Maximum cumule des lignes
U_cummax = np.maximum.accumulate(U, axis=1)
# Ou sont les records ?
records = (U == U_cummax)
# Nombre de paires de records consecutifs par ligne
R = np.sum(records[:, 1:] & records[:, :-1], axis=1)
# Nombre moyen de ces paires
I = np.mean(R)
# Ecart type
s = np.std(R, ddof=1)
# Quantile de la gaussienne
alpha = .05
q_alpha = sps.norm.ppf(1 - alpha / 2)
# Bornes de l'intervalle de confiance
b = s * q_alpha / np.sqrt(n)
print("Intervalle de confiance pour la probabilite au niveau {} : [{:.4f}, "
      "{:.4f}]".format(1 - alpha, I - b, I + b))

n_min = int((2 * q_alpha * s / (0.04 * I)) ** 2)
print("Pour avoir un precision de 4% il faut environ {} observations"
      .format(n_min))

###################
# Question 8.3.b. #
###################
counts = np.bincount(R)
counts = np.array(counts, dtype="double")
counts /= np.sum(counts)
plt.bar(left=np.arange(len(counts)) - 0.5, height=counts, width=1.)
plt.title("Loi du nombre de paires consecutives de records pour "
          "la loi uniforme")
plt.show()
