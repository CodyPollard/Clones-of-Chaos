import sqlite3 as lite
import unitinfo as unit
import os, settings


# Class used for AFTER game creation. Use CreatePlayer() if a save doesn't exist.
class PlayerInfo(object):

    # Accepts an existing player's savegame path
    def __init__(self, savepath):
        self.savepath = savepath
        self.gameinfo_path = savepath+'/gameinfo.db'
        self.playerinfo_path = savepath+'/playerinfo.db'
        # gameinfo.db variables
        self.playername, self.race, self.gold = "", "", ""
        # playerinfo.db variables
        self.unitCounts = list()
        self.armyCount, self.soldierCount, self.guardCount = 0, 0, 0
        self.espionageCount, self.spyCount, self.sentryCount = 0, 0, 0
        self.siegeCount = 0
        # Attack and Defense stats
        self.soldierStr, self.guardStr = 0, 0
        self.spyStr, self.sentryStr = 0, 0

        # Update info from DB
        self.update_gameinfo()
        self.update_playerinfo()

    def get_name(self):
        pass

    def update_gameinfo(self):
        print("Running update_gameinfo")
        # Create db connection
        con = lite.connect(self.gameinfo_path)
        with con:
            cur = con.cursor()
            cur.execute('SELECT Name from Players WHERE Id=1')
            self.playername = ''.join(cur.fetchone())
            cur.execute('SELECT Race from Players WHERE Id=1')
            self.race = ''.join(cur.fetchone())
            cur.execute('SELECT Gold from Players WHERE Id=1')
            self.gold = ''.join(cur.fetchone())

    def update_playerinfo(self):
        print("Running update_playerinfo")
        # Create db connection
        con = lite.connect(self.playerinfo_path)
        with con:
            cur = con.cursor()
            # Update army counts
            cur.execute('SELECT Amount from UnitInfo WHERE Id=1')
            record = cur.fetchall()
            for result in record:
                self.unitCounts.append(result[0])
            # Assign values from list
            self.soldierCount = self.unitCounts[0]
            self.guardCount = self.unitCounts[1]
            self.armyCount = self.guardCount+self.soldierCount
            # Clear the list
            self.unitCounts = []
            # Update espionage counts
            cur.execute('SELECT Amount from UnitInfo WHERE Id=2')
            record = cur.fetchall()
            for result in record:
                self.unitCounts.append(result[0])
            # Assign values from list
            self.spyCount = self.unitCounts[0]
            self.sentryCount = self.unitCounts[1]
            # Assign unit strengths
            self.soldierStr = self.soldierCount * unit.Soldier.strength
            self.guardStr = self.guardCount * unit.Guard.strength
            self.spyStr = self.spyCount * unit.Spy.strength
            self.sentryStr = self.sentryCount * unit.Sentry.strength




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
                cur.execute("CREATE TABLE Players(Id INT, Name TEXT, Race TEXT, Gold TEXT)")
                cur.execute("INSERT INTO Players VALUES(1, ?, ?, '5000')", (self.pname, race))
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
                cur.execute("CREATE TABLE UnitInfo(Id INT, Name TEXT, Amount INT)")
                cur.execute("INSERT INTO UnitInfo VALUES(1, 'Soldier', 50)")
                cur.execute("INSERT INTO UnitInfo VALUES(1, 'Guard', 20)")
                cur.execute("INSERT INTO UnitInfo VALUES(2, 'Spy', 10)")
                cur.execute("INSERT INTO UnitInfo VALUES(2, 'Sentry', 10)")
                cur.execute("INSERT INTO UnitInfo VALUES(3, 'Siege', 5)")
                # Equipment
                cur.execute("CREATE TABLE SoldierEquipment(Id INT, Name TEXT, Amount INT)")
                cur.execute("INSERT INTO SoldierEquipment VALUES(1, 'Sword', 20)")
                cur.execute("INSERT INTO SoldierEquipment VALUES(2, 'Flail', 0)")
                cur.execute("INSERT INTO SoldierEquipment VALUES(3, 'Spear', 0)")
                cur.execute("INSERT INTO SoldierEquipment VALUES(4, 'Poleaxe', 0)")
                cur.execute("INSERT INTO SoldierEquipment VALUES(5, 'Greatsword', 0)")
                # Espionage Equipment
                cur.execute("CREATE TABLE EspionageEquipment(Id INT, Name TEXT, Amount INT)")
                cur.execute("INSERT INTO EspionageEquipment VALUES(1, 'Rope', 5)")
                cur.execute("INSERT INTO EspionageEquipment VALUES(2, 'Cloak', 0)")
                cur.execute("INSERT INTO EspionageEquipment VALUES(3, 'Daggers', 0)")
                cur.execute("INSERT INTO EspionageEquipment VALUES(4, 'Lockpick', 0)")
                cur.execute("INSERT INTO EspionageEquipment VALUES(5, 'Grapple', 0)")
                # Castle Stats. Can have multiple castles?
                cur.execute("CREATE TABLE CastleStats(Id INT, Name TEXT, Location TEXT, Defense INT)")
                cur.execute("INSERT INTO CastleStats VALUES(1, 'My Castle', 'Random Location', 100)")
                # Castle Upgrades
                cur.execute("CREATE TABLE CastleUpgrades(Id INT, Name TEXT, Amount INT)")
                cur.execute("INSERT INTO CastleUpgrades VALUES(1, 'Palisades', 0)")
                cur.execute("INSERT INTO CastleUpgrades VALUES(2, 'Stockades', 0)")
                cur.execute("INSERT INTO CastleUpgrades VALUES(3, 'Stone Walls', 0)")
                cur.execute("INSERT INTO CastleUpgrades VALUES(4, 'Reinforced Walls', 0)")
                cur.execute("INSERT INTO CastleUpgrades VALUES(5, 'Portcullis', 0)")
                cur.execute("INSERT INTO CastleUpgrades VALUES(6, 'Turrets', 0)")
                cur.execute("INSERT INTO CastleUpgrades VALUES(7, 'Burning Oil', 0)")
                cur.execute("INSERT INTO CastleUpgrades VALUES(8, 'Moat', 0)")

        print("Player Initialized Succesfully!")



# Run player.py to run these tests
if __name__ == "__main__":
    c = PlayerInfo("/home/cody/Desktop/Projects/ClonesOfChaos/SaveGames/root")
    print(c.savepath)
    c.update_playerinfo()