from ChatObject import ChatFunctions
from tkinter import *
from tkinter import messagebox
from ChattingPage import ChatWindow
import time
import sqlite3
MainScreen = Tk()
MainScreen.geometry("300x250")
db = sqlite3.connect("ChatRoomDatabase.db")
cursor = db.cursor()
MainScreen.configure(bg="#1B1D21")
def MainPage():
    BigGap = Label(MainScreen, text ="", bg="#1B1D21").pack(pady = 30)
    TitleLabel = Label(MainScreen, text="Main Page", bg="#5A5A5A", font=("Comfortaa",40)).pack(pady = 50)
    RegisterButton = Button(MainScreen,highlightbackground="white", text="Register",bg='#1B1D21', width = 25, height = 10, command= RegisterPage).pack(pady = 10)
    LoginButton = Button(MainScreen,highlightbackground="white",bg='#1B1D21',text="Log in", width = 25, height = 10, command= LoginPage).pack(pady = 10)
    

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
    LoginButton = Button(LoginScreen, text ="Log in", height= 3, width = 15,command=lambda: GettingPasswordFromDatabaseAndChecking(UsernameInputted.get(),PasswordInputted.get(),LoginScreen)).pack()
    
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
    cursor.execute(f"INSERT INTO Accounts Values(NULL,\"{UsernameInputted}\",\"{Passwordinputted}\")") #Need the NULL for teh autoincmrent to work 
    db.commit()
#if UsernameInputted.get() == "" or PasswordInputted.get() == "":
        #messagebox.showinfo("showinfo","Put data in!!")
        #LoginPage()
        #LoginScreen.destroy()
        #This is code for telling the user to add data if they haven't inputted anything
def GettingPasswordFromDatabaseAndChecking(UsernameInputted,PasswordInputted,LoginScreen):
    cursor.execute(f"SELECT Password FROM Accounts WHERE Username = \"{UsernameInputted}\"")
    print("SELECT Password FROM Accounts WHERE Username = \"{UsernameInputted}\"")
    PasswordOfAccount = [row[0] for row in cursor.fetchall()]
    print(PasswordOfAccount)
    if PasswordInputted in PasswordOfAccount:
        messagebox.showinfo("showinfo","Successfully logged in")
        ChatWindow(Gettingid(UsernameInputted))
        #There should be a function here to take you to the next page but teher is no page so it just shows that you have logged in!
    elif PasswordOfAccount == []:
        messagebox.showinfo("showinfo","Username does not exist. Go register!")
        RegisterPage()
    else:
        messagebox.showinfo("showinfo","Incorrect password")
    
        
def CheckingDataIsValid(UsernameInputted,PasswordInputted):
    global RegisterScreen
    cursor.execute("SELECT Username FROM Accounts")
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
        TestLabel = Label(RegisterScreen, text="You have successfully registered").pack()
        time.sleep(3)
    RegisterScreen.destroy()
    
def Gettingid(Username):
        cursor.execute(f"SELECT UserId FROM Accounts WHERE Username = \"{Username}\"")
        UserId = cursor.fetchone()
        return UserId[0]
MainPage()
MainScreen.mainloop()