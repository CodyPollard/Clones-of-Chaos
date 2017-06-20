import sqlite3 as lite
import os, settings

# Class used for AFTER game creation. Use CreatePlayer() if a save doesn't exist.
class PlayerInfo(object):

    # Accepts an existing player's savegame path
    def __init__(self, savepath):
        self.savepath = savepath
        self.gameinfo_path = savepath+'/gameinfo.db'
        self.playerinfo_path = savepath+'/playerinfo.db'
        # gameinfo.db variables
        self.playername, self.race = "", ""
        # playerinfo.db variables
        self.armyCount, self.soldierCount, self.guardCount = 0, 0, 0
        self.espionageCount, self.spyCount, self.sentryCount = 0, 0, 0
        self.siegeCount = 0

        # Update info from DB
        self.update_gameinfo()

    def get_name(self):
        pass

    def update_gameinfo(self):
        print("Running update_gameinfo")
        # Create db connection
        con = lite.connect(self.gameinfo_path)
        with con:
            cur = con.cursor()
            cur.execute('SELECT Name from Players WHERE Id=1')
            self.playername = cur.fetchone()


# Class used to create and initialize a game if it doesn't exist.
class CreatePlayer():

    def __init__(self, pname):
        self.pname = pname
        self.savepath = settings.SAVEGAME_PATH + "/" + pname

    # Checks to see if database exist and creates all database needed for a fresh game
    def initialize_game(self, race):
        path = self.savepath + '/gameinfo.db'
        if os.path.isfile(path):
            print("This database already exists!")
        else:
            os.makedirs(self.savepath)
            con = lite.connect(path)
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE Players(Id INT, Name TEXT, Race TEXT)")
                cur.execute("INSERT INTO Players VALUES(1, ?, ?)", (self.pname, race))
        print("Game Created!")

    # Checks to see if database exist for the player and creates them
    def initialize_player(self):
        path = self.savepath + '/playerinfo.db'
        if os.path.isfile(path):
            print("This database already exists!")
        else:
            con = lite.connect(path)
            with con:
                cur = con.cursor()
                # Units
                cur.execute("CREATE TABLE UnitInfo(Id INT, Name TEXT, BaseStrength INT, BaseHP INT, Amount INT)")
                cur.execute("INSERT INTO UnitInfo VALUES(1, 'Soldier', 5, 20, 20)")
                cur.execute("INSERT INTO UnitInfo VALUES(1, 'Guard', 5, 20, 20)")
                cur.execute("INSERT INTO UnitInfo VALUES(2, 'Spy', 5, 20, 10)")
                cur.execute("INSERT INTO UnitInfo VALUES(2, 'Sentry', 5, 20, 10)")
                cur.execute("INSERT INTO UnitInfo VALUES(3, 'Siege', 15, 50, 5)")
                # Equipment
                cur.execute("CREATE TABLE SoldierEquipment(Id INT, Name TEXT, Modifier INT, Amount INT)")
                cur.execute("INSERT INTO SoldierEquipment VALUES(1, 'Sword', 1.5, 20)")
                cur.execute("INSERT INTO SoldierEquipment VALUES(2, 'Flail', 3, 0)")
                cur.execute("INSERT INTO SoldierEquipment VALUES(3, 'Poleaxe', 5, 0)")
                cur.execute("INSERT INTO SoldierEquipment VALUES(4, 'Greatsword', 20, 0)")
                # Espionage Equipment
                cur.execute("CREATE TABLE EspionageEquipment(Id INT, Name TEXT, Modifier INT, Amount INT)")
                cur.execute("INSERT INTO EspionageEquipment VALUES(1, 'Rope', 1.5, 10)")
                cur.execute("INSERT INTO EspionageEquipment VALUES(2, 'Cloak', 3, 0)")
                cur.execute("INSERT INTO EspionageEquipment VALUES(3, 'Daggers', 5, 0)")
                cur.execute("INSERT INTO EspionageEquipment VALUES(4, 'Grapple', 20, 0)")
                # Castle Stats. Can have multiple castles?
                cur.execute("CREATE TABLE CastleStats(Id INT, Name TEXT, Location TEXT, Defense INT)")
                cur.execute("INSERT INTO CastleStats VALUES(1, 'My Castle Name', 'Randomly Generated Name', 100)")
                # Castle Upgrades
                cur.execute("CREATE TABLE CastleUpgrades(Id INT, Name TEXT, Modifier INT, Amount INT)")
                cur.execute("INSERT INTO CastleUpgrades VALUES(1, 'Reinforced Walls', 2, 0)")
                cur.execute("INSERT INTO CastleUpgrades VALUES(2, 'Archers', 4, 0)")
                cur.execute("INSERT INTO CastleUpgrades VALUES(3, 'Burning Oil', 8, 0)")
                cur.execute("INSERT INTO CastleUpgrades VALUES(4, 'Moat', 15, 0)")

        print("Player Initialized Succesfully!")



# Run player.py to run these tests
if __name__ == "__main__":
    c = PlayerInfo("/home/cody/Desktop/Projects/ClonesOfChaos/SaveGames/root")
    print(c.savepath)
    c.update_gameinfo()
    print(c.playername)