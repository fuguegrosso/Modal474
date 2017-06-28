import numpy as np
import scipy.stats as sps
from matplotlib import pyplot as plt

N = 1000
m = 10
s = 3

X = m + s * np.random.randn(N)

x = np.linspace(np.min(X), np.max(X), 100)

f_x = np.exp(-(x - m) * (x - m) / (2 * s ** 2)) / (np.sqrt(2 * np.pi) * s)
n_bins = 2 * int(N ** (1. / 3.))


#plt.hist(X, bins = n_bins, normed = True, histtype = "step", Label = "Hist")
plt.hist(X, bins=n_bins, normed=True, histtype="step", label="Histo")
plt.plot(x, f_x, "r", label="Density")
#plt.plot(x, f_x, "r", label="Density")
plt.legend(loc = "upper right")

plt.title("Loi gaussienne d'esperance {} et d'ecart-type {}".format(m, s))
plt.show() 

