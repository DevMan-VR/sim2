from tkinter import *
import numpy as np 
from scipy import stats 
import time
import math
from .RandomGenerator import pseudorandom_generator

class NormalStandardClass:
    def __init__(self, mu, ro):
        self.name = "Normal Estandar"
        self.mu = mu
        self.ro = ro

#Cambiar:
    def va_pseudo_exp_generate(size=100, lamb=1):
        #Para este caso size representa la media y lamb la desv. estandar de la funcion
        size = 3
        lamb = 0.154
        num = (2*math.pi)**(1/2)
        rand = []
        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        U = pseudorandom_generator(seed=seed)[0]
        X = (1/(num*lamb)) * np.exp(-1*((1-size)**2)/(2*lamb**2))
        Z = (X-size)/lamb 
        #print("U in exp is ")
        rand.append(X)
        rand.append(Z)

        return rand
    
    def random_gen(self):
        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        num = (2*math.pi)**(1/2)
        U = pseudorandom_generator(seed=seed)[0]
        X = (1/(num*self.mu)) * np.exp(-1*((U-self.ro)**2)/(2*self.mu**2))
        Z = (X-self.ro)/self.mu
            
        return Z
        