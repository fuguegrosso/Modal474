import numpy as np
import numpy.random as npr
import scipy.stats as sps
import matplotlib.pyplot as plt

plt.close("all")

n = 100000
shape = 10.
scale = 4.

X = npr.gamma(shape=shape, scale=scale, size=n)

x = np.linspace(np.min(X), np.max(X), 1000)
f_x = sps.gamma.pdf(x, a=shape, scale=scale)

n_bins = 2 * int(n ** (1. / 3.))
plt.hist(X, bins=n_bins, normed=True, histtype="step", label="Histogramme")
plt.plot(x, f_x, "r", label="Densite")
plt.title("Loi gamma de forme {} et d'echelle {}".format(shape, scale))
plt.legend(loc="upper right")
plt.show()
