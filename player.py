# PlayerInfo class handles all things related to a players stats and Army
class PlayerInfo:
    # Variables for Player
    lineArray = []
    playerValues = []
    Name = ""
    Race = ""
    ArmySize = 0
    ArmyStr = 0
    ArmyDef = 0
    SpyStr = 0
    SpyDef = 0

    # Accepts the filepath for playerinfo from base.py and reads the contents
    # into an array
    def __init__(self, player):
        self.player = player
        with open(self.player + "/playerinfo.txt", "r") as f:
            for i in f:
                self.lineArray = f.read().splitlines()

    def PrintPlayer(self):
        print(self.player)

    def FormatInfo(self):
        for i, list in enumerate(self.lineArray):
            test = self.lineArray[i].split('=')
            self.playerValues.append(test[1])

        # Format into class variables
        self.Name = self.playerValues[0]
        self.Race = self.playerValues[1]
        self.ArmySize = self.playerValues[2]
        self.ArmyStr = self.playerValues[3]
        self.ArmyDef = self.playerValues[4]
        self.SpyStr = self.playerValues[5]
        self.SpyDef = self.playerValues[6]

    def PrintInfo(self):
        print(self.Name)
        print(self.Race)
        print(self.ArmyDef)
        print(self.SpyDef)
        print(self.SpyStr)


