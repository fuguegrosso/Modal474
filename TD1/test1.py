import numpy as np
import scipy.stats as sps
from matplotlib import pyplot as plt

x = np.array([1,2,3])
y = np.array([0.2, 0.5, 0.3])
plt.stem(x,y)
plt.xlim(0.5, 3.5)
plt.ylim(0., 0.6)
plt.show()