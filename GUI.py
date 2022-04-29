from tkinter import *
from PIL import ImageTk,Image

root = Tk() 
root.minsize(500, 500)
root.title("SIDS GUI")
img = PhotoImage(file='images/msdos.ico')
root.tk.call('wm', 'iconphoto', root._w, img)


def open():
    top = Toplevel()
    top.minsize(800, 800)
    top.title("View Rule List")
    img = PhotoImage(file='images/msdos.ico')
    top.tk.call('wm', 'iconphoto', top._w, img)
    menu = Button(top, text="Main Menu", padx=20, pady=20, bg="#0267C1", command=top.destroy).pack()
    addrule = Button(top, text="Add Rule", padx=20, pady=20, bg="#88AB75").pack()



rulelist = Button(root, text="Open Second Window").pack


# sub = Sublevel()
# sub.minsize(300, 300)
# sub.title("Add Rule")
# menu = Button(sub, text="Main Menu", padx=20, pady=20, bg="#0267C1", command=sub.destroy).pack()


# def myClick():
    # myLabel = Label(root)
    # myLabel.pack()


myLabel = Label(root, text="")
myLabel.pack()


myButton = Button(root, text="Main Menu", padx=20, pady=20, bg="#0267C1")
myButton.pack()

myButton = Button(root, text="View Rule List", padx=20, pady=20, bg="#88AB75", command=open)
myButton.pack()

myButton = Button(root, text="Synchronise Rules", padx=4, pady=4, bg="#88AB75")
myButton.pack()


root.mainloop()

