import numpy as np
import numpy.random as npr

n = 20
m = 10000
p = .2
bound = 5

X = npr.rand(m, n)
X = np.cumsum(X, axis=1)
indicatrices = (X < bound)

index_probabilities = np.mean(indicatrices, axis=0)
n_0 = np.min(np.argwhere(index_probabilities <= p))

print("\nn_0 = {}".format(n_0 + 1))
