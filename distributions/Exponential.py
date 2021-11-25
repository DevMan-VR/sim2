from tkinter import *
import numpy as np 
from scipy import stats 
import time
from .RandomGenerator import pseudorandom_generator

class ExponentialClass:
    def __init__(self, master):
        self.master = master
        self.label1 = Label(master, text="lambda", height=4)
        self.input1 = Entry(master)
        self.name = "Exponencial"
        self.label1.grid(column=0,row=1)
        self.input1.grid(column=1,row=1)
    
    def renderWidgets(self):
        self.label1.grid(column=0,row=1)
        self.input1.grid(column=1,row=1)

    def removeWidgets(self):
        self.label1.grid_remove()
        self.input1.grid_remove()

    def getLamb(self):
        self.lamb = float(self.input1.get())
        print("Self Lamb is: ", self.lamb)

    def va_pseudo_exp_generate(size=100, lamb=1):

        rand = []
        for i in range(1,size):
            t = time.perf_counter()
            seed = int(10**9*float(str(t-int(t))[0:]))
            U = pseudorandom_generator(seed=seed)[0]
            X = -(1/lamb)*(np.log(1-U))
            #print("U in exp is ")
            rand.append(X)

        return rand
