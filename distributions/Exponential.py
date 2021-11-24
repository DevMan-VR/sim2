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

    def renderVA(self):
        #Call VA from Normal Distribution and save as string
        self.lamb = float(self.input1.get())
        print("Self Lamb is: ", self.lamb)
        va = str(self.va_pseudo_exp_generate())

        self.input3.delete(0, 'end')
        self.input3.insert(END,va)


    def va_pseudo_exp_generate(size=100, lamb=1):

        rand = []
        for i in range(1,size):
            t = time.perf_counter()
            seed = int(10**9*float(str(t-int(t))[0:]))
            U = pseudorandom_generator(seed=seed)[0]
            X = -(1/lamb)*(np.log(1-U))
            #print("U in exp is ")
            rand.append(X)
            
        #print(U)

        return rand


    #Funcion de probabilidad de densidad
    def va_pseudo_exp_fpd(self,array): 

        X = np.zeros(array.size)
        for i in range(0,array.size-1):
            X[i] = (self.lamb) * np.exp((-self.lamb)*array[i])

        return X

    def va_pseudo_exp_fpa(self,x): 

        X = 1 - np.exp(-self.lamb*x)

        return X

    #Funcion de probabilidad acumulada
    def va_pseudo_exp_fpa_inverse(self,u): 

        X = -(1/self.lamb)*(np.log(1-u))

        return X

