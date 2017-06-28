import numpy as np
import matplotlib.pyplot as plt
import time

C = 100.0
Lambda = 30.0
T = 1.0
alpha = 30.0
la = 0.05
P = [0.1, 0.5, 0.9]
K = 8

Nalgo = 3
M = [int(1.5e5), int(8e4), int(1.5e5)]

Bounds = C*(1-((np.arange(K,dtype=float)+1)**2/K**2))
print("les seuils sont \t")
print(Bounds)

StartTime = time.time()
StockProbaEnd = np.zeros((len(P), Nalgo))

for n_p in np.arange(len(P)):
    p = P[n_p]
    m = M[n_p]
    print("Lorsque p = " + str(p) + "et lambda = " + str(la))

    for nalgo in np.arange(Nalgo):
        print("Run " + str(nalgo +1))

        N_Jump = np.random.poisson(lam = la * T, size = (1, m))
        Frequence = np.zeros(m + 1)

        print("\t Chaine 1")
        for i in np.arange(m):
            j = N_Jump[0, i]
            TimeJump = np.sort(T * np.random.uniform(0, 1, size = j))
            Reserve = C + Lambda * np.concatenate([np.arange(1), TimeJump]) - alpha * np.arange(j + 1)
            if min(Reserve) <= Bounds[0]:
                Frequence[i + 1] = Frequence[i] + 1
                PP_init = TimeJump
            else:
                Frequence[i + 1] = Frequence[i]
        ProbaEnd =  Frequence[-1] / m
        print("\t Pour le niveau 0, la proba estimee est" + str(ProbaEnd))

        plt.figure(1)
        plt.plot(Frequence[1:] / (np.arange(m) + 1))

        for n_level in (1+np.arange(K-1)):
            print("\t Chaine" + str(n_level + 1))
            Frequence = np.zeros(m + 1)
            RateAccept = np.zeros(m + 1)
            PP = PP_init
            MinPath = np.zeros(m + 1)
            MinPath[0] = min(C + Lambda * np.concatenate([np.arange(1), PP]) - alpha * np.arange(len(PP) + 1))
            for i in np.arange(m):
                j = len(PP)
                JumpConserve = PP[np.random.uniform(0, 1, size = j) <= p]
                NbrAjoute = np.random.poisson(T * la *(1-p))
                NewJump = T * np.random.uniform(0, 1, NbrAjoute)
                NewPP = np.sort(np.concatenate([JumpConserve, NewJump]))
                NewReserve = C + Lambda * np.concatenate([np.arange(1), NewPP]) - alpha * np.arange(len(NewPP) + 1)
                if min(NewReserve) <= Bounds[n_level -1]:
                    PP = NewPP
                    MinPath[i + 1] = min(NewReserve)
                    RateAccept[i + 1] = RateAccept[i] + 1
                else:
                    MinPath[i + 1] = MinPath[i]
                    RateAccept[i+1] = RateAccept[i]
                if MinPath[i+1] <= Bounds[n_level]:
                    PP_init = PP
                    Frequence[i + 1] = Frequence[i] + 1
                else:
                    Frequence[i + 1] = Frequence[i]

            #print("frequence = " + str(Frequence[-2]))
            NewProbaEnd = Frequence[-1] / m
            #print("newproba = " + str(NewProbaEnd))
            ProbaEnd = NewProbaEnd * ProbaEnd
            print("\t Pour le niveau " + str(n_level) + "la proba estimee est " + str(NewProbaEnd))

            plt.figure(1)
            plt.plot(Frequence[1:] / (np.arange(m) + 1))

            plt.figure(2)
            plt.plot(RateAccept[1:] / (np.arange(m) + 1))

        plt.figure(1)
        plt.title("Consistance des estimateurs des probas")
        plt.grid()
        plt.figure(2)
        plt.title("Evolution de taux d'acceptation-rejet")
        plt.grid()


        print("Run " + str(nalgo + 1) + ": la proba de ruine estimee est " + str(ProbaEnd))
        StockProbaEnd[n_p,nalgo] = ProbaEnd

plt.figure(3)
plt.title("Boxplot de " + str(Nalgo) + "estimateur independants")
plt.boxplot(np.transpose(StockProbaEnd), positions = [1,3,5], labels = ['p = 0.1', 'p = 0.5', 'p = 0.9'])

plt.figure(4)
mean = np.mean(StockProbaEnd, axis = 1)
s = np.std(StockProbaEnd, axis = 1)
plt.plot(P, s/mean, 'd-')
plt.xlabel("valeur de p", fontsize = 15)
plt.ylabel("ratio ecart-type / moyenne", fontsize = 15)
plt.grid()

EndTime = time.time()
print("Duree de temp " + str(EndTime -StartTime))

 

