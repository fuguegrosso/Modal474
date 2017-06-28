import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz #matrix with constant diagnals
import scipy.stats as sps

n = 30000
d = 10
alpha = 0.05
X = np.random.rand(n, d)
X_cumax = np.maximum.accumulate(X, axis = 1) #accumulated max

records = (X == X_cumax)
R = np.sum(records[:, 1:] & records[:, :-1], axis = 1)
m = np.mean(R) #average number of pairs
s = np.std(R, ddof = 1)

q = sps.norm.ppf(1 - alpha / 2)
delta = q * s / np.sqrt(n)
print("Intervalle de confiance {} = [{:.4f}, {:.4f}]".format(alpha, m - delta, m + delta))
n_min = int((2 * q * s / (0.04 * m)) ** 2)
print("Il faut {} tirages pour 0.04".format(n_min))

counts = np.bincount(R)
counts = np.array(counts, dtype = "double")
#obtain a percentage histogramme
counts /= np.sum(counts)
plt.bar(left = np.arange(len(counts)) - 0.5, height = counts, width = 1.0)

plt.title("Loi des paires consecutives...")
plt.show()
