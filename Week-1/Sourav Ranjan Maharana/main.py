from tkinter import * #Used to make the GUI
import db
import os

def login_screen():
    #Setting the window
    login_root = Toplevel(root)
    login_root.geometry("300x250")
    login_root.minsize(250,200)
    login_root.maxsize(300,250)
    login_root.title("Login Window")

    #Adding Username and Password button
    Label(login_root,text="Username:* ").place(x=30,y=20)
    Label(login_root,text="Password:* ").place(x=30,y=50)
    Entry(login_root,textvariable="username").place(x=100,y=23)
    Entry(login_root,textvariable="password",show="*").place(x=100,y=50)
    Button(login_root,text="Login").place(x=120,y=80)

# name="saurav"
# username="sauracv"
# password="saurav"
def registration_window(*args):
    global registration_root

    #Setting the window
    registration_root = Toplevel(root)
    registration_root.geometry("300x250")
    registration_root.minsize(400,200)
    # registration_root.maxsize(800,250)
    registration_root.title("Registration Window")

    global name
    global username
    global password

    global nameEntry
    global userEntry
    global passEntry

    name = StringVar()
    username = StringVar()
    password = StringVar()

    #Welcome Text
    Label(registration_root,text="Fill The Below Fields To Register",bg="black",fg="white",font=("Libre Baskerville",13,"bold")).pack(fill=X)

    #Adding Name,Username, Password and Register Button
    name=Label(registration_root,text="Name:* ").place(x=30,y=90)
    username=Label(registration_root,text="Username:* ").place(x=30,y=115)
    password=Label(registration_root,text="Password:* ").place(x=30,y=135)

    nameEntry = Entry(registration_root,textvariable=name).place(x=100,y=90)
    userEntry = Entry(registration_root,textvariable=username).place(x=100,y=115)
    passEntry = Entry(registration_root,textvariable=password,show="*").place(x=100,y=140)

    Button(registration_root,text="Register",command=validate_registration).place(x=120,y=200)

def validate_registration():
    print(nameEntry)
    if nameEntry is None or passEntry is None or nameEntry is None:
        print("Please enter the required details")
    else:
        name_info = nameEntry.get()
        username_info = userEntry.get()
        password_info = passEntry.get()
        print("Everything is correct")


def main_screen():
#Making the Fist Window/GUI
    global root #Making the varibale global so that it can be used anywhere in the program

    #Setting the Window
    root = Tk() #Creating the instance
    root.geometry("300x250") #Defining the size of the window
    root.minsize(250,200) #Setting the minimum size of the window
    root.maxsize(300,250) #Setting the maximum size of the window
    root.title("Login System") #Setting the title of the window

    #Welcome text on the top
    Label(root,text="Select Login/Register",bg="black",fg="white",font=("Libre Baskerville",18,"bold")).pack(fill=X)

    #Making Login and Register Button
    Button(root,text="Login",padx=15,pady=4,bg="#FF5732",command=login_screen).place(x=110,y=60)
    Button(root,text="Register",padx=10,pady=4,bg="#00BDA5",command=registration_window).place(x=110,y=100)

    #To show the GUI to the user
    root.mainloop()

main_screen()