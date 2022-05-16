
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
    """
    def __init__(self) -> None:
        self.allPlayers = []
    
    def addPlayer(self, player):
        self.addPlayer.append(player)