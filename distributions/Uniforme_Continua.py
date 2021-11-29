from tkinter import *
import numpy as np 
from scipy import stats 
import time
from .RandomGenerator import pseudorandom_generator

class UniformeContinuaClass:
    def __init__(self, a,b):
        self.name = "Uniforme Continua"
        self.a = a
        self.b = b

#Cambiar:
    def va_pseudo_exp_generate(size=100, lamb=1):

        rand = []
        a= 5 #Limites del arreglo (Parametros)
        b= 15
        for i in range(1,size+1):
            if(i < a):
                X=0
            elif(i >= b):
                X=1 #El valor esta fuera del rango
            else:
                X=1/(b-a)

            rand.append(X)

        return rand

    def random_gen(self):

        a= 5 #Limites del arreglo (Parametros)
        b= 15
        for i in range(1,21):
            if(i < a):
                X=0
            elif(i >= b):
                X=1 #El valor esta fuera del rango
            else:
                X=1/(b-a)
            
        return X