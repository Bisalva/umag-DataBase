from dataclasses import dataclass
from models import estudiante , prueba
# from time import 

@dataclass
class Calificacion :
    estudiante : estudiante
    prueba : prueba
    puntaje : float
    # fecha_calificacion : datetime??? - default : now 