import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sps

n = int(5e3)
X = np.random.randn(n)
MinX = min(X)
MaxX = max(X)
L = MaxX -MinX
#N = round(n ** (1. / 8.) * L /3.49)
#N=round(n**(5./8.)*L/3.49)
N=round(n**(1./3.)*L/3.49)

x = np.linspace(MinX, MaxX, 1000)
f_x = sps.norm.pdf(x)
plt.plot(x, f_x, "r", linewidth = 1.0, label = "Gauss distribution")

plt.hist(X, bins = N, normed = True, histtype = 'step', label = "Histo")
plt.legend(loc = 'upper right', bbox_to_anchor = (0.5, -0.05), ncol = 2, fancybox = True, shadow = True)
plt.show()