from funciones import *
from os import system

volver_jugar = ""
while volver_jugar != "n":
    print("Bienvenido al laberinto")
    print("Tu objetivo es llegar a la salida 'E'")


    tiene_partida_guardada = input("Tienes una partida guardada? (s/n): ")
    if tiene_partida_guardada == "s":
        laberinto = cargar_partida()
    else:
        dificultad = input("Selecciona la dificultad (facil, medio, dificil): ")
        laberinto = crear_laberinto(dificultad)
        

    eleccion_usuario = ""

    while eleccion_usuario != "end":
        for fila in laberinto:
            print(" ".join(fila))
        
        eleccion_usuario = input(""" 'W' (arriba) 'A'(izquierda) 'S'(abajo) 'D'(derecha) 'G' (Guardar progreso), 'end' (Salir)"
    Selecciona una opcion: """).lower().strip()
        
        match eleccion_usuario:
            case "w":
                mover_W(laberinto)
                system("cls")
                
            case "a":
                mover_A(laberinto)
                system("cls")
            case "s":
                mover_S(laberinto)
                system("cls")
            case "d":
                mover_D(laberinto)
                system("cls")
            case "g":
                mensaje = guardar_partida(laberinto)
                system("cls")
                print(mensaje)
                
            case "end":
                system("cls")
                print("Gracias por jugar")
            
        if laberinto[-2][-2] == "P":
            print("Felicidades, has llegado a la salida")
            borrar_guardado()
            break
                
    volver_jugar = input("Quieres volver a jugar? (s/n): ")
    system("cls")
    print("Hasta luego")

        
        
        
    