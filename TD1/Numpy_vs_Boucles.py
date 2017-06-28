from timeit import timeit

import numpy as np
n = int(1e5)


# Methode 1. Boucle for
print("Methode 1. Boucle for")
code_boucle_for = 
np.sum([1. / i for i in range(1, n)]) - np.log(n)

n_tries = 10
time_boucle_for = timeit(code_boucle_for, setup=setup, number=n_tries) / n_tries
print("Cela a pris {} secondes par essai".format(time_boucle_for))

print("-" * 40)
# Methode 2. Numpy
print("Methode 2. Numpy")
code_numpy = """
np.sum(1. / np.arange(1, n)) - np.log(n)
"""
n_tries = 100
time_numpy = timeit(code_numpy, setup=setup, number=n_tries) / n_tries
print("Cela a pris {} secondes par essai".format(time_numpy))

print("-" * 40)
print("Facteur de gain {}".format(time_boucle_for / time_numpy))
