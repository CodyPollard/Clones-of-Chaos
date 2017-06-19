import settings, os, player
import tkinter


# Main player screen. Used after Login is successful
class Base(tkinter.Tk):
    # Base class constructor
    def __init__(self, master, PlayerInfo):
        tkinter.Tk.__init__(self, master)
        self.master = master
        self.p = PlayerInfo
        self.main_window()

    # Accepts the PlayerInfo object from log_in after a user successfuly logs in
    def main_window(self):
        # Create window
        self.title(self.p.Name)
        self.grid()
        self.geometry("+600+350")
        labelTop = tkinter.Label(self, anchor="w", fg="black", text="Your Stats")
        labelTop.grid(column=0, row=0, columnspan=4)
        # Left column
        labelRace = tkinter.Label(self, anchor="w", fg="black", text="Race: ")
        labelRace.grid(column=0, row=1)
        labelArmy = tkinter.Label(self, anchor="w", fg="black", text="Army Size: ")
        labelArmy.grid(column=0, row=2)
        labelAstr = tkinter.Label(self, anchor="w", fg="black", text="Army Strength: ")
        labelAstr.grid(column=0, row=3)
        labelAdef = tkinter.Label(self, anchor="w", fg="black", text="Army Defense: ")
        labelAdef.grid(column=0, row=4)
        labelSpyStr = tkinter.Label(self, anchor="w", fg="black", text="Spy Strength: ")
        labelSpyStr.grid(column=0, row=5)
        labelSpyDef = tkinter.Label(self, anchor="w", fg="black", text="Spy Defense: ")
        labelSpyDef.grid(column=0, row=6)
        # Right column
        dataRace = tkinter.Label(self, anchor="e", text=self.p.Race)
        dataRace.grid(column=1, row=1)
        dataArmy = tkinter.Label(self, anchor="e", text=self.p.ArmySize)
        dataArmy.grid(column=1, row=2)
        dataAstr = tkinter.Label(self, anchor="e", text=self.p.ArmyStr)
        dataAstr.grid(column=1, row=3)
        dataAdef = tkinter.Label(self, anchor="e", text=self.p.ArmyDef)
        dataAdef.grid(column=1, row=4)
        dataSpyStr = tkinter.Label(self, anchor="e", text=self.p.SpyStr)
        dataSpyStr.grid(column=1, row=5)
        dataSpyDef = tkinter.Label(self, anchor="e", text=self.p.SpyDef)
        dataSpyDef.grid(column=1, row=6)


# Login class handles creation and continuation of player profiles
class Login(tkinter.Tk):

    # Base class constructor.
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.log_in()

    # initialize used to create widgets an instance of Base is created
    def log_in(self):
        # Create the parent grid and configure the column/row weights
        self.grid()
        self.minsize(width=0, height=0)
        self.columnconfigure(0, weight=1)
        # Create widgets below
        label = tkinter.Label(self, anchor="w", fg="black", text="Clones of Chaos")
        label.grid(column=0, row=0, columnspan=2, sticky="")
        # Log in widgets
        userlabel = tkinter.Label(self, pady=10, text="Username:")
        userlabel.grid(column=0, row=1, sticky="w")
        self.userfield = tkinter.Entry(self)
        self.userfield.grid(column=1, row=1, sticky="w")
        self.userfield.focus_set()
        login = tkinter.Button(self, text="Log in", anchor="s", command=self.load_game)
        login.grid(column=0, row=2, columnspan=2, sticky="we")


    def load_game(self):
        # Local Variables
        u = settings.SAVEGAME_PATH + "/" + self.userfield.get().lower()
        # Check if player's profile exists when logging in. If not, create it.
        if os.path.isdir(u):
            p = player.PlayerInfo(u)
            p.FormatInfo()
            Base(None, p)
            self.destroy()
        else:
            self.new_game_prompt(u)

    # Display new game prompt if user profile doesn't exist
    def new_game_prompt(self, u):
        # Prompt user for profile creation
        self.newgamePrompt = tkinter.Toplevel(self)
        l = tkinter.Label(self.newgamePrompt, text="That profile does not exist, would you like to create it?")
        # Buttons
        yesBtn = tkinter.Button(self.newgamePrompt, text="Yes", command=lambda: self.create_profile(u))
        noBtn = tkinter.Button(self.newgamePrompt, text="No", command=self.newgamePrompt.destroy)
        # Create window and widgets
        self.newgamePrompt.grid()
        self.newgamePrompt.geometry("+600+350")
        l.grid()
        yesBtn.grid()
        noBtn.grid()

    def create_profile(self, u):
        pname = self.userfield.get()
        os.mkdir(u)
        p = player.PlayerInfo(u, pname)
        self.select_race(p)
        # Destroy the newgameprompt
        self.newgamePrompt.destroy()

    def select_race(self, p):
        # Create window
        self.selectrace = tkinter.Toplevel(self)
        self.selectrace.title()
        self.selectrace.grid()
        self.selectrace.geometry("+600+350")
        labelTop = tkinter.Label(self.selectrace, anchor="w", fg="black", text="Choose Your Race")
        labelTop.grid(column=0, row=0, columnspan=4)
        # Buttons
        humanBtn = tkinter.Button(self.selectrace, text="Human", command=lambda: self.button_set_race(p, "Human"))
        humanBtn.grid(sticky="we", columnspan=5)
        orcBtn = tkinter.Button(self.selectrace, text="Orc", command=lambda: self.button_set_race(p, "Orc"))
        orcBtn.grid(sticky="we", columnspan=5)
        elfBtn = tkinter.Button(self.selectrace, text="Elf", command=lambda: self.button_set_race(p, "Elf"))
        elfBtn.grid(sticky="we", columnspan=5)
        dwarfBtn = tkinter.Button(self.selectrace, text="Dwarf", command=lambda: self.button_set_race(p, "Dwarf"))
        dwarfBtn.grid(sticky="we", columnspan=5)

    def button_set_race(self, p, race):
        p.set_race(race)
        # Test output
        # print("Testing in button_set_race\n-----------------")
        # print(p.printinfo())
        # print("---------------\n")
        # print(p.Name)
        # p.FormatInfo()
        # print(p.printinfo())

        # Create Base class with new profile and destroy Login class
        # p.FormatInfo()
        # Base(None, p)
        # self.destroy()

# Main method runs when base.py is run
if __name__ == "__main__":
    app = Login(None)  # creates an instance of Base and initializes all widgets inside initialize
    app.title('Clones of Chaos - Base.py')
    app.geometry("+600+350")
    app.mainloop()