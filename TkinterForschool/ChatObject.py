import sqlite3

db = sqlite3.connect("ChatRoomDatabase.db")
cursor = db.cursor()
class ChatFunctions():
    
    def __init__(self, UserId, ChatRoomId):
        self.UserId = UserId
        self.ChatRoomId = ChatRoomId
        
    def SendingMessage(self,Message):
        cursor.execute(f"INSERT INTO MessageTable VALUES({self.ChatRoomId},{self.UserId},\"{Message}\")")
        print(f"INSERT INTO MessageTable VALUES({self.ChatRoomId},{self.UserId},\"{Message}\")")
        db.commit()
    
    def GettingMessages(self):
        cursor.execute(f"SELECT Message, UserId FROM MessageTable WHERE ChatroomId = {self.ChatRoomId}")
        Messages = cursor.fetchall()
        return Messages
        for row in Messages:
            if row[1] == self.UserId:
                print(f"{row[0]} was sent by the user")
            else:
                print(f"{row[0]} was sent by another user")
    



        

