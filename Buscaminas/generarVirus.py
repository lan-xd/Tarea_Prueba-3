import numpy as np

cantVirusFacil = 5
cantVirusMedio = 9
cantVirusDificil = 16


class generarVirus:
    
    
    filas = 16
    columnas = 16

    matriz = np.zeros([filas,columnas])

    for i in range(filas):
        for j in range(columnas):
            a = i+1
            b = j+1
            matriz[i,j] = 0

    print(matriz)

    def asignarVirus(self, dificultad):
        
        for i in range(dificultad):
            randX = np.random.randint(0,self.filas - 1)
            randY = np.random.randint(0,self.columnas - 1)
            self.matriz[randX,randY] = '1'
        print(self.matriz)


test = generarVirus()
test.asignarVirus(cantVirusDificil)