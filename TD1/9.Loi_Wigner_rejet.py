import numpy as np
import matplotlib.pyplot as plt

plt.close("all")


def wigner_density(x):
    return np.sqrt(4 - x ** 2) / (2 * np.pi)


n = 100000
borne = 1. / np.pi
X = []
k = 0
for _ in range(n):
    # Il n'y a pas de "do while" en python
    # Premiere possibilite
    #u = 4. * np.random.rand() - 2.
    #v = borne * np.random.rand()
    #while v > wigner_density(u):
        #u = 4 * np.random.rand() - 2
        #v = borne * np.random.rand()
    # Seconde possibilite
    while True:
        u = 4 * np.random.rand() - 2
        v = borne * np.random.rand()
        if v <= wigner_density(u):
            break
    X.append(u)

x = np.linspace(-2., 2., 100)
f_x = wigner_density(x)

n_bins = 2 * int(n ** (1. / 3.))
plt.hist(X, normed=True, bins=n_bins, label="Loi de Wigner empirique")
plt.plot(x, f_x, "r", label="Densite de la loi de Wigner")
plt.legend(loc='best')
plt.title("Loi de Wigner")
plt.show()
