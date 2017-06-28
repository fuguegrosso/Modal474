import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

plt.close("all")

# Loi des grands nombres pour la loi uniforme
n = 1000
X = npr.rand(n)
M = np.cumsum(X) / np.arange(1, n + 1)

plt.subplot(1, 2, 1)
plt.plot(np.arange(1, n + 1), M, label="S_n / n")
plt.axhline(0.5, color="r", label="E(X)")
plt.axis([0, n, 0, 1])
plt.legend(loc="best")
plt.xlabel("n")
plt.title("LGN loi unif. sur [0, 1]")

# Loi des grands nombres pour la loi de densite 2x sur [0, 1]
X = np.sqrt(npr.rand(n))
M = np.cumsum(X) / np.arange(1, n + 1)

plt.subplot(1, 2, 2)
plt.plot(M, label="S_n / n")
plt.axhline(2. / 3, color="r", label="E(X)")
plt.title("LGN pour la densite 2x sur [0, 1]")
plt.axis([0, n, 0.2, 1])
plt.xlabel("n")
plt.legend(loc="best")

plt.show()
