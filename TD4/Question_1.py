# -*- coding: utf-8 -*-
from numpy import zeros, cumsum, arange, append
from numpy.random import poisson, rand, exponential

from matplotlib.pyplot import figure, step, title, legend, ylim


###############################################################################
## Question 1: simulation jusqu'a T_n
###############################################################################
def homogeneous_poisson_from_n(intensity, n):
    """
    Simulation d'une trajectoire d'un processus de Poisson homogene
    jusqu'a l'instant T_n    
    """
    scale = 1. / intensity
    # Attention: numpy.random.exponential prend comme premier argument la moyenne de la 
    # loi exponentielle, pas son parametre
    E = zeros(n+1)
    E[1:] = exponential(scale, size=n)
    events = cumsum(E)
    jumps = arange(n+1)
    return events, jumps

intensity = 1.
n = 10

events, jumps = homogeneous_poisson_from_n(intensity, n)

figure()
step(events, jumps, where="post", label="nbre de sauts fixe n=%s"%n, linewidth=2.0)
ylim((0.,jumps[-1]+1))

###############################################################################
## Question 1: simulation jusqu'a T
###############################################################################
def homogeneous_poisson_from_T(intensity, T):
    """
    Simulation d'une trajectoire d'un processus de Poisson homogene
    sur l'intervalle [0,T]
    """
    N = poisson(T * intensity)
    
    events = zeros(N+1)
    events[1:] = T * rand(N)
    events.sort()
    events = append(events,T)
    
    jumps = arange(N+1)
    jumps = append(jumps,N)
    return events, jumps

intensity = 1.
T = 10
events, jumps = homogeneous_poisson_from_T(intensity, T)

step(events, jumps, where="post", label="horizon fixe T=%s"%T, linewidth=2.0)
ylim((0.,jumps[-1]+1))

title("Processu de Poisson homogene d'intensite " + str(intensity), fontsize=12)
legend(loc="best")