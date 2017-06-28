import numpy as np
import scipy.stats as sps

m = 500
n = 100
alpha = 0.05
X = np.random.rand(m, n)

M = np.mean(X, axis = 1) #array of means
S = np.sqrt(1. / (n-1) * np.sum(np.power(X - M.reshape(-1, 1), 2), axis = 1))

error = np.abs(M - 0.5)
q = sps.norm.ppf(1 - alpha / 2)

alpha_empirique = 1. - np.mean(error < q * S / np.sqrt(n))

print("alpha_theorique = {}".format(alpha))
print("\n")
print("alpha_empirique = {}".format(alpha_empirique))


