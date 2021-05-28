class Car:
    def __init__(self,color,registration,mileage,speed):
        self.color=color
        self.registration=registration
        self.mileage=mileage
        self.speed=speed
    def set_speed(self):
        return f"this car moves at {self.speed}"
    def car_color(self):
        return f"My sister's car is {self.color} in color"


