import numpy as np
import matplotlib.pyplot as plt
import time

C = 100.0
T = 1.0
alpha = 30.0
Lambda = 30.0
la = 1.0
K = 3
p = 0.1

M = int(1e4)
Bounds = C * (1 - (np.arange(K, dtype = float) + 1) ** 2 / (K**2))
print("Spliting Bounds are: \t")
print(Bounds)
print("\n")

StartTime = time.time()
print("p = " + str(p) + " et lambda = " + str(la))
plt.clf()

N_jump = np.random.poisson(lam = la * T, size = (1, M))
Frequence = np.zeros(M + 1)

print("\t Chaine 1")

for i in np.arange(M): 
    j = N_jump[0, i] #one conditional value of N_T
    TimeJump = np.sort(T * np.random.uniform(0, 1, size = j))
    Reserve = C + Lambda * np.concatenate([np.arange(1), TimeJump]) - alpha * np.arange(j + 1)

    if min(Reserve) <= Bounds[0]:
        Frequence[i + 1] = Frequence[i] + 1
        PP_init = TimeJump
    else:
        Frequence[i+1] = Frequence[i]


ProbaEnd = Frequence[-1] / M

print("Pour le niveau 0, la proba estime est" + str(ProbaEnd))
plt.figure(1)
plt.plot(Frequence[1:] / (np.arange(M) + 1), label = "niveau 1")
plt.show()

for n_level in (1 + np.arange(K - 1)):
    print("\t Chaine" + str(n_level + 1))
    Frequence = np.zeros(M + 1)
    Rateaccept = np.zeros(M + 1)
    PP = PP_init #the last configuration that bankrupts
    MinPath = np.zeros(M + 1)
    MinPath[0] = min(C + Lambda * np.concatenate([np.arange(1), PP]) - alpha * np.arange(len(PP) + 1))

    for i in np.arange(M):
    	j = len(PP)
    	JumpConserve = PP[np.random.uniform(0, 1, size = j) <= p]
    	NbrAjoute = np.random.poisson((1 - p) * la * T)
    	NewJump = T * np.random.uniform(0, 1, size = NbrAjoute)
    	NewPP = np.sort(np.concatenate([JumpConserve, NewJump]))
    	NewReserve = C + Lambda * np.concatenate([np.arange(1), NewPP]) - alpha * np.arange(len(NewPP) + 1)
    	if min(NewReserve) <= Bounds[n_level - 1]:
    	    PP = NewPP
    	    MinPath[i + 1] = min(NewReserve)
    	    Rateaccept[i+1] = Rateaccept[i] + 1
    	else:
    	    MinPath[i+1] = MinPath[i]
    	    Rateaccept[i+1] = Rateaccept[i]

    	if MinPath[i + 1] <= Bounds[n_level]:
    	    Frequence[i + 1] = Frequence[i] + 1
    	    PP_init = PP
    	else:
            Frequence[i + 1] = Frequence[i]
    NewProbaEnd = Frequence[-1] / M
    ProbaEnd = NewProbaEnd * ProbaEnd
    print("\t Pour le niveau " + str(n_level) + ", la proba estimee est" + str(NewProbaEnd))

    plt.figure(1)
    plt.plot(Frequence[1:] / (np.arange(M) + 1), label = "niveau %1.0f" %(n_level + 1))
    plt.show()

    plt.figure(2)
    plt.plot(Rateaccept / (np.arange(M + 1) + 1), label = "niveau %1.0f" %(n_level + 1))
    plt.show()

plt.figure(1)
plt.title("Evolution de taux d'acceptation", fontsize = 20)
plt.ylabel("Taux d'accetptation", fontsize = 15)
plt.legend(loc = "best")
plt.grid()


print("\n La proba de ruine estimee est" + str(ProbaEnd))
EndTime = time.time()
print("\n Duree de calcul est" + str(EndTime - StartTime))

