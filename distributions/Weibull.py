from tkinter import *
import numpy as np 
from scipy import stats 
import time
from .RandomGenerator import pseudorandom_generator

class WeibullClass:
    def __init__(self,tasa_fallos,lamb):
        self.name = "Weibull"
        self.tasa_fallos = tasa_fallos
        self.lamb = lamb

    
    def random_gen(self):
        t = time.perf_counter()
        a=0.3 #Parametro de entrada, indica la tasa de fallos
        seed = int(10**9*float(str(t-int(t))[0:]))
        U = pseudorandom_generator(seed=seed)[0]
        X = (self.lamb*self.tasa_fallos)*((self.lamb*U)**(self.tasa_fallos-1))*np.exp(-((self.lamb*U)**self.tasa_fallos))
            
        return X

        