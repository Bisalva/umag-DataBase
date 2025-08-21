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