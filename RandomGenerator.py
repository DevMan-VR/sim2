import numpy as np
import time

#Revisar
def pseudorandom_generator(seed=123456789,size=1, mult=16807,mod=(2**31)-1):
    U = np.zeros(size)
    x = (seed*mult)%mod
    U[0] = x/mod
    for i in range(1,size):
        x =(x*mult)%mod
        U[i] = x/mod
    return U

def pseudo_uniforme_continua(low=0, high=1, seed=73372, size=1):
    return low+(high-low)*pseudorandom_generator(seed=seed, size=size)[0]


def pseudo_uniforme_discreta(seed=12381923, size=1):
    return int(pseudorandom_generator(seed,size))

#print("Pseudorandom generator Uniform is: ")
#t = time.perf_counter()
#seed1 = int(10**9*float(str(t-int(t))[0:]))
#print(float(pseudo_uniform()))
#print(float(pseudorandom_generator(16807,(2**31)-1,seed1,1)))
#Es continuo uniforme