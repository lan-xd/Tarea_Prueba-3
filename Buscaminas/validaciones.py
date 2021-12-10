
#Validaciones de el bloque seleccionado


class validaciones:
    def __init__(self):
        pass
    def validar_posicion(self, posX, posY):
        if self.cuadro(posX,posY) == 'X':
            
            print("Ha tocado una mina")
            return False
        else:
            print("Continuar jugando")
            return True    
        
        