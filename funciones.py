from pathlib import Path            # Importamos la librería Path para crear el directorio y el archivo de guardado
from random import *                # Importamos la funcion random para generar el mapa aleatorio

def guardar_partida(laberinto):                         # Funcion para guardar la partida, que recibe el tipo de laberinto
    directorio_saves = Path(__file__).parent / "saves"  # Se establece el directorio en donde se guardara la partida, se llamara saves
    directorio_saves.mkdir(exist_ok= True)              # Se crea el directorio si no existe
    
    archivo_guardado = directorio_saves / "save.txt"    # Se establece el archivo de guardado, se llamara save.txt
    archivo_guardado.write_text(str(laberinto))         # Se escribe el laberinto en el archivo de guardado como un string
    return(f"Partida guardada en {archivo_guardado}")   # Se devuelve un mensaje de guardado con la ruta del archivo, para notificar al jugador donde se guardo su partida

def cargar_partida():   # Funcion para cargar la partida
    directorio_saves = Path(__file__).parent / "saves"      # Se establece la ruta donde debera encontrar el archivo de guardado
    archivo_guardado = directorio_saves / "save.txt"        # El archivo de guardado que debe buscar es save.txt
    
    if archivo_guardado.exists():                   # Si el archivo de guardado existe 
        return eval(archivo_guardado.read_text())       # Se devuelve el contenido del archivo de guardado como una lista
    else:
        print("No hay una partida guardada")            # Si no hay una partida guardada, se notifica que no hay una partida guardada
        return None                                     # retorna None para que el programa principal sepa que no hay una partida guardada
    
def borrar_guardado():                      # Funcion para borrar la partida guardada
    directorio_saves = Path(__file__).parent / "saves"  # Se indica el directorio donde se guardo la partida
    archivo_guardado = directorio_saves / "save.txt"    # se indica cual es el archivo de guardado que debe buscar
    
    if archivo_guardado.exists():               # Si el archivo de guardado existe
        archivo_guardado.unlink()               # Se borra el archivo de guardado
        return "Partida borrada"                # Se devuelve un mensaje de que la partida fue borrada
    else:
        return "No hay una partida guardada"    # Si no hay una partida guardada, se devuelve un mensaje de que no hay una partida guardada
    
 
def dificultad_dificil():           # Funcion para crear laberinto dificultad dificil
    return ""
 
    
def crear_laberinto(dificultad):        # Funcion para crear el laberinto segun la dificultad seleccionada
    if dificultad == "facil":           # El laberinto recibe como parametro la dificultad seleccionada
        return [                    
    ['#', '#', '#', '#', '#'],          # Si el usuario escribe facil, se retorna un laberinto facil
    ['#', 'P', '.', '.', '#'],
    ['#', '.', '#', '.', '#'],
    ['#', '.', '.', 'E', '#'],
    ['#', '#', '#', '#', '#']
]
    elif dificultad == "medio":         # Si el usuario escribe medio, se retorna un laberinto medio
        return [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'P', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', 'E', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]
    elif dificultad == "dificil":           # Si el usuario escribe dificil, se retorna un laberinto dificil
        return dificultad_dificil()
      
    
    
def mover_W(laberinto):                     # Funcion para mover al jugador hacia arriba
    for i, fila in enumerate(laberinto):
        if "P" in fila:                     # Se busca la posicion del jugador en el laberinto
            indice_P = fila.index("P")      # Se obtiene el indice del jugador en la fila
            if laberinto[i-1][indice_P] != "#": # Si la posicion de arriba del jugador no es una pared
                laberinto[i][indice_P] = "."    # Se cambia la posicion del jugador a un espacio vacio
                laberinto[i-1][indice_P] = "P"  # Se cambia la posicion de arriba del jugador a la posicion del jugador
                break
    
def mover_A(laberinto):                     # Funcion para mover al jugador hacia la izquierda
    for i, fila in enumerate(laberinto):    
        if "P" in fila:                     # Se busca la posicion del jugador en el laberinto
            indice_P = fila.index("P")      # Se obtiene el indice del jugador en la fila
            if laberinto[i][indice_P-1] != "#": # Si la posicion de la izquierda del jugador no es una pared
                laberinto[i][indice_P] = "."    # Se cambia la posicion del jugador a un espacio vacio
                laberinto[i][indice_P-1] = "P"  # Se cambia la posicion de la izquierda del jugador a la posicion del jugador
                break

def mover_S(laberinto):                     # Funcion para mover al jugador hacia abajo
    for i, fila in enumerate(laberinto):   
        if "P" in fila:                     # Se busca la posicion del jugador en el laberinto
            indice_P = fila.index("P")      # Se obtiene el indice del jugador en la fila
            if laberinto[i+1][indice_P] != "#": # Si la posicion de abajo del jugador no es una pared
                laberinto[i][indice_P] = "."    # Se cambia la posicion del jugador a un espacio vacio
                laberinto[i+1][indice_P] = "P"  # Se cambia la posicion de abajo del jugador a la posicion del jugador
                break
    
    
def mover_D(laberinto):                 # Funcion para mover al jugador hacia la derecha
    for i, fila in enumerate(laberinto):
        if "P" in fila:                 # Se busca la posicion del jugador en el laberinto
            indice_P = fila.index("P")  # Se obtiene el indice del jugador en la fila
            if laberinto[i][indice_P+1] != "#": # Si la posicion de la derecha del jugador no es una pared
                laberinto[i][indice_P] = "."    # Se cambia la posicion del jugador a un espacio vacio
                laberinto[i][indice_P+1] = "P"  # Se cambia la posicion de la derecha del jugador a la posicion del jugador
                break