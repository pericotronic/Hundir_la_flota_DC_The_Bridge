import numpy as np
from abc import abstractmethod
import random

from Constantes import DIMENSIONES_TABLERO, BARCOS,INTACT_BOAT_UNIT,HIT_BOAT_UNIT,EMPTY_SEA,HIT_SEA


def position_available_in_grid(position,grid) -> bool :
    """ Check if a position is in the grid and that there is no boat on it """
    x, y = position
    if 0 <= x < 10 and 0 <= y < 10 :
        return grid[x,y] == EMPTY_SEA
    return False

def random_boat_area(size): 
    random_index = random.randint(0, 10)
    first_area_index = random.randint(0, 10-size)
    consecutive_indexes = range(first_area_index, first_area_index + size)
    boat_area = []
    if random.choice([True, False]) : # Choose if the boat is place verticaly or horizontally
        # Vertical placement
        for i in consecutive_indexes :
            boat_area.append((random_index, i))
    else :
        # Horizontal placement
        for i in consecutive_indexes :
            boat_area.append((i, random_index))
    # The above lines can be compacted using zip (in library itertools)
    # and list comprehension but it makes it less readible
    return boat_area

#===-----------------------------------------------------------------
#===--- Solution ----------------------------------------------------
#===-----------------------------------------------------------------

def randomly_place_new_boat(size,grid) :
    while(True) :   # /!\ Potentially infinite loop
        boat_area = random_boat_area(size)
        if all([position_available_in_grid(p,grid) for p in boat_area]) : # Check if we can place a boat on the area
            for p in boat_area :
                grid[p[0], p[1]] = INTACT_BOAT_UNIT  # Place the boat 
            return


class Tablero:
    def __init__(self):
        #dimensiones del tablero
        self.filas, self.columnas = DIMENSIONES_TABLERO
        

        # Crear matrices de numpy para los barcos y los disparos
        self.barcos = np.zeros((self.filas, self.columnas), dtype=np.int8)
        self.colocar_barcos()
        """self.disparos = np.zeros((self.filas, self.columnas), dtype=np.int8)"""

    def colocar_barcos(self):
        # Colocar barcos aleatoriamente en el tablero
        for _, data in BARCOS.items():
            cantidad = data["numero"]
            eslora=data["eslora"]

            for _ in range(cantidad):
                randomly_place_new_boat(eslora,self.barcos)


    def disparar(self, fila, columna):
        # Comprobar si hay un barco en la coordenada indicada
        case_state=self.barcos[fila][columna]
        if case_state== HIT_BOAT_UNIT:
            print("Is already been shot") 
            return False
        elif case_state==EMPTY_SEA:
            self.barcos[fila][columna]=HIT_SEA
            return False    

        elif case_state==HIT_SEA:
            print("Ya ha sido impactado")
            return False    
        else:
            self.barcos[fila][columna]=HIT_BOAT_UNIT
            return True
            

    def mostrar(self):
        #Below code states machine´s board which will be displayed for didactic purposes
        print(self.barcos)  

        for f in range(self.filas):
            for c in range(self.columnas):
                case_state=self.barcos[f,c]
                if case_state==HIT_SEA:
                    print("O",end=" ")
                elif case_state==HIT_BOAT_UNIT:
                    print("x",end=" ")    
                else:
                    print("_",end=" ")        
            print(" ")
            

      

    def all_boats_sunk(self):
        for x in range(10):
            for y in range(10):
                if self.barcos[x,y]==INTACT_BOAT_UNIT:
                    return False
        return True
            











