from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
 
class Win1:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x300")
        self.master.title("GUI")
        self.show_widgets()
        self.master_icon = PhotoImage(file='images/msdos.ico')
        self.master.tk.call('wm', 'iconphoto', root._w, self.master_icon)
 
    def show_widgets(self):
        self.frame = tk.Frame(self.master)
        self.img1, self.button1 = self.create_button("View Rule List",
            lambda: self.new_window(Win2))
        self.img2, self.button2 = self.create_button("Add Rule",
            lambda: self.new_window(Win3))
        self.img3, self.quit_button3 = self.create_button(
                        "Quit",
                        lambda: self.close_window())
        self.frame.pack()
 
    def create_button(self, text, command):
        ''' Button that creates a new window
        pass the text and the command
        " '''
        img = tk.PhotoImage(file="images\msdos.ico")
        img = img.subsample(2, 2)
        butt = tk.Button(
            self.frame,
            border=0,
            relief="ridge",
            compound=tk.CENTER,
            text=text,
            fg="black",
            font="Arial 12",
            command=command)
        butt.pack()
        butt.configure(image=img)
        return img, butt
 
    def new_window(self, _class):
            global win2, win3
 
            try:
                if _class == Win2:
                    if win2.state() == "normal":
                        win2.focus()
            except:  
                win2 = tk.Toplevel(self.master)
                _class(win2)
 
            try:
                if _class == Win3:
                    if win3.state() == "normal":
                        win3.focus()
            except:  
                win3 = tk.Toplevel(self.master)
                _class(win3)
 
    def close_window(self):
        self.master.destroy()
 
class Win2(Win1):
 
    def __init__(self, master):
        super().__init__(master)
        self.master.title("View Rule List")
        self.master_icon = PhotoImage(file='images/msdos.ico')
        self.master.tk.call('wm', 'iconphoto', root._w, self.master_icon)
 
    def show_widgets(self):
        ''' A frame with a button to quit the window '''
        self.frame = tk.Frame(self.master)
        self.frame.pack()
 
        # Button 1
        self.img1, self.button2 = self.create_button(
                                "Add Rule",
                                lambda: self.new_window(Win3))
 
        # Button 2
        self.img2, self.quit_button = self.create_button(
                                "Quit",
                                lambda: self.close_window())
 
 
 
class Win3(Win2):
    
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Add Rule")
        self.master_icon = PhotoImage(file='images/msdos.ico')
        self.master.tk.call('wm', 'iconphoto', root._w, self.master_icon)
 
    def show_widgets(self):
        self.frame = tk.Frame(self.master)
        self.img1, self.quit_button = self.create_button(
                                    "Quit",
                                    command=self.close_window)
        self.label = tk.Label(
            # self.frame, text="THIS IS ONLY IN THE THIRD WINDOW"
            )
        self.label.pack()
        self.frame.pack()
 
 
 
root = tk.Tk()
app = Win1(root)
root.mainloop()