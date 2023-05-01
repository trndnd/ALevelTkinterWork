from tkinter import *
from tkinter import messagebox
import sqlite3
MainScreen = Tk()
MainScreen.geometry("300x2")
db = sqlite3.connect("CustomerLogIn.db")
cursor = db.cursor()
def MainPage():
    TitleLabel = Label(MainScreen, text="Main Page").pack()
    RegisterButton = Button(MainScreen, text="Register", command= RegisterPage).pack()
    LoginButton = Button(MainScreen,text="Log in", command= LoginPage).pack()
    

def LoginPage():
    global MainScreen
    UsernameInputted = StringVar()
    PasswordInputted = StringVar()
    LoginScreen = Toplevel(MainScreen) # Makes this teh top level screen whihc essentially makes it the new screen from teh main screen
    UsernameLabel = Label(LoginScreen, text="Username").pack()
    Entry()
    
def RegisterPage():
    global MainScreen
    UsernameInputted = StringVar()
    PasswordInputted = StringVar()
    RegisterScreen = Toplevel(MainScreen) # Makes this teh top level screen whihc essentially makes it the new screen from teh main screen
    UsernameLabel = Label(RegisterScreen, text="Username").pack()
    Entry(RegisterScreen, textvariable= UsernameInputted).pack()
    Entry(RegisterScreen,textvariable= PasswordInputted, show="*").pack()
    RegisterButton = Button(RegisterScreen, text = "register", command=lambda: CheckingDataIsValid(UsernameInputted.get(),PasswordInputted.get())).pack()

def AddingToDatabase(UsernameInputted,Passwordinputted):
    cursor.execute(f"INSERT INTO Customers Values(\"{UsernameInputted}\",\"{Passwordinputted}\")") # Need apostrpahes as it makes them strings for the db
    db.commit()
    
def CheckingDataIsValid(UsernameInputted,PasswordInputted):
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
        
a = "aad"
mylist = [("aaron"),("aad")]
print(a in mylist)
MainPage()
MainScreen.mainloop()