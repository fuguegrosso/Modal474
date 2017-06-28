import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt

n = 100
p = 0.4  #S_n is binominal distribution
#p = 0.01

m_binomial = n * p
s_binomial = np.sqrt(n * p * (1 - p))

plot_range = m_binomial + 4 * s_binomial

#discret = pmf, continue = pdf, inverse quantile = ppf

x = np.arange(int(plot_range) + 1) 
f_x = sps.binom.pmf(x, n, p) #binomial probability 

#Loi poisson
p_poisson = sps.poisson.pmf(x, m_binomial)
#loi gaussienne
x1 = np.linspace(0, plot_range, 2000)
p_gauss = sps.norm.pdf(x1, loc = m_binomial, scale = s_binomial)

plt.plot(x1, p_gauss, "r", lw = 1.5, label = "Gauss")  #lw = linewidth, in float
plt.stem(x + 0.12 * s_binomial, p_poisson, label = "Poisson", linefmt = "b", makerfmt = "ro", basefmt = "b")
#add a biais to differ from binom
plt.stem(x, f_x, label = "binom", linefmt = "g", makerfmt = "go", basefmt = "g")

plt.title("Approximation poisson vs norm")
plt.legend(loc = "upper right")

plt.show()