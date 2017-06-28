import numpy as np
import matplotlib.pyplot as plt

n = 1000000
M = 1 / np.pi

def wigner(x):
	return np.sqrt(4 - x**2) / (2 * np.pi)

X = []


for _ in range(n):
    while True:
        u = 4 * np.random.rand() - 2
        v = M * np.random.rand()
        if v <= wigner(u):
            break
    X.append(u)
    #add the min{}, rejeter

x = np.linspace(-2.0, 2.0, 100)
f_x = wigner(x)

n_bins = int(2 * n ** (1. / 3.))
plt.hist(X, normed = True, bins = n_bins,label = "methode de rejet")
plt.plot(x, f_x, label = "distribution theorique")
plt.legend(loc = "upper right")
plt.title("Loi de Wigner")
plt.show()
