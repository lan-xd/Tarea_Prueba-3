import numpy as np
 
filas = 10
columnas = 10

x = np.zeros([filas,columnas])

for i in range(filas):
    for j in range(columnas):
        a = i+1
        b = j+1
        x[i,j] = 1

print(x)