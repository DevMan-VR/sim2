from tkinter import *
import numpy as np 
from scipy import stats 
import time
from .RandomGenerator import pseudorandom_generator

class BernoulliClass:
    def __init__(self):
        self.name = "Bernoulli"


#Cambiar:
    def va_pseudo_exp_generate(size=100):

        rand = []
        for i in range(0,size):
            t = time.perf_counter()
            seed = int(10**9*float(str(t-int(t))[0:]))
            U = pseudorandom_generator(seed=seed)[0]
            if (U>=0.5):
                X=1
            else:
                X=0
            rand.append(X)

        return rand

    def random_gen(self):
        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        U = pseudorandom_generator(seed=seed)[0]
        if (U>=0.5):
            X=1
        else:
            X=0
            
        return X