# -*- coding: utf-8 -*-
from numpy import zeros, cumsum, append
from numpy.random import poisson, rand, exponential, standard_cauchy

from matplotlib.pyplot import figure, step, title, legend

###############################################################################
## Question 2
###############################################################################
def compound_poisson_from_n(intensity, n, jumps_distribution="exponential",
                            intensity_jumps=4.):
    """
    Simulation de la trajectoire d'un processus de Poisson composé jusqu'a
    l'instant T_n, pour une loi d'amplitude des sauts donnee (par défaut, 
    c'est la loi exponentielle d'esperance 1/4)
    """
    scale = 1. / intensity
    scale_jumps = 1. / intensity_jumps

    events = zeros(n+1)
    events[1:] = cumsum(exponential(scale, size=n))
    
    jumps = zeros(n+1)
    if jumps_distribution == "exponential":
        jumps[1:] = cumsum(exponential(scale_jumps, size=n))
    if jumps_distribution == "cauchy":
        jumps[1:] = cumsum(abs(standard_cauchy(size=n)))    
    return events, jumps

def compound_poisson_from_T(intensity, T, jumps_distribution="exponential",
                            intensity_jumps=4.):
    """
    Simulation de la trajectoire d'un processus de Poisson composé sur l'intervalle
    [0,T], pour une loi d'amplitude des sauts donnee (par défaut, c'est la loi
    exponentielle d'espérance 1/4)
    """
    scale_jumps = 1. / intensity_jumps
    N = poisson(T * intensity)

    events = zeros(N+1)
    events[1:] = T * rand(N)
    events.sort()
    events = append(events,T)
    
    jumps = zeros(N+1)
    if jumps_distribution == "exponential":
        jumps[1:] = cumsum(exponential(scale_jumps, size=N))
    if jumps_distribution == "cauchy":
        jumps[1:] = cumsum(abs(standard_cauchy(size=N)))
    jumps = append(jumps,jumps[-1])
    
    return events, jumps


if __name__ == "__main__":
    ######################
    ## Affichage: on peut choisir quelle type de trajectoire afficher en 
    ## modifiant la valeur des 'Flags'
    ######################
    
    n_Flag = 1
    T_Flag = 0
    
    ## Simulation a partir de la valeur de n
    if n_Flag:
        intensity = 3.
        n = 10
        events, jumps = compound_poisson_from_n(intensity, n, "exponential")
        step(events, jumps, where="post", linewidth=2.0)
        title("Qu.2 : Poisson compose jusqu'a T_n d'intensite " + str(intensity) + ", n="+str(n))
         
        events, jumps = compound_poisson_from_n(intensity, n, "cauchy")
        step(events, jumps, where="post", linewidth=2.0)
        legend(['Exponentiel', 'Cauchy'],loc="best")
    
    ## Simulation a partir de la valeur de T
    if T_Flag:
        # Sauts exponentiels
        intensity = 3. 
        T = 8.
        events, jumps = compound_poisson_from_T(intensity, T, "exponential")
        figure()
        step(events, jumps, where="post", linewidth=2.0)
        title("Qu.2: Poisson compose sur [0,T] d'intensite " + str(intensity) + ", T=" + str(T))
        
        events, jumps = compound_poisson_from_T(intensity, T, "cauchy")
        step(events, jumps, where="post", linewidth=2.0)
        legend(['Exponentiel', 'Cauchy'],loc="best")