# examples of object orientated programming concepts in python

class Animal():

    """The class for animals"""
    def __init__(self, name='no name', weight= 1, age= 1):
        self._name = name # the underscore inidcates that this is a procted attribute
        self.weight = weight
        self.age = age
    
    def move(self):
        pass

    def eat(self):
        pass

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name()

class Bird(Animal):
    def __init__(self, name='no name', weight=1, age=1, migrates=True, flight=True):
        super().__init__(name,weight,age) # super refers to the class which was inherited from. Here we define all the attributes from the inherited class.
        self.migratory = migrates # we can add new attributes
        self.flight = flight
    
    def buildNest(self): # we can add new methods seperate from the inherited class
        print("nest is building...")

    def move(self): # we can also redefine methods from the inherited class. this is called polymorphism.
        if self.flight:
            print("flying")
        else:
            super.move() # refers to the inherited version of the method

class Mammal(Animal):
    def __init__(self, name='no name', weight=1, age=1, water=False, eatsMeat=True):
        super().__init__(name, weight, age)
        self.livesInWater = water
        self.carnivore = eatsMeat
    
    def breath(self):
        print("breathing...")

    def eat(self):
        if self.carnivore:
            print('eating meat')
        else:
            super().eat()