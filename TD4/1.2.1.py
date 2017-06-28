import numpy as np
import matplotlib.pyplot as plt

n = 10
X = np.arange(0,n)
beta = 2.0

T = np.random.exponential(scale = beta, size = n)
T = np.cumsum(T)
plt.step(T, X, where = 'post', label = 'trajectoire')
plt.show()
