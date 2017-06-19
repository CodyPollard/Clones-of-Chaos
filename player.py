import sqlite3 as lite
import os, settings


class PlayerInfo(object):
    pass

class CreatePlayer():

    def __init__(self, pname):
        self.pname = pname
        self.filepath = settings.SAVEGAME_PATH + "/" + pname

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

    def initialize_player(self):
        path = self.filepath+'playerinfo.db'
        if os.path.isfile(path):
            print("This database already exists!")
        else:
            con = lite.connect(path)
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE OffensiveInfo(Id INT, Name TEXT, Strength INT, HP INT, Amount INT)")
                cur.execute("INSERT INTO OffensiveInfo VALUES(1, 'Footman', 1, 5, 20)")
                cur.execute("INSERT INTO OffensiveInfo VALUES(2, 'Archer', 3, 10, 5)")
                cur.execute("INSERT INTO OffensiveInfo VALUES(3, 'Knight', 5, 20, 0)")
                cur.execute("INSERT INTO OffensiveInfo VALUES(4, 'Royal Guard', 20, 50, 0)")

# Run player.py to run these tests
if __name__ == "__main__":
    c = CreatePlayer("default")
    print(c.filepath)
    c.initialize_game("Dwarf")
    # c.initialize_player()