from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk,Image

# rule_var=tk.StringVar()

class Win1:
    def __init__(self, master):
        self.master = master
        self.master.geometry("760x600")
        self.master.title("Signature-Based IDS")
        self.show_widgets()
        self.master_icon = PhotoImage(file='images/msdos.ico')
        self.master.tk.call('wm', 'iconphoto', root._w, self.master_icon)

 
    def show_widgets(self):
        self.frame = tk.Frame(self.master)
        self.label1 = tk.Label(
            self.frame, text="What is Snort? \n Snort is the foremost Open Source Intrusion Prevention System (IPS) in the world. \n Snort IPS uses a series of rules that help define malicious network activity and uses \n those rules to  find packets that match against them and generates alerts for users. \n Snort can be deployed inline to stop these packets, as well."
            )
        self.label2 = tk.Label(
            self.frame, text="\n Snort has three primary uses: As a packet sniffer like tcpdump, as a packet logger — which is useful for network traffic debugging, \n or it can be used as a full-blown network intrusion prevention system. \n Snort can be downloaded and configured for personal and business use alike."
            )
        self.label3 = tk.Label(
            self.frame, text="All rules added here will be listed in the database"
            )
        self.img1, self.button1 = self.create_button("",
            lambda: self.new_window(Win2),
            "images/View Rule List.ico")
        self.img2, self.button2 = self.create_button("",
            lambda: self.new_window(Win3),
            "images/Add Rule.ico")
        self.img3, self.quit_button3 = self.create_button("",
                        lambda: self.close_window(),
                        "images/Quit.ico")
        self.label1.pack(side=TOP, padx=2, pady=5)  
        self.label2.pack(side=TOP, padx=2, pady=5)   
        self.label3.pack(side=TOP, padx=2, pady=5)           
        self.frame.pack()
 
    def create_button(self, text, command, icon_path):
        ''' Button that creates a new window
        pass the text and the command
        " '''
        img = tk.PhotoImage(file=icon_path)
        img = img.subsample(2, 2)
        butt = tk.Button(
            self.frame,
            border=0,
            relief="ridge",
            compound=tk.LEFT,
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
                                "",
                                lambda: self.new_window(Win3),
                                "images/Add Rule.ico")
 
        # Button 2
        self.img2, self.quit_button = self.create_button(
                                "",
                                lambda: self.close_window(),
                                "images/Quit.ico")

    # def 
                                
 
 
 
class Win3(Win2):
    
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Add Rule")
        self.master_icon = PhotoImage(file='images/msdos.ico')
        self.master.tk.call('wm', 'iconphoto', root._w, self.master_icon)

    
    def show_widgets(self):
        self.frame = tk.Frame(self.master)
        self.entry1 = tk.Text(self.master, height=1, width=50, bg='white') 
        
        self.label4 = tk.Label(
            self.frame, text="Syntax of writing Snort rule: \n alert ip any any -> any any (msg: 'IP Packet Detected';)"
            )
        
        self.label5 = tk.Label(
            self.frame, text="Example of Snort rule: \n log tcp !192.168.0/24 any -> 192.168.0.33 (msg: 'mounted access' ;)"
            )
        # Button for adding rule from user
        self.img, self.button2 = self.create_button(
                                "", 
                                lambda: self.handle_add_rule_click(), 
                                "images/add.ico", )
        # self.button2.place(x=100, y=75)
        
        self.img1, self.quit_button = self.create_button(
                                    "",
                                    lambda: self.close_window(),
                                    "images/Quit.ico")
        # self.quit_button.place(x=100, y=50)
        
        # creating a label for
        # name using widget Label
        # self.label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
  
        # creating a entry for input
        # name using widget Entry
        # self.entry1 = tk.Entry(self.master,textvariable = rule_var, font=('calibre',10,'normal'))
        
        # add one text box
        # t1 = self.Text(root._w,  height=1, width=50,bg='white') 
        # t1.grid(row=3,column=2)

        # l0 = tk.Label(root._w,  text='',
        # font=('Helvetica', 16), width=30,anchor="c" )
        # # l0.grid(row=1,column=1,columnspan=4)

        # l1 = tk.Label(root._w,  text='Rule: ', width=10,anchor="c" )  
        # l1.grid(row=3,column=1)
        
        # my_str = tk.StringVar()
        # l5 = tk.Label(root,  textvariable=my_str, width=10 )  
        # l5.grid(row=3,column=3) 
        # my_str.set("Output")
        # def add_data():
        #     flag_validation=True # set the flag 
        #     my_name=t1.get("1.0",END) # read name
        #     if(len(my_name) < 50 ):
        #         # or len(my_class)<2  or len(my_gender) < 2 
        #         flag_validation=False 

        self.label4.pack(side=TOP, padx=15, pady=20)
        self.label5.pack(side=TOP, padx=15, pady=20)
        self.entry1.pack(side=TOP, padx=15, pady=20)

        self.frame.pack(side=TOP, padx=15, pady=20)
        

    # def submit(self):
    #     rule=rule_var.get(self)
    #     print("Custom Rule: "+ rule)
    #     rule_var.set("")

    def handle_add_rule_click(self):
        """
        This function handles the code when the user clicks the button
        """
        # get the value
        new_rule =self.entry1.get('1.0', 'end-1c')
        success = insert_new_rule_to_db(new_rule)
        if success == 0:
            print('Success')
        #insert rule
        elif success == 1:
            print('Failure')
            self.entry1.delete(0, self.END)
          

    
def insert_new_rule_to_db(rule: str):
    """
    Inserts users added rule to the database
    rule syntax: alert any any -> any any (msg: "IP Packet detected";)
    return: 0 on success, 1 on failure
    """
    import mysql.connector

    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Mydatabase123!",
            database="user_ruleset"
        )

        mycursor = mydb.cursor()

        sql_query = """INSERT INTO rules (RuleName) VALUES (%s)"""
        mycursor.execute(sql_query, (rule,))
    
        mydb.commit()
        return 0

    except mysql.connector.Error as error:
        print("Failed to insert rule to database {}".format(error))
        return 1
    # print(mycursor.rowcount, "Rule added to Database")
    # mycursor.close()

    def get_rules_from_db(rule: str):
        """

        """
        # Connect to database
        #Query "SELECT * FROM rules"
        #Return rules    

    def write_rules_to_rule_file(self, rules):
        file = open("rules", "a")
        for rules in rules:
            file.write(rule)
        file.close()


        
 
 
 
root = tk.Tk()
app = Win1(root)
root.mainloop()