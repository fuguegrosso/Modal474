import numpy as np
import scipy.stats as sps
from matplotlib import pyplot as plt

result = np.random.choice([1,2,3],p =[0.3,0.6,0.1],size = 100)
#print result
plt.hist(result,normed = True, bins = 3, range = (0.5, 3.5))
plt.show()