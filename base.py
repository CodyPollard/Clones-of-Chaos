import tkinter

class Base(tkinter.Tk):
    # Base class constructor.
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    # initialize used to create widgets an instance of Base is created
    def initialize(self):
        # Sets the minimum size of the frame and uses grid for layout management inside the frame
        self.minsize(width=500, height=500)
        self.grid()
        # Create widgets below
        label = tkinter.Label(self, pady=10, anchor="w", fg="black", text="Clones of Chaos")
        label.grid(column=0, row=1, columnspan=2, sticky="EW")

# Main method runs when base.py is run
if __name__ == "__main__":
    app = Base(None)  # creates an instance of Base and initializes all widgets inside initialize
    app.title('Clones of Chaos')
    app.mainloop()