import os.path, fileinput, sys
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
    def __init__(self, player, pname):
        # Passed variables are the player's profile folder and player's name
        self.player = player + "/playerinfo.txt"
        self.pname = pname
        # When an instance of PlayerInfo is created, checks to see if the profile already exists.
        # Otherwise it creates one.
        if os.path.isfile(self.player):
            with open(self.player, "r") as f:
                for i in f:
                    self.lineArray = f.read().splitlines()
        else:
            self.initialize_player()

    # Takes playerinfo.txt and reads their stats into class variables for the PlayerInfo object
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

    # Used to print a player's stats
    def printinfo(self):
        print(self.Name)
        print(self.Race)
        print(self.ArmyDef)
        print(self.SpyDef)
        print(self.SpyStr)

    # Creates a playerinfo.txt for the user if none exists
    def initialize_player(self):
        f = open(self.player, "w")
        f.write("### Player info file contains values for player stats ###\n")
        f.write("Name=" + self.pname + "\n")
        f.write("Race=\n")
        f.write("ArmySize=100\n")
        f.write("ArmyStr=10\n")
        f.write("ArmyDef=10\n")
        f.write("SpyStr=10\n")
        f.write("SpyDef=10")
        f.close()

    def set_race(self, race):
        for line in fileinput.input(self.player, inplace=1):
            if "Race=" in line:
                print("Race="+race)
            else:
                sys.stdout.write(line)