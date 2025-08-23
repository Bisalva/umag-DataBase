
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
pair_list = []
pow_list = []
div_list = []

def number_filter(list):
    for number_index in range(len(list)+1):
        if number_index % 2 == 0:
            pair_list.append(number_index)
        elif number_index % 2 != 0:
            pow_list.append(number_index*number_index)

        if number_index % 3 == 0:
            div_list.append(number_index)

# BETTER WAY
#    pares = [n for n in lista_numeros if n % 2 == 0]
#    cuadrados_impares = [n**2 for n in lista_numeros if n % 2 != 0]
#    divisibles_3 = [n for n in lista_numeros if n % 3 == 0]      
      
number_filter(numbers)

print(pair_list)
print(pow_list)
print(div_list)