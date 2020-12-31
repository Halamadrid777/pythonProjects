# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print("I am", self.name, "and I am", self.age, "years old")

#     def change_age(self, age):
#         self.age = age  # This changes the age attribute


# tim = Dog("Tim", 5)
# tim.change_age(8)
# tim.speak() 
# print(tim.__dict__) # This will print "I am Tim and I am 7 years old"



# class Animal():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 

#     def speak(self):
#         print("I am", self.name, "and I am", self.age, "years old")

#     def bark(self,quote):
#         print("Bark Bark!!!  "+quote)


# class Dog(Animal):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.type = "dog"

    

#     # Since we inherit from the animal class we can use the method speak on Dog objects


# timmy = Dog("Timmy", 5)
# timmy.speak() # This will print "I am Timmy and I am 5 years old" 
# timmy.bark("a journey of thousand miles start  with a single step")

class Veichle:
    def __init__(self, price, color):
        self.color = color
        self.price = price
        self.gas = 0

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas


class Truck(Veichle):
    def __init__(self, price, color, tires):
        super().__init__(price, color)
        self.tires = tires

    def beep(self):
        print("Honk honk")


class Car(Veichle):
    def __init__(self, price, color, speed):
        super().__init__(price, color)
        self.speed = speed

    def beep(self):
        print("Beep Beep")

