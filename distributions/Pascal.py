from tkinter import *
import numpy as np 
from scipy import stats 
import time
from .RandomGenerator import pseudorandom_generator

class PascalClass:
    def __init__(self,k,m):
        self.name = "Pascal"
        self.k = k
        self.m = m
    
    def random_gen(self):
        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        U = pseudorandom_generator(seed=seed)[0]
        num=np.math.factorial(int(self.k)-1)/np.math.factorial(int(self.m-1))*np.math.factorial((int(self.k)-1)-(int(self.m)-1))
        X = (1-U)**(int(self.k)-int(self.m)) #Num fracasos (1-p)^(k-m)
        X = num * X * U #Probabilidad Pascal.

        return X
