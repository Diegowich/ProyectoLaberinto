from funciones import * 
from os import system  # Importamos la funcion system del modulo os para limpiar la pantalla

volver_jugar = ""       # Volver a jugar inicia vacio
while volver_jugar != "n":      # Mientras volver a jugar no sea n, se ejecutara el juego
    print("Bienvenido al laberinto")        
    print("Tu objetivo es llegar a la salida 'E'")


    tiene_partida_guardada = input("Tienes una partida guardada? (s/n): ")  # Preguntamos si tiene una partida guardada
    if tiene_partida_guardada == "s":     # Si tiene una partida guardada, cargamos la partida
        laberinto = cargar_partida()
    else:                                   # Si no tiene una partida guardada, creamos un laberinto nuevo
        dificultad = input("Selecciona la dificultad (facil, medio, dificil): ")
        laberinto = crear_laberinto(dificultad)         # Creamos el laberinto segun la dificultad seleccionada
        

    eleccion_usuario = ""     # La eleccion del usuario inicia vacia

    while eleccion_usuario != "end":  # Mientras el usuario no escriba end en la eleccion, se ejecutara el juego
        for fila in laberinto:
            print(" ".join(fila))    # Se imprime el laberinto seleccionado
        
        eleccion_usuario = input(""" 'W' (arriba) 'A'(izquierda) 'S'(abajo) 'D'(derecha) 'G' (Guardar progreso), 'end' (Salir)"
    Selecciona una opcion: """).lower().strip()    # Se pide la eleccion del usuario
        
        match eleccion_usuario:
            case "w":               # Si la eleccion del usuario es w, se mueve hacia arriba
                mover_W(laberinto)
                system("cls")           # system cls limpia la pantalla para mostrar el laberinto tras el movimiento hecho
                
            case "a":               # si la eleccion del usuario es a, se mueve hacia la izquierda
                mover_A(laberinto)
                system("cls")       # system cls limpia la pantalla para mostrar el laberinto tras el movimiento hecho
            case "s":               # si la eleccion del usuario es s, se mueve hacia abajo
                mover_S(laberinto)
                system("cls")       # system cls limpia la pantalla para mostrar el laberinto tras el movimiento hecho
            case "d":               # si la eleccion del usuario es d, se mueve hacia la derecha
                mover_D(laberinto)
                system("cls")       # system cls limpia la pantalla para mostrar el laberinto tras el movimiento hecho
            case "g":               # si la eleccion del usuario es g, se guarda la partida
                mensaje = guardar_partida(laberinto)
                system("cls")       # system cls limpia la pantalla para mostrar el mensaje de guardado a continuacion
                print(mensaje)      # Se imprime el mensaje de guardado
                
            case "end":             # si la eleccion del usuario es end, termina el juego antes de llegar a la salida
                system("cls")               # Se limpia la pantalla
                print("Gracias por jugar")  # Se imprime un mensaje de despedida
            
        if laberinto[-2][-2] == "P":        # Si la posicion del jugador es igual a la salida, se imprime un mensaje de felicitacion
            print("Felicidades, has llegado a la salida")
            borrar_guardado()                 # Se borra la partida guardada
            break   # Se rompe el ciclo while
                
    volver_jugar = input("Quieres volver a jugar? (s/n): ")   # Se pregunta si se quiere volver a jugar
    system("cls")       # Se limpia la pantalla
    print("Hasta luego")        # Si no quiere volver a jugar, se imprime un mensaje de despedida

        
        
        
    