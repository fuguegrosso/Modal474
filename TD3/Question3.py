# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:55:39 2015

@author: florent

In this text, for Z=Binom(n,p), we compute P(Z<=nx) in 3 different ways:
- we give the exact value of the probability thanks to the function scipy.stats.binom.cdf
- we give a standard Monte Carlo estimate out of N independant simulations of Z
- we give an importance sampling estimate out of N independant simulations of Z'=Binom(n,q) with q=x
"""

import numpy as np
import scipy.stats

p=.25
n=300
x=.001
q=x
N=int(1E6)

print("\n"+"Exact value : ")
print(str(scipy.stats.binom.cdf(n*x,n,p)))

print("\nStandard Monte Carlo : ")

Z=np.random.binomial(n,p,N)

pest=np.mean(Z/float(n)<=x)

sigma = np.sqrt(pest*(1-pest))

print(str(pest)+" +/- "+str(1.96*sigma/np.sqrt(N)))

print("\nIS Monte Carlo : ")

F=((1-p)/(1-q))**n

quot=p*(1-q)/(q*(1-p))

Zprime=np.random.binomial(n,q,N)

Ech=F*((Zprime/float(n))<=x)*(quot**Zprime)

pest=np.mean(Ech)

sigma=np.std(Ech)

print(str(pest)+" +/- "+str(1.96*sigma/np.sqrt(N)))