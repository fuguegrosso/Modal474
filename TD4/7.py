import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps

l = 1.0
T = 1.0
alpha = 0.5
expectation = l * T * alpha
variance = l * T * alpha ** 2
rho = 5

x = expectation + rho * np.sqrt(variance)
thetax = np.log(x / expectation) / alpha
GammaT = l * T * (np.exp(alpha * thetax) - 1)
seuil = x / alpha

Nb_MC = int(2e5)
Nb_es = int(1e2)

est_MC = np.zeros((Nb_es, Nb_MC))
est_IS = np.zeros((Nb_es, Nb_MC))


for i in np.arange(Nb_es):
    N_mc = np.random.poisson(lam = l * T, size = (1, Nb_MC))
    N_is = np.random.poisson(lam = l * T * np.exp(alpha * thetax), size = (1, Nb_MC))
    L = np.exp(-thetax * alpha * N_is + GammaT)
    
    est_MC[i,:] = np.cumsum(N_mc > seuil) / np.arange(1,Nb_MC+1,dtype=float)
    est_IS[i,:] = np.cumsum((N_is > seuil) * L) / np.arange(1, Nb_MC + 1, dtype = float)


plt.figure(1)
plt.plot(est_MC[1, :], 'b', linewidth = 3.)
plt.plot(est_IS[1, :], 'r', linewidth = 3.)
theorique = sps.poisson.sf(x / alpha, mu = l * T)
plt.hlines(theorique, 0, Nb_MC, 'g', linewidth = 3.)

plt.title("Valeur de rho :" + str(rho))
plt.legend(['Monte Carlo','Imp Sampl'], loc="best")
plt.xlabel("M")
plt.grid()


plt.show()