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
        super().__init__(name,weight,age) # super refers to the class which was inherited from always. 
        self.migratory = migrates
        self.flight = flight
    
    def buildNest(self):
        print("nest is building...")

    