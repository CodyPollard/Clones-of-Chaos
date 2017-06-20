import sqlite3 as lite
import os, settings


class PlayerInfo(object):
    pass

class CreatePlayer():

    def __init__(self, pname):
        self.pname = pname
        self.filepath = settings.SAVEGAME_PATH + "/" + pname

    # Checks to see if database exist and creates all database needed for a fresh game
    def initialize_game(self, race):
        path = self.filepath+'/gameinfo.db'
        if os.path.isfile(path):
            print("This database already exists!")
        else:
            os.makedirs(self.filepath)
            con = lite.connect(path)
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE Players(Id INT, Name TEXT, Race TEXT)")
                cur.execute("INSERT INTO Players VALUES(1, ?, ?)", (self.pname, race))

    # Checks to see if database exist for the player and creates them
    def initialize_player(self):
        path = self.filepath+'/playerinfo.db'
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
                cur.execute("INSERT INTO UnitInfo VALUES(2, 'Sentry', 5, 20, 10)")
                cur.execute("INSERT INTO UnitInfo VALUES(2, 'Lookout', 5, 20, 10)")
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

# Run player.py to run these tests
if __name__ == "__main__":
    c = CreatePlayer("root")
    print(c.filepath)
    c.initialize_game("Elf")
    c.initialize_player()