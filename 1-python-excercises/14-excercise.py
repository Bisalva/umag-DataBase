# IN Base de datos 2 work is a shorter versions
# this comment is after I finish the code and search for compare the solution

messages = [
    "2024-01-15 10:30:45 Usuario conectado correctamente",
    "2024-01-15 10:31:12 Error al conectar usuario",
    "2024-01-15 10:31:45 Usuario desconectado",
    "2024-01-15 10:32:01 Error de sistema crítico"
]

def process_messages(messages):
    errors = 0
    message_list = []
    for message in messages:
        parts = message.split(" ",2)
        if len(parts) == 3:
            date, hour, messa = parts

            if messa.lower().startswith("error"):
                errors += 1

            message_list.append({
                "fecha" : date,
                "hora" : hour,
                "mensaje" : messa
            })
    return f"Mensajes : {message_list}" , "Errores : " , {errors}



print(process_messages(messages))
