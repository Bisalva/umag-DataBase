from dataclasses import dataclass
from datetime import datetime
from estudiante import Estudiante
from prueba import Prueba

@dataclass
class Calificacion :
    estudiante : Estudiante
    prueba : Prueba
    puntaje : float
    fecha_calificacion : datetime 