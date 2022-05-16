# examples of object orientated programming concepts in python

# declaration of a class with a doc-string
class Animal():
    """
    The class for animals with atrributes of: 
    name, 
    weight,
    age; 
    and methods like: 
    move(), 
    eat(), 
    setName(), 
    getName()
    """
    def __init__(self, name='no name', weight= 1, age= 1):
        """
        initializes the animal class with default values of:
        name = 'no name'
        weight = 1
        age = 1
        """
        self._name = name # the underscore inidcates that this is a protected attribute
        self.weight = weight
        self.age = age
    
    def move(self):
        print("moving!")

    def eat(self):
        print("eating!")

    def setName(self, name):
        """
        setter method as variables should not be modified outside the class to avoid side-effects
        """
        self._name = name

    def getName(self):
        return self._name()

class Mammal(Animal):
    """
    class for mammals with inheritance from Animal() class
    """
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

class Bird(Animal):
    """
    the class for birds
    atrributes:
    name 
    weight
    age
    migrates
    flight
    methods:
    buildNest()
    move()
    in addition to inherited methods of Animal() class
    """
    def __init__(self, name='no name', weight=1, age=1, migrates=True, flight=True):
        super().__init__(name,weight,age) # super refers to the class which was inherited from. Here we define all the attributes from the inherited class.
        self.migratory = migrates # we can add new attributes
        self.flight = flight
    
    def buildNest(self): # we can add new methods seperate from the inherited class
        print("nest is building...")

    def move(self): # polymorphism; we can redefine methods from the inherited class.
        """
        polymorphic method redefining move() method from Animal() class
        """
        if self.flight:
            print("flying")
        else:
            super().move() # refers to the inherited version of the method



# creating instances of a class
whale = Mammal()
pidgeon = Bird()