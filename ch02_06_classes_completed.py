#
# Learning in Tamil - Python 
# Example file - classes
#

class Animal():
    def __init__(self, name):
        self.name = name

    def walk(self, speed ):
        self.eats  = "food"
        self.speed  = speed 


class Dog(Animal):
    def __init__(self, animalType):
        super().__init__("Dog")
        self.age = 10
        self.legs = 4
        self.type = animalType

    def walk(self, speed):
        super().walk(speed)
        print("Walking ", self.type, " Dog at ", self.speed)


class Tiger(Animal):
    def __init__(self, animalType, age):
        if(age < 7):
            super().__init__("Tiger Cub")
        else:
            super().__init__("Tiger")
		
        self.legs = 4
        self.type = animalType

    def walk(self, speed):
        super().walk(speed)
        print("Walking ", self.type, " Tiger at ", self.speed)


dog1 = Dog("Farm")
dog2 = Dog("Wild")
tiger1 = Tiger("Wild", 5)

print(tiger1.age)
print(dog1.type)
print(dog2.legs)

dog1.walk(30)
dog2.walk(40)
tiger1.walk(50)
