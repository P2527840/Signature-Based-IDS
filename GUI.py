from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Return to Main Menu")
    myLabel.pack()


myLabel = Label(root, text="")
myLabel.pack()


myButton = Button(root, text="Main Menu", padx=50, pady=50, command=myClick, bg="#0267C1")
myButton.pack()



root.mainloop()

