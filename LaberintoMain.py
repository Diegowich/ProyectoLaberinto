from funciones import *

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
        case "g":
            print(guardar_partida(laberinto))
            
        
    