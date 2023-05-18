from ChatObject import ChatFunctions
from tkinter import *
from tkinter.simpledialog import askinteger
class ChatWindow():
    
    def __init__(self, UserId):
        self.UserId = UserId
        Id = askinteger("Chat Room Id","What chat room do you want to access?")
        self.ChatId = Id
        self.FunctionsObject = ChatFunctions(self.UserId,self.ChatId)
        self.ChatActualScreen = Tk()
        ChatWindow.AccesessingChatRoom(self)
        
    def AccesessingChatRoom(self):
        self.ChatActualScreen.geometry("1000x1000")
        Messages = self.FunctionsObject.GettingMessages()
        for Message in Messages:
            print(self.UserId)
            print(Message)
            if Message[1] == self.UserId:
                MessageLabelUser = Label(self.ChatActualScreen, text=f"{Message[0]}", fg="green").pack(pady=4)
            else:
                MessageLabelOtherUser = Label(self.ChatActualScreen,text=f"{Message[0]}", fg="blue").pack(pady=4)
        UserMessage = StringVar()
        Entry(self.ChatActualScreen, textvariable= UserMessage).pack()
        MessageButton = Button(self.ChatActualScreen, text= "Send", command= lambda: self.FunctionsObject.SendingMessage(UserMessage.get())).pack()
    