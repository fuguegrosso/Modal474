# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 19:23:31 2017

@author: Ruodan NI Yitao ZHANG
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps



a = 5
seuil = 0.1
rho = 0.7
seuil = 0.1 #the niveau of spliting defined in the question
tau = np.sqrt(1 - rho ** 2)

def estimation(b, a, rho, n):
	tau = np.sqrt(1 - rho ** 2)
	X =  np.random.randn(1)
	while X[0] <= a:
		X = np.random.randn(1)

	Y = np.random.randn(n)
	for i in range(int(n)):
		newX = rho * X[-1] * Y[i]
		X = np.append(X, newX * (newX > a) + X[-1] * (newX <= a))
	return np.mean(X > b)

def TrouverNiveaux(a, seuil, rho, n): #very tricky way to get a series of a_i
	av = [0]
	while 1 :
		x = np.linspace(av[-1], a, 10)
		probas = np.array([estimation(z, av[-1], rho, n) for z in x])

		if probas[-1] > seuil or probas[-1] >= a:
			break
		else :
			av.append(x[np.size(probas[probas > seuil])])
	av.append(a)
	av = av[1:]
	return av 

print "On trouve les niveaux des splitings approximatifs"
av = TrouverNiveaux(a, seuil, rho, 100)
print "Les niveaux des splitings sont" + str(av)

n = int(8e4)
Y = np.random.randn(n)
X = np.random.randn(1)

for i in range(n):
	X = np.append(X, rho * X[-1] + tau * Y[i]) #np.append makes an array

P = [np.mean(X > av[0])]

k = len(av)
for l in range(1, k):
	aprime = av[l - 1]
	startpoint = X[X > aprime][0]
	X = np.array([startpoint])
	Y = np.random.randn(n)

	for i in range(n):
		x = rho * X[-1] + tau * Y[i]
		X = np.append(X, x*(x>aprime) + X[-1]*(x<=aprime))
	P.append(np.mean(X > av[l]))

	Proba_empirique_spilit = np.prod(P)
	Proba_empirique_monte = np.mean(np.random.randn(k* n) > a)

	p = sps.norm.sf(a)

print "-"*40

print "Exact probability = "+str(p)

print "Splitting method gives = "+str(Proba_emp_split)

print "Simple Monte Carlo gives = "+str(Proba_emp_MonteCarlo)

print "-"*40

print "Splitting method relative error (percentage) = "+str(100*abs(Proba_emp_split-p)/p)

print "Simple Monte Carlo relative error (percentage) = "+str(100*abs(Proba_emp_MonteCarlo-p)/p)





