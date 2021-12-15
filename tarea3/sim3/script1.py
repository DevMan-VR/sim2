import os
import time

lineas1 = []
lineas2 = []
lineas3 = []

file = open("marta-email-size.1.txt", "r")

for line in file.readlines():
    lineas1.append(line)

for line in lineas1:
    var = []
    var.append(line.split(" "))
    #print(var)
    lineas2.append(var[0][0])
    lineas3.append(var[0][1])

