
items = [
    {"nombre": "Laptop", "precio": 800000, "categoria": "Tecnología"},
    {"nombre": "Mouse", "precio": 15000, "categoria": "Tecnología"},
    {"nombre": "Escritorio", "precio": 120000, "categoria": "Muebles"},
    {"nombre": "Silla", "precio": 80000, "categoria": "Muebles"}
]


def items_analisys(items):
    amounts = [count['precio'] for count in items]
    total_amount = sum(amounts)
    avarage = total_amount / 4

    print("Prices : ", amounts, "\nAvarage : ", avarage)

    sort_item(items)


def sort_item(items):
    sort = sorted(items, key=lambda x:x['precio'],reverse=True)
    print("Most Expensive Item",sort[:1])


items_analisys(items)