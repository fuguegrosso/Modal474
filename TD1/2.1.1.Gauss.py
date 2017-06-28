import numpy as np
import numpy.random as npr
import scipy.stats as sps
import matplotlib.pyplot as plt

plt.close("all")

n = 10000
m = 10.  # Esperance
s = 3.  # Ecart-type

# La fonction randn de numpy.random genere des v.a. gaussiennes centrees
# reduites
X = m + s * npr.randn(n)

x = np.linspace(np.min(X), np.max(X), 100)

f_x = np.exp(-(x - m) * (x - m) / (2 * s ** 2)) / (np.sqrt(2 * np.pi) * s)
# Autre possibilite:
# f_x = sps.norm.pdf(x, loc=m, scale=s)

n_bins = 2 * int(n ** (1. / 3.))
plt.hist(X, bins=n_bins, normed=True, histtype="step", label="Histogramme")
plt.plot(x, f_x, "r", label="Densite")
plt.legend(loc="upper right")
plt.title("Loi gaussienne d'esperance {} et d'ecart-type {}".format(m, s))
plt.show()
