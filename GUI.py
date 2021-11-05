from tkinter import *


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title('Tournament Fixtures')
        self.minsize(500, 400)


# Root function call
root = Root()

root.mainloop()
