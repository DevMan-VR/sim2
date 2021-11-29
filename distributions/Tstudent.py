from tkinter import *
import numpy as np 
from scipy import stats 
import time
import math
from .RandomGenerator import pseudorandom_generator

class TstudentClass:
    def __init__(self, v):
        self.name = "T-student"
        self.v = v


    def random_gen(self):
        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        num = (self.v * np.pi)**(1/2)
        U = pseudorandom_generator(seed=seed)[0]
        X = math.gamma((self.v+1)/2)/(math.gamma(self.v/2) * num)
        X = X * (1 + (U**2)/self.v)**(-1*((self.v+1)/2))
            
        return X