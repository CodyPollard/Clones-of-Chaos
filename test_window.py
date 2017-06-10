import tkinter

class Base(tkinter.Tk):
    # Base class constructor.
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.TESTINIT()

    # initialize used to create widgets an instance of Base is created
    def TESTINIT(self):
        # Create window
        twindow = tkinter.Toplevel(self)
        twindow.title("Memes")
        twindow.grid()
        twindow.geometry("+600+350")


# Main method runs when test_window.py is run
