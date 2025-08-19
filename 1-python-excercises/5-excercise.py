
shop_list = [
    ["Cafe",1000],
    ["Cereal",3000]
]

def calculate_total_shop(shop_list):
    item_prices = [get_price[1] for get_price in shop_list]
    print("Final Price : ",sum(item_prices))


def add_item(shop_list,name,price):
    new_items = [name,price]
    shop_list.append(new_items)


print(shop_list)
calculate_total_shop(shop_list)
add_item(shop_list,"pan",1200)
print(shop_list)
calculate_total_shop(shop_list)
