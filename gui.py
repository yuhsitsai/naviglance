import tkinter as tk
from tkinter import messagebox
from createRoute import *
from fondrenSetUp import *
from auth0.authentication import Database, GetToken
from PIL import ImageTk, Image

Domain = 'dev-8ohyjwmydl270q2y.us.auth0.com'
ClientID = 'Krg6tslxDWrKONghHokYlnokuDNFwrG4'
ClientSecret = 'vwZEL5GSwLVHHUVRC7997531zGXmt2uPUX6bIXDHPOhV1rGvGV8V3p4B56JJKUMU'

database = Database(Domain, ClientID)
token = GetToken(Domain, ClientID, ClientSecret)

class FondrenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fondren Library Route Finder")
        
        # Create UI Elements
        self.start_label = tk.Label(root, text="Start Room:")
        self.start_label.pack()
        
        self.start_entry = tk.Entry(root)
        self.start_entry.pack()
        
        self.end_label = tk.Label(root, text="End Room:")
        self.end_label.pack()
        
        self.end_entry = tk.Entry(root)
        self.end_entry.pack()
        
        self.find_path_button = tk.Button(root, text="Find Path", command=self.find_path)
        self.find_path_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        # Image does not work, sadly
        #self.img = ImageTk.PhotoImage(master=Image.open('path1.png'))
        #self.panel1 = tk.Label(root, image = img)
        #self.panel1.pack(side = "bottom", fill = "both", expand = "yes")
        #self.panel2 = tk.Label(root, image = img)
        #self.panel2.pack(side = "bottom", fill = "both", expand = "yes")

        # Initialize Fondren Library
        self.FondrenLibrary = buildingObj("Fondren", 7)
        self.FondrenLibrary = setFondrenMap(self.FondrenLibrary)


    def find_path(self):
        start_room_name = self.start_entry.get()
        end_room_name = self.end_entry.get()
        
        startRoom = self.FondrenLibrary.getRoomfromBuilding(start_room_name)
        endRoom = self.FondrenLibrary.getRoomfromBuilding(end_room_name)
        
        if startRoom and endRoom:
            self.result_label.config(text=f"Path found from {start_room_name} to {end_room_name}!")
            executeFindPath(self.FondrenLibrary, startRoom, endRoom)
            #img = ImageTk.PhotoImage(Image.open('path'+str(startRoom.getFloor())+'png'))
            #self.panel1.configure(image=img)
            #if (startRoom.getFloor() != endRoom.getFloor()):
                #img = ImageTk.PhotoImage(Image.open('path'+str(endRoom.getFloor())+'png'))
                #self.panel2.configure(image=img)
        else:
            messagebox.showerror("Error", "Invalid room names.")

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login to PathFinder")
        
        # Create UI Elements
        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack()
        
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()
        
        self.pw_label = tk.Label(root, text="Password:")
        self.pw_label.pack()
        
        self.pw_entry = tk.Entry(root)
        self.pw_entry.pack()
        
        self.login_button = tk.Button(root, text="Log In", command=self.login)
        self.login_button.pack()

        self.signup_button = tk.Button(root, text="Sign Up", command=self.signup)
        self.signup_button.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def signup(self):
        acc = self.email_entry.get()
        pw = self.pw_entry.get()
        try:
            database.signup(email=acc, password=pw, connection='Username-Password-Authentication')
            self.result_label.config(text=f"Signed up :) Please log in")
        except:
            self.result_label.config(text=f"Signed up failed :(")

    def login(self):
        acc = self.email_entry.get()
        pw = self.pw_entry.get()
        try:
            token.login(username=acc, password=pw, realm='Username-Password-Authentication')
        except:
            #print("Wrong Email / PassWord :(")
            self.result_label.config(text=f"Wrong Email / Password :(")
        else:
            #print("Logged in! :)")
            self.result_label.config(text=f"Logged in :)")
            root = tk.Tk()
            app = FondrenApp(root)
            root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()

