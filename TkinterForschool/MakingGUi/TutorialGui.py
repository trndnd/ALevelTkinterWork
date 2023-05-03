from tkinter import *
from tkinter import messagebox
import time
import sqlite3
MainScreen = Tk()
MainScreen.geometry("300x250")
db = sqlite3.connect("CustomerLogIn.db")
cursor = db.cursor()
def MainPage():
    TitleLabel = Label(MainScreen, text="Main Page").pack(pady = 10)
    RegisterButton = Button(MainScreen, text="Register", command= RegisterPage).pack(pady = 10)
    LoginButton = Button(MainScreen,text="Log in", command= LoginPage).pack(pady = 10)
    

def LoginPage():
    global MainScreen
    UsernameInputted = StringVar()
    PasswordInputted = StringVar()
    LoginScreen = Toplevel(MainScreen) # Makes this teh top level screen which essentially makes it the new screen from teh main screen
    LoginScreen.title("Login Window")
    BigGap = Label(LoginScreen, text ="   ").pack(pady = 100)
    UsernameLabel = Label(LoginScreen, text="Username").pack(pady = 10)
    Entry(LoginScreen,textvariable = UsernameInputted).pack(pady = 10)
    PasswordLabel = Label(LoginScreen, text = "Password").pack()
    Entry(LoginScreen,textvariable = PasswordInputted, show = "*").pack(pady = 10)
    LoginButton = Button(LoginScreen, text ="Log in",command=lambda: GettingPasswordFromDatabaseAndChecking(UsernameInputted.get(),PasswordInputted.get(),LoginScreen)).pack()
    
def RegisterPage():
    global MainScreen
    UsernameInputted = StringVar()
    PasswordInputted = StringVar()
    RegisterScreen = Toplevel(MainScreen) # Makes this teh top level screen whihc essentially makes it the new screen from teh main screen
    RegisterScreen.title("Register Window")
    BigGap = Label(RegisterScreen, text ="   ").pack(pady = 100)
    UsernameLabel = Label(RegisterScreen, text="Username").pack(pady = 10)
    Entry(RegisterScreen, textvariable= UsernameInputted).pack(pady = 10)
    PasswordLabel = Label(RegisterScreen, text = "Password").pack()
    Entry(RegisterScreen,textvariable= PasswordInputted, show="*").pack(pady = 10)
    RegisterButton = Button(RegisterScreen, text = "register", command=lambda: CheckingDataIsValid(UsernameInputted.get(),PasswordInputted.get())).pack(pady = 10)
    

def AddingToDatabase(UsernameInputted,Passwordinputted):
    cursor.execute(f"INSERT INTO Customers Values(\"{UsernameInputted}\",\"{Passwordinputted}\")") # Need apostrpahes as it makes them strings for the db
    db.commit()

def GettingPasswordFromDatabaseAndChecking(UsernameInputted,PasswordInputted,LoginScreen):
    print(UsernameInputted)
    cursor.execute(f"SELECT Password FROM Customers WHERE Username = \"{UsernameInputted}\"")
    print("SELECT Password FROM Customers WHERE Username = \"{UsernameInputted}\"")
    PasswordOfAccount = [row[0] for row in cursor.fetchall()]
    print(PasswordOfAccount)
    if PasswordInputted == PasswordOfAccount[0]:
        messagebox.showinfo("showinfo","Successfully logged in")
        #There should be a function here to take you to the next page but teher is no page so it just shows that you have logged in!
    elif PasswordOfAccount == None:
        messagebox.showinfo("showinfo","Username does not exist. Go register!")
        RegisterPage()
    else:
        messagebox.showinfo("showinfo","Incorrect password or username")
    LoginScreen.destroy()
        
def CheckingDataIsValid(UsernameInputted,PasswordInputted):
    global RegisterScreen
    cursor.execute("SELECT Username FROM Customers")
    AllUsernames = [row[0] for row in cursor.fetchall()] # got rid of the comments as the problem with comparing the two was that the username form teh database had an extra comment at the end
    print(UsernameInputted)
    print(AllUsernames)
    if UsernameInputted in AllUsernames:
        messagebox.showinfo("showinfo","Username already exists")
    elif len(PasswordInputted) < 10:
        messagebox.showinfo("showinfo", "Password should be over 10 characters")
    else:
        AddingToDatabase(UsernameInputted,PasswordInputted)
        messagebox.showinfo("showinfo",f"You have successfully registered with the username {UsernameInputted}")
        TestLabel = Label(RegisterScreen, text="You have successfully registerd").pack()
        time.sleep(3)
    RegisterScreen.destroy()
        
MainPage()
MainScreen.mainloop()
