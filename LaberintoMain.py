from funciones import * 
from os import system 

volver_jugar = ""  # Volver a jugar inicia vacio

while volver_jugar != "n":  # Mientras volver a jugar no sea n, se ejecutara el juego
    print("Bienvenido al laberinto")        
    print("Tu objetivo es llegar a la salida 'E'")

    tiene_partida_guardada = input("Tienes una partida guardada? (s/n): ").lower().strip()  # Preguntamos si tiene una partida guardada
    
    while tiene_partida_guardada not in ["s", "n"]:  # Mientras la respuesta no sea s o n, se seguira preguntando
        print("Respuesta no valida")
        tiene_partida_guardada = input("Tienes una partida guardada? (s/n): ").lower().strip()

    if tiene_partida_guardada == "s":
        laberinto = cargar_partida()
        if laberinto is None:
            print("No hay una partida guardada")
            dificultad = input("Selecciona la dificultad del laberinto (facil, medio, dificil): ").lower().strip()
            while dificultad not in ["facil", "medio", "dificil"]:  # Mientras la dificultad no sea facil, medio o dificil, se seguira preguntando
                print("Respuesta no valida")
                dificultad = input("Selecciona la dificultad del laberinto (facil, medio, dificil): ").lower().strip()
            laberinto = crear_laberinto(dificultad)  # Se crea el laberinto segun la dificultad seleccionada
    elif tiene_partida_guardada == "n":
        dificultad = input("Selecciona la dificultad del laberinto (facil, medio, dificil): ").lower().strip()  # Selecciona la dificultad del laberinto
        while dificultad not in ["facil", "medio", "dificil"]:  # Mientras la dificultad no sea facil, medio o dificil, se seguira preguntando
            print("Respuesta no valida")
            dificultad = input("Selecciona la dificultad del laberinto (facil, medio, dificil): ").lower().strip()
        laberinto = crear_laberinto(dificultad)  # Se crea el laberinto segun la dificultad seleccionada

    eleccion_usuario = ""  # La eleccion del usuario inicia vacia

    while eleccion_usuario != "end":  # Mientras el usuario no escriba end en la eleccion, se ejecutara el juego
        for fila in laberinto:
            print(" ".join(fila))  # Se imprime el laberinto seleccionado
        
        eleccion_usuario = input(""" 'W' (arriba) 'A'(izquierda) 'S'(abajo) 'D'(derecha) 'G' (Guardar progreso), 'end' (Salir)"
    Selecciona una opcion: """).lower().strip()  # Se pide la eleccion del usuario
        
        match eleccion_usuario:
            case "w":  # Si la eleccion del usuario es w, se mueve hacia arriba
                mover_W(laberinto)
                system("cls")  # system cls limpia la pantalla para mostrar el laberinto tras el movimiento hecho
                
            case "a":  # si la eleccion del usuario es a, se mueve hacia la izquierda
                mover_A(laberinto)
                system("cls")  # system cls limpia la pantalla para mostrar el laberinto tras el movimiento hecho
            case "s":  # si la eleccion del usuario es s, se mueve hacia abajo
                mover_S(laberinto)
                system("cls")  # system cls limpia la pantalla para mostrar el laberinto tras el movimiento hecho
            case "d":  # si la eleccion del usuario es d, se mueve hacia la derecha
                mover_D(laberinto)
                system("cls")  # system cls limpia la pantalla para mostrar el laberinto tras el movimiento hecho
            case "g":  # si la eleccion del usuario es g, se guarda la partida
                mensaje = guardar_partida(laberinto)
                system("cls")  # system cls limpia la pantalla para mostrar el mensaje de guardado a continuacion
                print(mensaje)  # Se imprime el mensaje de guardado
                
            case "end":  # si la eleccion del usuario es end, termina el juego antes de llegar a la salida
                system("cls")  # Se limpia la pantalla
                print("Gracias por jugar")  # Se imprime un mensaje de despedida
            
        if laberinto[-2][-2] == "P":  # Si la posicion del jugador es igual a la salida, se imprime un mensaje de felicitacion
            print("Felicidades, has llegado a la salida")
            borrar_guardado()  # Se borra la partida guardada
            break  # Se rompe el ciclo while
    
    # Este apartado soluciona errores si el usuario termino el juego escribiendo end y volvio a cargar su partida y llego a la salida
            
    volver_jugar = input("Quieres volver a jugar? (s/n): ").strip().lower()  # Se pregunta si quiere volver a jugar
    while volver_jugar not in ["s", "n"]: # Pregunta si quiere volver a jugar
        print("Respuesta no valida")
        volver_jugar = input("Quieres volver a jugar? (s/n): ").lower().strip()
    system("cls")  # Se limpia la pantalla
    if volver_jugar == "n":
        print("Hasta luego")  # Si no quiere volver a jugar, se imprime un mensaje de despedida
        break



