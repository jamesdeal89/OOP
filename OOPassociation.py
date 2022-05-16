# python example of association in OOP

class Player():
    """
    the class for players which has attributes of: name, age, skill.
    and methods of: move().
    """
    def __init__(self, name, age, skillLevel) -> None:
        self.name = name
        self.age = age
        self.skill = skillLevel

    def move():
        print("moving")


class Team():
    """
    the class for teams which is made of associated aggregated players.
    has the methods:
    addPlayer() - adds a player of type player,
    printPlayers() - prints all the players names,
    """
    def __init__(self) -> None:
        self.allPlayers = []
    
    def addPlayer(self, player):
        self.allPlayers.append(player)

    def printPlayers(self):
        for player in self.allPlayers:
            print(player.name)

manUnited = Team()
ronaldo = Player("Ronaldo", 38, "extreme")
manUnited.addPlayer(ronaldo)