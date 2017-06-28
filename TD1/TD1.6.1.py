import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps

m = 10000
n = 5000

X = 2 * np.sqrt(3) * (np.random.rand(m, n) - 0.5) 
m = 0.
s = 1.

T = np.sqrt(n) * (np.mean(X, axis = 1) - m) / s ##LGN suite
x= np.linspace(np.min(T), np.max(T), 1000)
f_x = sps.norm.pdf(x) ##norm distribution

plt.subplot(1,2,1)
n_bins = 2 * int(n * (1. / 3.))
plt.hist(T, normed = True, bins = n_bins, histtype = "step", label = "la suite concerge vers norme" )
plt.plot(x, f_x, label = "norm distribution")
plt.title("TCL pour la loi uniforme")

X1 = X[0, :] #take an array

T1 = np.sqrt(np.arange(1, n+1)) * (np.cumsum(X1) / np.arange(1, n+1) - m) / s
plt.subplot(1,2,2)
plt.plot(np.arange(1 , n+1), T1)
plt.xlabel("n")
plt.ylabel("sqrt(n) * (mean(x)-m)/s")
plt.title("une trajection de l'erreur normalisee")

plt.show()