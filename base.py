import settings, os, player
import tkinter


class Base(tkinter.Tk):
    counter = 0
    # Base class constructor.
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    # initialize used to create widgets an instance of Base is created
    def initialize(self):
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
        login = tkinter.Button(self, text="Log in", anchor="s", command=self.log_in)
        login.grid(column=0, row=2, columnspan=2, sticky="we")

        # Testing window button
        # self.testB = tkinter.Button(self, text="Test Button", command=test_window.Base(None))
        # self.testB.grid(column=0, row=3)

    def log_in(self):
        # Local Variables
        u = settings.SAVEGAME_PATH + "/" + self.userfield.get().lower()
        # Check if player's profile exists when logging in. If not, create it.
        if os.path.isdir(u):
            # print("This should run main_window")
            p = player.PlayerInfo(u)
            p.FormatInfo()
            self.main_window(p)
        else:
            os.mkdir(u)

    # Accepts the PlayerInfo object from log_in after a user successfuly logs in
    def main_window(self, profile):
        p = profile
        # Create window
        mainscreen = tkinter.Toplevel(self)
        mainscreen.title(p.Name)
        mainscreen.grid()
        mainscreen.geometry("+600+350")
        labelTop = tkinter.Label(mainscreen, anchor="w", fg="black", text="Your Stats")
        labelTop.grid(column=0, row=0, columnspan=4)
        # Column 0 labels
        labelRace = tkinter.Label(mainscreen, anchor="w", fg="black", text="Race: ")
        labelRace.grid(column=0, row=1)
        labelArmy = tkinter.Label(mainscreen, anchor="w", fg="black", text="Army Size: ")
        labelArmy.grid(column=0, row=2)
        labelAstr = tkinter.Label(mainscreen, anchor="w", fg="black", text="Army Strength: ")
        labelAstr.grid(column=0, row=3)
        labelAdef = tkinter.Label(mainscreen, anchor="w", fg="black", text="Army Defense: ")
        labelAdef.grid(column=0, row=4)
        labelSpyStr = tkinter.Label(mainscreen, anchor="w", fg="black", text="Spy Strength: ")
        labelSpyStr.grid(column=0, row=5)
        labelSpyDef = tkinter.Label(mainscreen, anchor="w", fg="black", text="Spy Defense: ")
        labelSpyDef.grid(column=0, row=6)

        # Column 1 labels
        dataRace = tkinter.Label(mainscreen, anchor="e", text=p.Race)
        dataRace.grid(column=1, row=1)
        dataArmy = tkinter.Label(mainscreen, anchor="e", text=p.ArmySize)
        dataArmy.grid(column=1, row=2)
        dataAstr = tkinter.Label(mainscreen, anchor="e", text=p.ArmyStr)
        dataAstr.grid(column=1, row=3)
        dataAdef = tkinter.Label(mainscreen, anchor="e", text=p.ArmyDef)
        dataAdef.grid(column=1, row=4)
        dataSpyStr = tkinter.Label(mainscreen, anchor="e", text=p.SpyStr)
        dataSpyStr.grid(column=1, row=5)
        dataSpyDef = tkinter.Label(mainscreen, anchor="e", text=p.SpyDef)
        dataSpyDef.grid(column=1, row=6)

# Main method runs when base.py is run
if __name__ == "__main__":
    app = Base(None)  # creates an instance of Base and initializes all widgets inside initialize
    app.title('Clones of Chaos')
    app.geometry("+600+350")
    app.mainloop()