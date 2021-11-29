from tkinter import *
import numpy as np 
from scipy import stats 
import time
import math
from .RandomGenerator import pseudorandom_generator

class NormalClass:
    def __init__(self, mu, ro):
        self.name = "Normal"
        self.mu = mu
        self.ro = ro


#Cambiar:
    def va_pseudo_exp_generate(size=100):
        #Para este caso size representa la media y lamb la desv. estandar de la funcion
        size = 3
        lamb = 0.154
        num = (2*math.pi)**(1/2)
        rand = []
        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        U = pseudorandom_generator(seed=seed)[0]
        X = (1/(num*lamb)) * np.exp(-1*((U-size)**2)/(2*lamb**2))
        #print("U in exp is ")
        rand.append(X)

        return rand

    def random_gen(self):
        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        num = (2*math.pi)**(1/2)
        U = pseudorandom_generator(seed=seed)[0]
        U = pseudorandom_generator(seed=seed)[0]
        X = (1/(num*self.ro)) * np.exp(-1*((U-self.mu)**2)/(2*self.ro**2))
            
        return X