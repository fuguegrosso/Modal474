import numpy as np
import numpy.random as npr
import scipy.stats as sps
import matplotlib.pyplot as plt

plt.close("all")

n = 10000
m = 5000

# Question 6.1.1
# Lois uniformes sur [-sqrt(3), sqrt(3)]
X = 2 * np.sqrt(3) * (npr.rand(m, n) - 0.5)
mu = 0.
s = 1.

T = np.sqrt(n) * (np.mean(X, axis=1) - mu) / s

x = np.linspace(np.min(T), np.max(T), 1000)
f_x = sps.norm.pdf(x)

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
n_bins = 2 * int(n ** (1. / 3.))
plt.hist(T, normed=True, bins=n_bins, histtype="step",
         label="Erreur normalisee")
plt.plot(x, f_x, "r", label="densite gaussienne")
plt.legend(loc='lower right')
plt.title("TCL pour la loi unif. [-sqrt(3), sqrt(3)]")


# Question 6.1.2
X1 = X[0, :]
arange_n = np.arange(1, n + 1)

T1 = np.sqrt(arange_n) * (np.cumsum(X1) / arange_n - mu) / s

plt.subplot(1, 2, 2)
plt.plot(arange_n, T1)
plt.xlabel("n")
plt.ylabel("sqrt(n)*(mean(X) - m)/s")
plt.title("Une trajectoire de l'erreur normalisee")

plt.show()
