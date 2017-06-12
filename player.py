import base

class PlayerInfo:
    # Variables for Player
    name = ""
    Race = ""
    ArmySize = 0
    ArmyStr = 0
    ArmyDef = 0
    SpyStr = 0
    SpyDef = 0

    def __init__(self, player):
        self.player = player

    def PrintPlayer(self):
        print(self.player)

    def FormatInfo(self):
        # Open playerinfo file
        f = open(self.player + "/playerinfo.txt", "r")
        print(f.read())


