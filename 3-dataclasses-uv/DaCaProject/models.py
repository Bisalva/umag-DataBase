from dataclasses import dataclass
from datetime import datetime
from datetime import date
import pandas as pd


@dataclass
class Estudiante :
    id : int
    nombre : str
    apellido : str
    email : str
    fecha_nacimiento : str
    carrera : "Carrera"
    semestre_actual : int
    fecha_ingreso : int


@dataclass
class Calificacion :
    estudiante : Estudiante
    prueba : "Prueba"
    puntaje : float
    fecha_calificacion : datetime 


@dataclass
class Carrera :
    codigo : str
    nombre : str
    facultad : str
    duracion_semestres : str


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

    