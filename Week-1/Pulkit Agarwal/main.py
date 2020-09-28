# importing modules.
import tkinter as tk
import tkinter.messagebox as tsmg
import dbfile


root = tk.Tk()              # instantiating Tk class.
root.title("FRLS")          # Specifying title for the window.
root.geometry("390x244")    # Specifying size of the window at opening.
root.minsize(390,240)       # Specifying minimum size of the window.

# Creating frames.
f1 = tk.Frame(root)         # Login frame.
f2 = tk.Frame(root)         # Register frame.
f3 = tk.Frame(root)         # Successful login frame.

# To switch between frames.
for frame in (f1, f2, f3):
    frame.grid(row=0, column=0, sticky='news')

# To raise required frame.
def raise_frame(frame):
    frame.tkraise()

# Registration block starts here.
def register():
    frstname = fname.get()                                                  
    lastname = lname.get()
    usrname = username.get()
    pwd = password.get()
    if frstname == '' or lastname == '' or usrname == '' or pwd == '':          # Checking if any field was left empty.
        tsmg.showinfo("Oops!","Sorry you need to fill all the fields.")
    elif len(pwd) < 8:
        tsmg.showinfo("Oops!", "Password must be of 8 characters.")
    else:
        details = [frstname,lastname,usrname,pwd]
        dbfile.registerUser(*details)                                           # Passing the credentials to the database file.
        tsmg.showinfo("Hurrah!", "You have been successfully registered.")      # Popup shown when user is successfully registered.

# Login block starts here.
def login():
    username = usernameVar.get()
    passwrd = passwordVar.get()

    if username == '' or password == '':
        tsmg.showinfo("Oops!,","Sorry you need to fill all the fields.")
    else:
        details = [username, passwrd]

        tk.Label(f3, text = f"{dbfile.loginUser(*details)}").grid(row = 1, column = 1, padx = 40, pady = 40)
        tk.Button(f3, text = "Logout", command = logout).grid(row = 2, column = 1)
        f3.grid(row = 0, column = 0)
        raise_frame(f3)

# Function to bring user back to frame 1.     
def logout():
    raise_frame(f1)


# Frame 1 starts here
tk.Label(f1, text = "Username").grid(row = 1, column = 0)           # Creating username label.
tk.Label(f1, text = "Password").grid(row = 2, column = 0)           # Creating password label.

# Defining variables to store username and password entered by user.
usernameVar = tk.StringVar()
passwordVar = tk.StringVar()

# Creating entry widgets to accept user inputs.
tk.Entry(f1, textvariable = usernameVar).grid(row = 1, column = 3)
tk.Entry(f1, textvariable = passwordVar, show = "*").grid(row = 2, column = 3)

tk.Button(f1, text = "Login", command = login).grid(row = 3, column = 3, pady = 10)

tk.Label(f1, text = "Not Registered?").grid(row = 4, column = 0)
tk.Button(f1, text = "Register Now", command=lambda:raise_frame(f2)).grid(row = 4, column = 3, pady = 10)

f1.grid(row = 0, column = 0, pady = 10, padx = 10)
# Frame 1 ends here.


# Frame 2 starts here. Frame 2 is the registration form.
# Creating labels and packing them in frame 2.
tk.Label(f2, text = "First Name").grid(row = 1, column = 0)     
tk.Label(f2, text = "Last Name").grid(row = 2, column = 0)
tk.Label(f2, text = "Username").grid(row = 3, column = 0)
tk.Label(f2, text = "Password").grid(row = 4, column = 0)

# Declaring variables and their types.
fname = tk.StringVar()
lname = tk.StringVar()
username = tk.StringVar()
password = tk.StringVar()

# Creating entry widgets for the user to give input and packing them in frame 2.
tk.Entry(f2, textvariable = fname).grid(row = 1, column = 3)
tk.Entry(f2, textvariable = lname).grid(row = 2, column = 3)
tk.Entry(f2, textvariable = username).grid(row = 3, column = 3)
tk.Entry(f2, textvariable = password, show = "*").grid(row = 4, column = 3)

# Submit button to register the user in database.
tk.Button(f2, text = "Register", command = register).grid(row = 5, column = 3, pady = 10)

# Asking user if they already have a registered account and leading them to the login frame.
tk.Label(f2, text = "Already Registered?").grid(row = 6, column = 0)
tk.Button(f2, text = "Login", command = lambda:raise_frame(f1)).grid(row = 6, column = 3)

f2.grid(row = 0, column = 0, pady = 10, padx = 10)      # Packing frame 2 in the window.
# Frame 2 ends here.

raise_frame(f1)  # frame 1 always stays up.

root.mainloop()
