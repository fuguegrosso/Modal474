# -*- coding: utf-8 -*-
#from pylab import * 
import numpy as np
import scipy.stats as sps

######################
# Parametres du pbme
######################
# horizon temporel
n = 20
# nombre de particules a chaque iteration
M = int(1E5)
#  definition du seuil
c = 4.0
a = c*np.sqrt(n)


# Tirages de M n points N(0,1) pour Monte Carlo naif avec M points.
# Tirages de M n points N(0,1) pour particulaire avec M trajectoires de longueur n
# on prendra les memes tirages pour les deux methodes.
Y = np.random.randn(M,n)

####################
# Valeur theorique
####################
print "-" * 45
print "Valeur theorique"
print "\t La vraie valeur de la probabilite est :", sps.norm.cdf(-c)


##################
# Methode naive 
##################
print "-" * 45
print "Methode Monte Carlo naive"
# M realisations de X_n
X = np.sum(Y,axis=1) 
p_naive = np.mean(X>a)
rayonIC = 1.96 * np.sqrt(p_naive*(1-p_naive)/M)

print "\t Valeur par Monte Carlo naif :", p_naive, "avec precision au risque 5%:", rayonIC 
print "\t Amplitude relative Monte Carlo naif :", 2 * rayonIC / p_naive

###########################################################################################
# En ponderant les trajectoires croissantes : Estimation via G(X)=e^{alpha (X_p-X_{p-1}) }
###########################################################################################
print "-" * 45
print "Ponderation des trajectoires croissantes"
# le calcul de ces poids necessite de garder en mémoire 
# l'instant courant et le premier passe.

# parametres des poids G_p
la = a/(n+1)
# X stocke l'instant courant et le precedent pour chacune des M particules 
# initialisation de X : X0 = 0 et X1 suit une loi N(0,1)
X = np.array([np.zeros(M), Y[:,0]]) 
X = X.T
# on stocke les indices de sélection de l'ancetre
indices = np.zeros(M)

estim_constante_normalisation = 1
for i in range(1,n):
    "Selection puis mutation en ponderant les trajectoires croissantes"
    # Calcul des poids non normalises Gp
    G = np.exp(la*(X[:,1]-X[:,0]))
    # Mise a jour de la constante de normalisation
    estim_constante_normalisation = estim_constante_normalisation*np.mean(G)
    # Selection de M ancetres, indep, avec poids G; avec repetition
    valeurs = np.arange(0,M)
    indices = np.random.choice(valeurs, size=M, p=G/np.sum(G)) 
    # Mise a jour des particules approchant eta_(i+1)
    # On stocke l'instant precedent et l'instant courant
    X[:,0] = X[indices,1]
    X[:,1] = X[:,0]+Y[:,i]
    
estimation_terme_1 = np.mean( (X[:,1]>=a)*np.exp( -la*X[:,0]) )
# Ici, la constante de normalisation se calcule explicitement :    
constante_normalisation = np.exp((n-1)*(la**2)/2) 
# Estimateur particule, constante exacte
estim_part_1 = estimation_terme_1 * constante_normalisation 
# Estimateur particule, constante estimee
estim_part_1_aux = estimation_terme_1 * estim_constante_normalisation


# Affichage
print "\t Constante de normalisation exacte : ", constante_normalisation
print "\t Constante de normalisation estimee : ", estim_constante_normalisation
print "\t Erreur relative ", np.abs(constante_normalisation-estim_constante_normalisation)/constante_normalisation
print "\n \t Estimation (avec normalisation exacte) : ", estim_part_1 
print "\t Estimation (avec normalisation estimee) : ", estim_part_1_aux 


###############################################################################
## En ponderant les trajectoires hautes : Estimation via G(X)=e^{alpha X_p}
###############################################################################
print "-" * 45
print "En ponderant les trajectoires hautes"

la = 2*a/(n*(n-1))

# Stockage des M particules successives, de longueur max n
X = np.zeros((M,n)) 
# Initialisation, approximation de eta_1
X[:,0] = Y[:,0] 
indices = np.zeros(M)

estim_constante_normalisation = 1
for i in range(0,n-1):
    "Selection puis mutation en ponderant les trajectoires hautes"
    # Calcul des poids des particules courantes
    G = np.exp(la*X[:,i])
    # Update de la constante de normalisation
    estim_constante_normalisation = estim_constante_normalisation * np.mean(G)
    # Sélection de M ancetres
    valeurs = np.arange(0,M)
    indices = np.random.choice(valeurs, size=M, p=G/sum(G)) 
    # Mise  a jour des particules, approximation de eta_(i+2)  
    X = X[indices,:]
    X[:,i+1] = X[:,i] + Y[:,i+1] 

# Calcul de l'estimateur du 1er terme
estimation_terme_1 = np.mean( (X[:,-1]>=a) * np.exp( -la * np.sum(X[:,:-1],1) )  )

# Ici, la constante de normalisation se calcule explicitement : 
constante_normalisation = np.exp(n*(n-1)*(2*n-1)*(la**2)/12)
# Calcul de l'estimateur avec constante exacte
estim_part_2 = estimation_terme_1*constante_normalisation
# Calcul de l'estimateur avec constante estimee
estim_part_2_aux = estimation_terme_1 * estim_constante_normalisation  



# Affichage
print "\t Constante de normalisation exacte ", constante_normalisation
print "\t Constante de normalisation estimee ", estim_constante_normalisation
print "\t Erreur relative ", np.abs(constante_normalisation-estim_constante_normalisation)/constante_normalisation
print "\n \t Estimation (avec normalisation exacte) =", estim_part_2
print "\t Estimation (avec normalisation estimee) =", estim_part_2_aux