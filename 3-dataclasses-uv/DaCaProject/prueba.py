from dataclasses import dataclass
from calificacion import Calificacion
from datetime import date


@dataclass
class Prueba :
    id : int
    nombre : str
    materia : str
    tipo : str #parcial,final,quiz,tarea
    fecha : date
    puntaje_maximo : float
    peso_porcentual : float # 0-100
    calificaciones : list[Calificacion]