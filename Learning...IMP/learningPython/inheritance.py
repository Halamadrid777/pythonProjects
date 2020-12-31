

# class animals(object):
#     def __init__(self, kingdom, levelOfOrganization, symmetry, coelom, phylum, scientific_name):
#         self.kingdom = kingdom
#         self.levelOfOrganization = levelOfOrganization
#         self.symmetry = symmetry
#         self.coelom = coelom
#         self.phylum = phylum
#         self.scientific_name = scientific_name


# class Animalia(animals):
#     def __init__(self, kingdom, levelOfOrganization, symmetry, coelom, phylum, scientific_name,habitat):
#         super().__init__(kingdom, levelOfOrganization, symmetry, coelom, phylum, scientific_name)
#         self.habitat = habitat


# earthworm = Animalia("Animalia", "tissue Organ System", "Bialateral","with true coelum", "Annelida", "Lumbricus terrestris","earth living" )
# print(earthworm.__dict__)


# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
class Person(object):


	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

	# To check if this person is an employee
	def isEmployee(self):
		return False




# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

	# Here we return true
	def isEmployee(self):
     return super().isEmployee()
     


# Driver code
emp = Person("Geek1") # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())
print(emp.display())
