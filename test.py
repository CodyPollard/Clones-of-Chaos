import os, player, settings

class Test_Case():

    user = settings.SAVEGAME_PATH + "/root"
    root = player.PlayerInfo(user)


    def __init__(self):
        self.root.FormatInfo()


    def changerace(self):
        print("Testing changerace\n--------------------")
        print(self.root.set_race())
        print("End of test")


if __name__ == "__main__":
    t = Test_Case()
    t.changerace()