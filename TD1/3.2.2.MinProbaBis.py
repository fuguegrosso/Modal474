import numpy as np

n = 20
m = int(1e3)
p = .2
bound = 5
X = np.random.rand(m, n)
X = np.cumsum(X, axis=1)
P = np.sum(X < bound, axis=0, dtype=float) / m
print("\nMinimum = {}".format(str(min(np.argwhere(P <= p))[0] + 1)))
