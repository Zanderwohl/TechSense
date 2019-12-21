from tkinter import *
#import SystemC

class Window(Frame):
    
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self.master = master
        self.controller = controller

        self.pack(fill=BOTH, expand=1)

        exitButton = Button(self, text="Exit", command=self.v_exit)
        exitButton.place(x = 0, y = 0)

        self.addMenuBar()
        self.addFileDrop()
        self.addEditDrop()
        self.addCalcDrop()

    def addMenuBar(self):
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

    def addFileDrop(self):
        fileMenu = Menu(self.menu)
        fileMenu.add_command(label="New")
        fileMenu.add_command(label="Open")
        fileMenu.add_command(label="Save")
        fileMenu.add_command(label="Save as...")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.v_exit);
        self.menu.add_cascade(label="File", menu=fileMenu)

    def addEditDrop(self):
        editMenu = Menu(self.menu)
        editMenu.add_command(label="Duplicate")
        editMenu.add_command(label="Time")
        self.menu.add_cascade(label="Edit", menu=editMenu)

    def addCalcDrop(self):
        calcMenu = Menu(self.menu)
        calcMenu.add_command(label="Torch Burn")
        calcMenu.add_command(label="Hohmann Transfer")
        calcMenu.add_separator()
        calcMenu.add_command(label="Radio Time")
        self.menu.add_cascade(label="Calculate", menu=calcMenu)

    def v_exit(self):
        self.controller.exit(1)
        #User exit (0).
        #SystemC.exit(0)

def showWindow(controller):
    root = Tk()
    app = Window(root, controller)

    root.wm_title("Solar System")
    root.geometry("320x200");

    root.mainloop() #show window

    return root
