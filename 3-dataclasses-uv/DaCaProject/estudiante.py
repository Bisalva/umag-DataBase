from dataclasses import dataclass
from carrera import Carrera


@dataclass
class Estudiante :
    id : int
    nombre : str
    apellido : str
    email : str
    fecha_nacimiento : str
    carrera : Carrera
    semestre_actual : int
    fecha_ingreso : int