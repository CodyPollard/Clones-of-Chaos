import settings, os, player
import tkinter


# Main player screen. Used after Login is successful
class Base(tkinter.Tk):
    # Base class constructor
    def __init__(self, master, savepath):
        tkinter.Tk.__init__(self, master)
        self.savepath = savepath
        self.master = master
        self.main_window()

    # Accepts the PlayerInfo object from log_in after a user successfuly logs in
    def main_window(self):
        p = player.PlayerInfo(self.savepath)
        # Create window
        self.title("Clones of Chaos")
        self.grid()
        self.geometry("+600+350")
        # Create frame for widgets
        frame = tkinter.Frame(self)
        frame.grid()
        labelTop = tkinter.Label(frame, anchor="w", fg="black", text="CoC - "+p.playername)
        labelTop.grid(column=0, row=0, columnspan=4)
        # Left column
        labelRace = tkinter.Label(frame, fg="black", text="Race: ")
        labelRace.grid(column=0, row=1)
        labelArmy = tkinter.Label(frame, fg="black", text="Army Size: ")
        labelArmy.grid(column=0, row=2)
        labelAstr = tkinter.Label(frame, fg="black", text="Army Strength: ")
        labelAstr.grid(column=0, row=3)
        labelAdef = tkinter.Label(frame, fg="black", text="Army Defense: ")
        labelAdef.grid(column=0, row=4)
        labelSpyStr = tkinter.Label(frame, fg="black", text="Espionage Strength: ")
        labelSpyStr.grid(column=0, row=5)
        labelSpyDef = tkinter.Label(frame, fg="black", text="Espionage Defense: ")
        labelSpyDef.grid(column=0, row=6)
        # Right column
        dataRace = tkinter.Label(frame, text=p.race)
        dataRace.grid(column=1, row=1)
        dataArmy = tkinter.Label(frame, text=p.armyCount)
        dataArmy.grid(column=1, row=2)
        dataAstr = tkinter.Label(frame, text=p.soldierStr)
        dataAstr.grid(column=1, row=3)
        dataAdef = tkinter.Label(frame, text=p.guardStr)
        dataAdef.grid(column=1, row=4)
        dataSpyStr = tkinter.Label(frame, text=p.spyStr)
        dataSpyStr.grid(column=1, row=5)
        dataSpyDef = tkinter.Label(frame, text=p.sentryStr)
        dataSpyDef.grid(column=1, row=6)
        # menu_right column 2
        unitinfoBtn = tkinter.Button(frame, text="Unit Info", command=lambda: self.unit_info(frame, p))
        unitinfoBtn.grid(column=2, row=1, columnspan=2, sticky="we")
        unitinfoBtn = tkinter.Button(frame, text="Equipment Info")
        unitinfoBtn.grid(column=2, row=2, columnspan=2, sticky="we")
        castleinfoBtn = tkinter.Button(frame, text="Castle Info")
        castleinfoBtn.grid(column=2, row=3, columnspan=2, sticky="we")

    def unit_info(self, f, p):
        f.destroy()
        frame = tkinter.Frame(self)
        frame.grid()
        # Top
        labelTop = tkinter.Label(frame, fg="black", text="CoC - Unit Info")
        labelTop.grid(column=0, row=0, columnspan=4)
        unitsLbl = tkinter.Label(frame, fg="black", text="Units")
        unitsLbl.grid(column=0, row=1, padx=10)
        strengthLbl = tkinter.Label(frame, fg="black", text="Total Strength")
        strengthLbl.grid(column=1, row=1, padx=10)
        countLbl = tkinter.Label(frame, fg="black", text="Amount")
        countLbl.grid(column=2, row=1, padx=10)
        # Row 2
        soldierLbl = tkinter.Label(frame, fg="black", text="Soldier")
        soldierLbl.grid(column=0, row=2)
        soldierStrLbl = tkinter.Label(frame, fg="black", text=p.soldierStr)
        soldierStrLbl.grid(column=1, row=2)
        soldierCountLbl = tkinter.Label(frame, fg="black", text=p.soldierCount)
        soldierCountLbl.grid(column=2, row=2)
        # Row 3
        guardLbl = tkinter.Label(frame, fg="black", text="Guard")
        guardLbl.grid(column=0, row=3)
        guardStrLbl = tkinter.Label(frame, fg="black", text=p.guardStr)
        guardStrLbl.grid(column=1, row=3)
        guardCountLbl = tkinter.Label(frame, fg="black", text=p.guardCount)
        guardCountLbl.grid(column=2, row=3)
        # Row 4
        spyLbl = tkinter.Label(frame, fg="black", text="Spy")
        spyLbl.grid(column=0, row=4)
        spyStrLbl = tkinter.Label(frame, fg="black", text=p.spyStr)
        spyStrLbl.grid(column=1, row=4)
        spyCountLbl = tkinter.Label(frame, fg="black", text=p.spyCount)
        spyCountLbl.grid(column=2, row=4)
        # Row 5
        sentryLbl = tkinter.Label(frame, fg="black", text="Sentry")
        sentryLbl.grid(column=0, row=5)
        sentryStrLbl = tkinter.Label(frame, fg="black", text=p.sentryStr)
        sentryStrLbl.grid(column=1, row=5)
        sentryCountLbl = tkinter.Label(frame, fg="black", text=p.sentryCount)
        sentryCountLbl.grid(column=2, row=5)



# Login class handles creation and continuation of player profiles
class Login(tkinter.Tk):

    # Base class constructor.
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.pname = ""
        self.prace = ""
        self.log_in()

    # initialize used to create widgets an instance of Base is created
    def log_in(self):
        # Create the parent grid and configure the column/row weights
        self.grid()
        self.minsize(width=0, height=0)
        self.columnconfigure(0, weight=1)
        self.bind('<Return>', self.load_game)
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


    def load_game(self, event):
        # Variables
        self.pname = self.userfield.get().lower()
        savepath = settings.SAVEGAME_PATH + "/" + self.pname
        # Check if player's profile exists when logging in. If not, create it.
        if os.path.isdir(savepath):
            # Create window from Base and destroy Login
            Base(None, savepath)
            self.destroy()
        else:
            # Start the new game process
            self.new_game_prompt()

    # Display new game prompt if user profile doesn't exist
    def new_game_prompt(self):
        # Prompt user for profile creation
        self.newgamePrompt = tkinter.Toplevel(self)
        l = tkinter.Label(self.newgamePrompt, text="That profile does not exist, would you like to create it?")
        # Buttons
        yesBtn = tkinter.Button(self.newgamePrompt, text="Yes", command=lambda: self.create_profile())
        noBtn = tkinter.Button(self.newgamePrompt, text="No", command=self.newgamePrompt.destroy)
        # Create window and widgets
        self.newgamePrompt.grid()
        self.newgamePrompt.geometry("+600+350")
        l.grid()
        yesBtn.grid()
        noBtn.grid()

    def create_profile(self):
        c = player.CreatePlayer(self.pname)
        self.select_race(c)
        # Destroy the newgameprompt
        self.newgamePrompt.destroy()

    def select_race(self, c):
        # Create window
        self.selectrace = tkinter.Toplevel(self)
        self.selectrace.title()
        self.selectrace.grid()
        self.selectrace.geometry("+600+350")
        labelTop = tkinter.Label(self.selectrace, anchor="w", fg="black", text="Choose Your Race")
        labelTop.grid(column=0, row=0, columnspan=4)
        # Buttons
        humanBtn = tkinter.Button(self.selectrace, text="Human", command=lambda: self.button_set_race(c, "Human"))
        humanBtn.grid(sticky="we", columnspan=5)
        orcBtn = tkinter.Button(self.selectrace, text="Orc", command=lambda: self.button_set_race(c, "Orc"))
        orcBtn.grid(sticky="we", columnspan=5)
        elfBtn = tkinter.Button(self.selectrace, text="Elf", command=lambda: self.button_set_race(c, "Elf"))
        elfBtn.grid(sticky="we", columnspan=5)
        dwarfBtn = tkinter.Button(self.selectrace, text="Dwarf", command=lambda: self.button_set_race(c, "Dwarf"))
        dwarfBtn.grid(sticky="we", columnspan=5)

    def button_set_race(self, c, race):
        # Initialize game and player then start the game
        c.initialize_game(race)
        c.initialize_player()
        Base(None, c.savepath)
        self.destroy()

# Main method runs when base.py is run
if __name__ == "__main__":
    app = Login(None)  # creates an instance of Base and initializes all widgets inside initialize
    app.title('Clones of Chaos - Base.py')
    app.geometry("+600+350")
    app.mainloop()