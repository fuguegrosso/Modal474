import numpy as np
import numpy.random as npr
import scipy.stats as sps
import matplotlib.pyplot as plt
plt.close("all")

t = 10.
shape = 1.
scale = 4.
n = 50000

X = npr.gamma(shape, scale, size=n)
X_c = X[X > t] - t
x = np.linspace(0., max(X_c), 1000)
f_x = sps.gamma.pdf(x, a=shape, scale=scale)

plt.hist(X_c, normed=True, bins=2*round(n**(1./3.))) #empirique
plt.plot(x, f_x, "r") #theorique
plt.title("Loi empirique de (X | X > t) - t pour X de loi exponentielle d'intensite " \
    + str(1./scale))
plt.show()