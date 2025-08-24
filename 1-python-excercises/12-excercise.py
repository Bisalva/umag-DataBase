
fruits = ["manzana", "sandia", "frutilla"]


def get_first_last_fruit(fruits):
    return f"primera fruta : {fruits[0]} ; ultima fruta : {fruits[len(fruits)-1]}"

def add_fruit(fruits,new_fruit):
    fruits.append(new_fruit)

def get_fruit_list(fruits):
    print(fruits)


print(get_first_last_fruit(fruits))
get_fruit_list(fruits)
add_fruit(fruits,"pera")
print(get_first_last_fruit(fruits))
get_fruit_list(fruits)

