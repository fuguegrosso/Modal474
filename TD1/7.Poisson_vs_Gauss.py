import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt

plt.close("all")

n = 50
# p = 0.3
p = 0.01

mean_binomial = n * p
sd_binomial = np.sqrt(n * p * (1. - p))

plot_bound = mean_binomial + 4 * sd_binomial

x = np.arange(plot_bound + 1)
f = sps.binom.pmf(x, n, p)

# Trace de la loi de Poisson associee
p_poisson = sps.poisson.pmf(x, mean_binomial)
# Trace de la loi normale associee
x2 = np.linspace(0, plot_bound, 1000)
p_gauss = sps.norm.pdf(x2, loc=mean_binomial, scale=sd_binomial)

plt.plot(x2, p_gauss, "g", lw=3, label="Loi gaussienne")
plt.stem(x, f, label="Loi binom.", linefmt="b", markerfmt="bo", basefmt="b")
eps = .12 * sd_binomial
plt.stem(x + eps, p_poisson, label="Loi de poisson",
         linefmt="r", markerfmt="ro", basefmt="r")

plt.title("Approximation gaussienne vs poissonienne (n * p^2 = {:.2g})"
          .format(n * p ** 2))
plt.legend(loc="upper right")
plt.show()
