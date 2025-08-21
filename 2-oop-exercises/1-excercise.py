
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def show_info(self):
        print(f"Product: {self.name}, Price: {self.price}, Stock: {self.stock}")
    
    def apply_discount(self, percentage):
        discount = self.price * (percentage / 100)
        self.price -= discount
        print(f"New price in {self.name} with a discount : {self.price:.0f}")

    def sell(self, amount):
        if amount <= self.stock:
            self.stock -= amount
            print(f"{amount} {self.name} sold. Stock : {self.stock}")
        else:
            print(f"There is no stock enough {amount} of {self.name}. Stock : {self.stock}")

product = Product("Laptop", 800000, 5)
product.show_info()
product.apply_discount(10)
product.sell(2)