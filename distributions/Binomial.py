from tkinter import *
import numpy as np 
from scipy import stats 
import time
from .RandomGenerator import pseudorandom_generator

class BinomialClass:
    def __init__(self, n,m):
        self.name = "Binomial"
        self.n = n
        self.m = m



    def random_gen(self):
        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        U = pseudorandom_generator(seed=seed)[0]
        num = np.math.factorial(self.n)/np.math.factorial(self.m)*np.math.factorial(self.n-self.m)
        X = (num * U) * (1-U)**(self.n-self.m)
            
        return X