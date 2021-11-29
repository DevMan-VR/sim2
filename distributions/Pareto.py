from tkinter import *
import numpy as np 
from scipy import stats 
import time
from .RandomGenerator import pseudorandom_generator

class ParetoClass:
    def __init__(self, alpha,xm):
        self.name = "Pareto"
        self.alpha = alpha
        self.xm = xm


    def random_gen(self):
        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        U = pseudorandom_generator(seed=seed)[0]
        X = (self.alpha * self.xm**(self.alpha))/(U*self.xm)**(self.xm+1)
            
        return X