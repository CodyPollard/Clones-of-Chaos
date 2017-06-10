import settings, test_window, os
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
        # Variables for entry

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
            print('This path exists!')
        else:
            os.mkdir(u)


        # Create window
        twindow = tkinter.Toplevel(self)
        twindow.title(self.userfield.get())
        twindow.grid()
        twindow.geometry("+600+350")

# Main method runs when base.py is run
if __name__ == "__main__":
    app = Base(None)  # creates an instance of Base and initializes all widgets inside initialize
    app.title('Clones of Chaos')
    app.geometry("+600+350")
    app.mainloop()