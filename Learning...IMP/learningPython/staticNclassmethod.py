# # when using @staticmethor or @classmethod you don't have to create any object(variables) to use any of the methods
# # also we don't need the SELF paramater like any other regural method
# class person(object):
#     population = 50
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     @staticmethod
#     def isAdult(age):
#         return age>=18

#     @classmethod
#     def getPopulation(cls):
#         return cls.population


#     def  display(self):
#         print(self.name, "is",self.age,"years old")

# new_person = person("Tim",18)

# print(new_person.getPopulation())

# print(person.getPopulation())

# # print(new_person.isAdult())
# print(person.isAdult(18))



###***###

class veichles(object):
    def __init__(self,name,type,wheels,seats):
        self.name = name
        self.type = type
        self.wheels = wheels
        self.seats = seats

    @staticmethod
    def isFourWheelers(wheels):
        return wheels == 4

    @staticmethod
    def isForFamily(seats):
        return seats >=4


LaFerrari = veichles("La Ferrari","car",4,2)
londonBus = veichles("long bus","bus",6,50)
RangeRover = veichles("Range rover Sports","car",4,4)


print(RangeRover.__dict__)
print(londonBus.isFourWheelers())

###***###

class myClass:
    count = 0

    def __init__(self):
        self.x = x

    @classmethod
    def classMethod(cls):  
        cls.count += 1
         
print(myClass.classMethod())
# The classMethod can access and modify class variables. It takes the class name as a required parameter