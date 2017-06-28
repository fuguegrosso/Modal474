import numpy as np
from numpy.linalg import norm
import scipy.stats as sps
import matplotlib.pyplot as plt

n = 1000
d = 10
alpha = 0.05

X = np.random.rand(n, d) 
f_X = np.pi ** 2 * np.sum(X, axis = 1) ** 2 * norm(X, axis = 1)

I = np.mean(f_X) #I = estimation of integral
s = np.std(f_X, ddof = 1) #means delta degrees of freedom, divisor  n - ddof

q = sps.norm.ppf(1 - alpha / 2)

delta = q * s / np.sqrt(n)

print("Intervalle de confiance au niveau {} : [{:.2f}, {:.2f}]" # .2f = 2 decimals
      .format(1 - alpha, I - delta, I + delta))
n_min = np.round((2 * q * s / (0.02 * I))**2)
print("Il faut {} d'obervations".format(n_min))
