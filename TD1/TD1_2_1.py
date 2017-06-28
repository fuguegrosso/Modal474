import numpy as np
import scipy.stats as sps
from matplotlib import pyplot as plt

n, p, N = 10, 0.5, 1000
x = np.arange(n+1)
B = np.random.binomial(n, p, N)
f_X = sps.binom.pmf(x, n, p)

plt.hist(B, bins = n+1, normed = True, range = (-0.5, n+0.5), color = "white", label = "Loi empirique")
plt.stem(x, f_X, 'r', label = "loi theorique")

plt.legend(loc = 'best')
plt.show()