from abc import abstractmethod
from Tablero import Tablero
import random


class Jugador:
    def __init__(self,nombre:str):
        self.nombre=nombre
        self.tablero=Tablero()

    def disparo_acertado(self,disparo_correcto): 
        pass   


    @abstractmethod
    def dar_coordenadas_de_disparo(self):
        ...
        
class JugadorHumano(Jugador):
    def __init__(self):
        super().__init__("human")

    def dar_coordenadas_de_disparo(self):
        fila = int(input('Introduce fila (0-9): '))
        columna = int(input('Introduce columna (0-9): ')) 
        return (fila,columna)
                
class NivelFacil(Jugador):
    def __init__(self):
        super().__init__("DumbAI")

    def dar_coordenadas_de_disparo(self):
        fila = random.randint(0, 10)
        columna = random.randint(0, 10)
        return (fila,columna)