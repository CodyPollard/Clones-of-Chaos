import tkinter

class Base(tkinter.Tk):
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
        userfield = tkinter.Entry(self)
        userfield.grid(column=1, row=1, sticky="w")
        login = tkinter.Button(self, text="Log in", anchor="s")
        login.grid(column=0, row=2, columnspan=2, sticky="we")

# Main method runs when base.py is run
if __name__ == "__main__":
    app = Base(None)  # creates an instance of Base and initializes all widgets inside initialize
    app.title('Clones of Chaos')
    app.mainloop()