from pathlib import Path
from random import *

def guardar_partida(laberinto):
    directorio_saves = Path(__file__).parent / "saves"
    directorio_saves.mkdir(exist_ok= True)
    
    archivo_guardado = directorio_saves / "save.txt"
    archivo_guardado.write_text(str(laberinto))
    return(f"Partida guardada en {archivo_guardado}")

def cargar_partida():
    directorio_saves = Path(__file__).parent / "saves"
    archivo_guardado = directorio_saves / "save.txt"
    
    if archivo_guardado.exists():
        return eval(archivo_guardado.read_text())
    else:
        print("No hay una partida guardada")
        return None
    
 
def dificultad_dificil():
    return ""
 
    
def crear_laberinto(dificultad):
    if dificultad == "facil":
        return [
    ['#', '#', '#', '#', '#'],
    ['#', 'P', '.', '.', '#'],
    ['#', '.', '#', '.', '#'],
    ['#', '.', '.', 'E', '#'],
    ['#', '#', '#', '#', '#']
]
    elif dificultad == "medio":
        return [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'P', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', 'E', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]
    elif dificultad == "dificil":
        return dificultad_dificil()
      
    
    
def mover_W(laberinto):
    for i, fila in enumerate(laberinto):
        if "P" in fila:
            indice_P = fila.index("P")
            if laberinto[i-1][indice_P] != "#":
                laberinto[i][indice_P] = "."
                laberinto[i-1][indice_P] = "P"
                break
    
def mover_A(laberinto):
    for i, fila in enumerate(laberinto):
        if "P" in fila:
            indice_P = fila.index("P")
            if laberinto[i][indice_P-1] != "#":
                laberinto[i][indice_P] = "."
                laberinto[i][indice_P-1] = "P"
                break

def mover_S(laberinto):
    for i, fila in enumerate(laberinto):
        if "P" in fila:
            indice_P = fila.index("P")
            if laberinto[i+1][indice_P] != "#":
                laberinto[i][indice_P] = "."
                laberinto[i+1][indice_P] = "P"
                break
    
    
def mover_D(laberinto):
    for i, fila in enumerate(laberinto):
        if "P" in fila:
            indice_P = fila.index("P")
            if laberinto[i][indice_P+1] != "#":
                laberinto[i][indice_P] = "."
                laberinto[i][indice_P+1] = "P"
                break