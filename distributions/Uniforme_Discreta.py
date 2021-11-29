from tkinter import *
import numpy as np 
from scipy import stats 
import time
from .RandomGenerator import pseudorandom_generator

class UniformeDiscretaClass:
    def __init__(self, n):
       # self.master = master
        #self.label1 = Label(master, text="lambda", height=4)
        #self.input1 = Entry(master)
        self.name = "Uniforme Discreta"
        self.n = n
    
    def renderWidgets(self):
        self.label1.grid(column=0,row=1)
        self.input1.grid(column=1,row=1)

    def removeWidgets(self):
        self.label1.grid_remove()
        self.input1.grid_remove()

#Cambiar:
    def va_pseudo_exp_generate(size=100, lamb=1):

        rand = []
        for i in range(1,size):
            X = 1/size
            #print("U in exp is ")
            rand.append(X)

        return rand
    
    def random_gen(self):
        X = 1/self.n
            
        return X