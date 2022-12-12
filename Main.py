
from Jugador import Jugador, JugadorHumano , NivelFacil




def playturn(current_player:Jugador, enemy:Jugador):

    while True:
        # Pedir al jugador 1 que introduzca coordenadas de disparo
        print()
        enemy.tablero.mostrar()
        fila, columna= current_player.dar_coordenadas_de_disparo()
        # Disparar al jugador 2 y mostrar resultado
        impacto = enemy.tablero.disparar(fila, columna)
        #Con la siguiente linea de codigo le doy a la AI informacion sobre si ha sido acertado o no.
        current_player.disparo_acertado(impacto)
        
        if impacto:
            print("Impacto!")
            if enemy.tablero.all_boats_sunk():
                break
            print(f"{current_player.nombre} Juegas otra vez")
            continue #Si impacto se repite el turno para el jugador de turno    
        else:
            print("You missed, dispara la máquina")
            break        




if __name__ == '__main__':

     # Inicializar tableros de jugadores
     # I have two player, one is a human player, and i make it play agaisnt an easy AI.(36,37)
     # While there is no winner I alterate each player with the other.
     # Until there is a winner when the function playturn() will return a Boolean value(True) 
     # indicating that there is a winner

    jugador1=JugadorHumano()
    jugador2=NivelFacil()
    # Mostrar mensaje inicial y tableros de ambos jugadores
    print('Bienvenido al juego del Hundir la Flota!')
    print()

    current_player=jugador1
    other_player=jugador2

    # Bucle principal del juego
    while True:
        playturn(current_player,other_player)
        if other_player.tablero.all_boats_sunk():
            print(f"{current_player.nombre} player won!")
            break
        current_player,other_player=other_player,current_player
        #  Lo que digo aqui es juega una parte y luego
        #  simplemente se intercambia con la otra.
        #  Esto es basicamente el juego"""
        






   
            

    






