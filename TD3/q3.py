import numpy as np
import scipy.stats as sps

p = 0.25
n = 300
x = 0.001
q = x
N = int(1E6)

print("exact value = ")
print(str(sps.binom.cdf(n*x, n, p)))

print("\n"+ "Monte Carlo = ")
Z = np.random.binomial(n,p,N)
pest = np.mean(Z/float(n) <= x)
sigma = np.sqrt(pest * (1- pest))

print(str(pest) + "+/-" + str(1.96 * sigma / np.sqrt(N)))

print("\n IS MonteCarlo = ")
F = ((1-p)/(1-q))**n
quot = p * (1-q) /(q * (1-p))
Zprime = np.random.binomial(n, q, N)
Ech=F*((Zprime/float(n))<=x)*(quot**Zprime)

pest=np.mean(Ech)

sigma=np.std(Ech)

print(str(pest)+" +/- "+str(1.96*sigma/np.sqrt(N)))