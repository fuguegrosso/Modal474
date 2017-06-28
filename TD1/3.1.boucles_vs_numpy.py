import numpy as np
from time import time

n = int(1e6)
# Methode 1. Boucle for
print("-" * 40)
print("Methode 1. Boucle for")
print("-" * 40)
t1 = time()
print("gamma=", np.sum([1. / i for i in range(1, n)]) - np.log(n))
t2 = time()
temps1 = t2 - t1
print("Cela a pris ", temps1, " secondes")
# Methode 2. Numpy
print("-" * 40)
print("Methode 2. Numpy")
t1 = time()
print("gamma=", np.sum(1. / np.arange(1, n)) - np.log(n))
t2 = time()
temps2 = t2 - t1
print("Cela a pris ", temps2, " secondes")
print("-" * 40)
print("Facteur de gain ", temps1 / temps2)
