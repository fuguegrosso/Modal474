import numpy as np
import matplotlib.pyplot as plt

#plt.close("all")

n = 1000
X = np.random.rand(n)
M = np.cumsum(X) / np.arange(1, n+1) #S_n / n

plt.subplot(1,2,1)
plt.plot(np.arange(1, n+1), M, label = "S_n / n")
plt.axhline(0.5, color = "r", label = "E(x)")
plt.axis([0, n, 0, 1])
plt.legend(loc = "best")
plt.xlabel("n")
plt.title("LGN uniforme")

X = np.sqrt(np.random.rand(n))
M = np.cumsum(X) / np.arange(1, n+1)

plt.subplot(1,2,2)
plt.plot(np.arange(1, n+1), M, label = "S_n / n")
plt.axhline(2. / 3., color = "r", label = "E(X)")
plt.axis([0, n, 0, 1])
plt.legend(loc = "best")
plt.xlabel("zyt")
plt.title("LGN density 2x")

plt.show()

