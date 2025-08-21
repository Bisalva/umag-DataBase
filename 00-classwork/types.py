name : str = "diego"
edad : int = 12

def send_hello(name: str | None = None)  -> str:
    if name is not None:
        return f"Hola,{name}"
    return "Hola"

print(send_hello())