

def evaluate_grade(grade):
    if grade > 6.0:
        print("Aprobado con Distincion")
    elif grade > 4.0:
        print("Aprobado")
    else:
        print("Reprobado")

evaluate_grade(5.0)
evaluate_grade(6.5)
evaluate_grade(3.0)