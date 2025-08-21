
# los tipos es una mejora de calidad de vida

name : str = "diego"
edad : int = 12

def send_hello(name: str | None = None)  -> str:
    if name is not None:
        if isinstance(name,list):
            for n in name:
                print(f"Hala {n}")
            return
        print(f"Hola,{name}")
    print("Hola")

send_hello(["Diego","Alan"])

def found_item(lista : list[int], elemento : int) -> int | None :
    if elemento in lista:
        return lista.index(elemento)

print(found_item([1,2,3,4,5,6],4))


def avegare_results(res : dict[str,int | float]) -> int | float :
    add = sum(res.values())
    return add / len(res)

print(
    avegare_results({
    "pedro" : 12,
    "juan" : 10,
    "diego" : 20,
}))


# tuplas
t : tuple[int,int,int] = (1,2,3)


class Persona:
    def __init__(self,name : str, age : int) -> None:
        self.name = name
        self.age = age
    
    def salute(self) -> str:
        """Envia un saludo""" #Añade documentacion
        return f"Hola, soy {self.name} y tengo {self.age} años"
    

def print_info(persona : Persona) -> None:
    print(persona.salute())


def carga_personas() -> list[Persona]:
    datos = []
    datos.append(Persona("Diego",30))
    datos.append(Persona("juan",20))
    datos.append(Persona("pedro",10))

    return datos

p = carga_personas()
#p. trabaja como lista, p[0]. trabaja con indice de una persona
# se usa "Persona" si se declara un metodo antes que la clase

# example
class A:
    def __init__(self, b : list["B"]) -> None:
        self.b = b

class B:
    def __init__(self, a : A) -> None:
        self.a = a


def AddExample(a: int, b : int) -> int:
    return a+b

resExample = AddExample(10,12)
print(resExample)