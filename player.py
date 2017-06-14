import os.path
# PlayerInfo class handles all things related to a players stats and Army


class PlayerInfo(object):

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
        self.player = player + "/playerinfo.txt"
        if os.path.isfile(self.player):
            with open(self.player, "r") as f:
                for i in f:
                    self.lineArray = f.read().splitlines()
        else:
            self.initialize_player()


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

    def initialize_player(self):
        f = open(self.player, "w")
        f.write("### Player info file contains values for player stats ###\n")
        f.write("Name=\n")
        f.write("Race=\n")
        f.write("ArmySize=100\n")
        f.write("ArmyStr=10\n")
        f.write("ArmyDef=10\n")
        f.write("SpyStr=10\n")
        f.write("SpyDef=10")
        f.close()