from tkinter import *
import numpy as np 
from scipy import stats 
import time
from .RandomGenerator import pseudorandom_generator

class GeometricaClass:
    def __init__(self, k):
        self.name = "Geometrica"
        self.k =k



    def va_pseudo_exp_generate(size=6):

        rand = []
        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        U = pseudorandom_generator(seed=seed)[0] #Probabilidad de exito P
        for i in range(0,size):
            X = (1-U)**(size-1) #Num fracasos (1-p)^(k-1)
            X = X * U #Probabilidad Geometrica.
            #print("U in exp is ")
            rand.append(X)

        return rand

    def random_gen(self):
        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        U = pseudorandom_generator(seed=seed)[0] #Probabilidad de exito P
        X = (1-U)**(self.k-1) #Num fracasos (1-p)^(k-1)
        X = X * U #Probabilidad Geometrica.

        return X