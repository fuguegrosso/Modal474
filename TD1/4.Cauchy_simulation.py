import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt


def densite_cauchy(x, scale):
    return scale / (np.pi * (scale ** 2 + x ** 2))


def inverse_fonction_repartition_cauchy(y, scale):
    return scale * np.tan(np.pi * (y - .5))


a = 1.
n = 5000
plot_bound = 10 * a

U = npr.rand(n)
X = inverse_fonction_repartition_cauchy(U, a)

x_axis = np.linspace(-plot_bound, plot_bound, int(np.sqrt(n)))
f_x = densite_cauchy(x_axis, a)

n_bins = 2 * int(n ** (1. / 3.))
plt.hist(X, normed=True, bins=n_bins, color="w", label="histogramme",
         range=(-plot_bound, plot_bound))
plt.plot(x_axis, f_x, "r", label="densite de Cauchy", linewidth="2.0")
plt.legend(loc='best')
plt.title("Loi de Cauchy de parametre {}".format(a))
plt.show()
