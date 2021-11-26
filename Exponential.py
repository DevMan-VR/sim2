from tkinter import *
import numpy as np 
from scipy import stats 
import time
from RandomGenerator import pseudorandom_generator

class ExponentialClass:
    def __init__(self, master=None, lambdaValue=None):
        self.master = master
        self.name = "Exponencial"
        self.lambdaValue = lambdaValue

        if(master != None):
            self.label1 = Label(master, text="lambda", height=4)
            self.input1 = Entry(master)
            self.label1.grid(column=0,row=1)
            self.input1.grid(column=1,row=1)
        
    
    def renderWidgets(self):
        self.label1.grid(column=0,row=1)
        self.input1.grid(column=1,row=1)

    def removeWidgets(self):
        self.label1.grid_remove()
        self.input1.grid_remove()

    def getLamb(self):
        self.lambdaValue = float(self.input1.get())
        print("Self Lamb is: ", self.lambdaValue)

    def random_gen_arr(self,size=100):

        rand = []
        for i in range(1,size):
            t = time.perf_counter()
            seed = int(10**9*float(str(t-int(t))[0:]))
            U = pseudorandom_generator(seed=seed)[0]
            X = -(1/self.lambdaValue)*(np.log(1-U))
            #print("U in exp is ")
            rand.append(X)

        return rand

    def random_gen(self):
        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        U = pseudorandom_generator(seed=seed)[0]
        X = -(1/self.lambdaValue)*(np.log(1-U))
            
        return X
