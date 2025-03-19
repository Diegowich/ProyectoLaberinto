from pathlib import Path

def guardar_partida(laberinto):
    directorio_saves = Path(__file__).parent / "saves"
    directorio_saves.mkdir(exist_ok= True)
    
    archivo_guardado = directorio_saves / "save.txt"
    archivo_guardado.write_text(str(laberinto))
    return f"Partida guardada en {archivo_guardado}"

def cargar_partida():
    directorio_saves = Path(__file__).parent / "saves"
    archivo_guardado = directorio_saves / "save.txt"
    
    if archivo_guardado.exists():
        return eval(archivo_guardado.read_text())
    else:
        print("No hay una partida guardada")
        return None
    
 
def dificultad_dificil():
     return "e"
 
    
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
        dificultad_dificil()