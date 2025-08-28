from dataclasses import dataclass
from models import calificacion


@dataclass
class Prueba :
    id : int
    nombre : str
    materia : str
    tipo : str #parcial,final,quiz,tarea
    fecha : int #date ???
    puntaje_maximo : float
    peso_porcentual : float # 0-100
    #calificaciones : List[calificacion] ???