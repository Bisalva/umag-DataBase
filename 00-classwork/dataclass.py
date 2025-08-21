from dataclasses import dataclass
from typing import Any
from math import sqrt

class Punto2:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


    def __repr__(self) -> str:
        return f"Punto(x={self.x}, y ={self.y})"

    def __eq__(self, value: Any) -> bool:
        return self.x == value.x and self.y == value.y
    

#froze evita modificacion , normalmente desactivado
@dataclass(eq=True, order=True, frozen=False)
class Punto:
    x: int
    y: int

    def __post_init__(self):
        self.x = self.x **2

    # se pueden agregar nuestros propias clases
    def origin_distance(self) -> float:
        return sqrt(self.x**2 + self.y**2)
    
@dataclass
class Poligono:
    vertices: list[Punto]

p1 = Punto(1,4)
p2 = Punto(3,4)

print(p1)
print(p1 == p2)
print(sorted([p2,p1]))
print(p1.origin_distance())

poligono = Poligono([p1,p2,Punto[10,10]])