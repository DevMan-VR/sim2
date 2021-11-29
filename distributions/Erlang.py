from tkinter import *
import numpy as np 
from scipy import stats 
import time
from .RandomGenerator import pseudorandom_generator

class ErlangClass:
    def __init__(self,n,lamb):
        self.name = "Erlang"
        self.n = n
        self.lamb = lamb


    def random_gen(self):
        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        U = pseudorandom_generator(seed=seed)[0]
        X = (self.lamb*((self.lamb*U)**(self.n-1))*np.exp(-self.lamb*U))/np.math.factorial(self.n-1)

        return X
