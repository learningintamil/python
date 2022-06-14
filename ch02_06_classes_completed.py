#
# Learning in Tamil - Python 
# Example file - classes
#

class Computer():
    def __init__(self, bodyStyle):
        self.bodyStyle = bodyStyle

    def boot(self, speed ):
        self.mode  = "booting"
        self.speed  = speed 

class Desktop(Computer):
    def __init__(self, processorType):
        super().__init__("Desktop")
        self.camera = 0
        self.cdDrive = 2
        self.processor = processorType

    def boot(self, speed):
        super().boot(speed)
        print(self.bodyStyle, "Booting with", self.processor, "processor in", self.speed, "seconds")

class Laptop(Computer):
    def __init__(self, processorType, hasCamera):
        super().__init__("Laptop")
        if (hasCamera):
            self.camera = 1
        else:
            self.camera = 0
        self.cdDrive = 1
        self.processor = processorType

    def boot(self, speed):
        super().boot(speed)
        print(self.bodyStyle, "Booting with", self.processor, "processor in", self.speed, "seconds")

desktop1 = Desktop("AMD")
desktop2 = Desktop("intel")
laptop1 = Laptop("M1Pro", True)

print(laptop1.camera)
print(desktop1.processor)
print(desktop2.cdDrive)

desktop1.boot(10)
desktop2.boot(8)
laptop1.boot(5)
