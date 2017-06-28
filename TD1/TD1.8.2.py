import numpy as np
import scipy.stats as sps

n = 100000
d = 9
alpha = 0.05
a = -5
b = 3
diag = [1,2,3,4,5,4,3,2,1]

mean = np.zeros(d) #mean
cov = np.diag(diag) #initialize the cov matrix

for i in range(d):
    for j in range(d):
        cov[i, j] += 1. / (10 * (i + j + 2))

X = np.random.multivariate_normal(mean, cov, size = n)
indicatrices = np.all((X >= a) & (X <= b), axis = 1) #indicatrice: a 9d vector is confined in [a, b]^9 

proba = np.mean(indicatrices)
s = np.std(indicatrices, ddof = 1)

q = sps.norm.ppf(1 - alpha / 2)
delta = q * s / np.sqrt(n)
print(delta)
print("Intervalle de confiance {} = [{:.5f}, {:.5f}]".format(1 - alpha, proba - delta, proba + delta))
n_min = np.round(2 * q * s / (0.04 * proba) ** 2)
print("Il faut {} tirages".format(n_min))