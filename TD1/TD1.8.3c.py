import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz

n = 30000
d = 4
alpha = 0.05
rho = 0.95
m = np.zeros(d)
cov = toeplitz(rho ** np.arange(1, d+1))
X = np.random.multivariate_normal(m, cov, size = n)
X_cumax = np.maximum.accumulate(X, axis = 1)

records = (X == X_cumax)
R = np.sum(records[:, 1:] & records[:, :-1], axis = 1)
I = np.mean(R)
s = np.std(R)
q = sps.norm.ppf(1 - alpha / 2)
delta = q * s / np.sqrt(n)
print("Intervalle de confiance pour la probabilite au niveau {} : [{:.4f}, "
      "{:.4f}]".format(1 - alpha, I - delta, I + delta))

n_min = int((2 * q * s / (0.04 * I)) ** 2)
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