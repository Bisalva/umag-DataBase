
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def turn_on(self):
        print(f"The vehicle is on")
    
    def __str__(self):
        return f"Brand : {self.brand}; Model : {self.model}; Year : {self.year}"
    
class Car(Vehicle):
    def __init__(self, brand, model, year, door_num):
        super().__init__(brand, model, year)
        self.number_doors = door_num

    def turn_on(self):
        print("The car is on")

class Motorbike(Vehicle):
    def __init__(self, brand, model, year, cylinder_capacity):
        super().__init__(brand, model, year)
        self.cylinder = cylinder_capacity

    def turn_on(self):
        print("The motorbike is on")

def vehichle_test(vehicle):
    vehicle.turn_on()
    print(vehicle)

car = Car("Toyota", "Corolla", 2020, 4)
bike = Motorbike("Honda", "CBR", 2021, 600)

vehicles = [car, bike]
for vehicle in vehicles:
    vehichle_test(vehicle)