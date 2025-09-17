class Vehicle:
    def __init__(self,name,max_speed):
        self.name=name
        self.max_speed=max_speed
    def drive(self):
        print("Driving a Vehicle")
class Car(Vehicle):
    def drive(self):
        print(f"Driving a {self.name} at {self.max_speed} km/h")
class Bike(Vehicle):
    def drive(self):
        print(f"Driving a {self.name} at {self.max_speed} km/h")
vehicles = [
    Car("Toyota", 180),
    Bike("Yamaha", 120),
]
for v in vehicles:
    v.drive()