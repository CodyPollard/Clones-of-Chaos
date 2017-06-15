import settings, os, player
import tkinter


class Base(tkinter.Tk):
    counter = 0
    # Base class constructor
    def __init__(self, master, PlayerInfo):
        tkinter.Tk.__init__(self, master)
        self.master = master
        self.p = PlayerInfo
        self.main_window()

    # Accepts the PlayerInfo object from log_in after a user successfuly logs in
    def main_window(self):
        # Create window
        #self.title("whats this")
        #mainscreen = tkinter.Toplevel(self)
        self.title(self.p.Name)
        self.grid()
        self.geometry("+600+350")
        labelTop = tkinter.Label(self, anchor="w", fg="black", text="Your Stats")
        labelTop.grid(column=0, row=0, columnspan=4)
        # Column 0 labels
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

        # Column 1 labels
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

class Login(tkinter.Tk):
    counter = 0

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
        u = u
        # Prompt
        newgamePrompt = tkinter.Toplevel(self)
        l = tkinter.Label(newgamePrompt, text="That profile does not exist, would you like to create it?")
        yesBtn = tkinter.Button(newgamePrompt, text="Yes", command= lambda: self.create_profile(u))
        noBtn = tkinter.Button(newgamePrompt, text="No", command=newgamePrompt.destroy)
        newgamePrompt.grid()
        newgamePrompt.geometry("+600+350")
        l.grid()
        yesBtn.grid()
        noBtn.grid()

    def create_profile(self, u):
        u = u
        os.mkdir(u)
        p = player.PlayerInfo(u)
        self.select_race(p)
        # Destroy the newgamePrompt window here


    def select_race(self, p):
        # Create window
        selectrace = tkinter.Toplevel(self)
        selectrace.title()
        selectrace.grid()
        selectrace.geometry("+600+350")
        labelTop = tkinter.Label(selectrace, anchor="w", fg="black", text="Choose Your Race")
        labelTop.grid(column=0, row=0, columnspan=4)
        # Labels
        humanBtn = tkinter.Button(selectrace, text="Human", command=p.set_race("Human"))
        humanBtn.grid(sticky="we", columnspan=5)
        orcBtn = tkinter.Button(selectrace, text="Orc", command=p.set_race("Orc"))
        orcBtn.grid(sticky="we", columnspan=5)
        elfBtn = tkinter.Button(selectrace, text="Elf", command=p.set_race("Elf"))
        elfBtn.grid(sticky="we", columnspan=5)
        dwarfBtn = tkinter.Button(selectrace, text="Dwarf", command=p.set_race("Dwarf"))
        dwarfBtn.grid(sticky="we", columnspan=5)


# Main method runs when base.py is run
if __name__ == "__main__":
    app = Login(None)  # creates an instance of Base and initializes all widgets inside initialize
    app.title('Clones of Chaos - Base.py')
    app.geometry("+600+350")
    app.mainloop()