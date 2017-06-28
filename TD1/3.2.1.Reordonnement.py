import numpy as np
import numpy.random as npr

n = 100
m = 10000

u = .8
p = .6
rang = int(np.floor(n*u))

X = npr.randn(m, n)
X = np.sort(X, axis=1)

probabilite = np.mean(np.cos(X[:, rang]) < p)

# Autre possibilite: attention a la conversion en double
# Y = np.cos(X[:, rang]) < p
# probabilite = np.sum(Y, dtype=np.double) / m

print("\nprobabilite : {}".format(probabilite))
