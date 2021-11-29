from tkinter import *
import numpy as np 
from scipy import stats 
import time
from .RandomGenerator import pseudorandom_generator

class PoissonClass:
    def __init__(self, lamb, k):

        self.name = "Poisson"
        self.lamb = lamb
        self.k = k
    

    def random_gen(self):
        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        U = pseudorandom_generator(seed=seed)[0]
        X = (np.exp(-self.lamb) * self.lamb**self.k)/np.math.factorial(self.k)
            
        return X