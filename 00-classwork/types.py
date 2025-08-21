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