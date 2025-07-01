import logging


loggerr=logging.getLogger(__name__)
loggerr.setLevel(logging.INFO)
handler=logging.FileHandler("Entries.log")
formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
loggerr.addHandler(handler)

class Book:
    def __init__(self,titlee,author,id,total_books,avialable_books):
        self.titlee=titlee
        self.author=author
        self.id=id
        self.total_books=total_books
        self.avialable_books=avialable_books
        self.statuss=None
        self.status()
        loggerr.info(f"BOOK OBJECT CREATED (TITLE : {self.titlee}, AUTHOR : {self.author}, ID: {self.id} , TOTAL BOOKS : {self.total_books} , AVIALABLE BOOKS : {self.avialable_books} )")
    def __repr__(self):
        return f"{self.titlee} by {self.author} ID: {self.id} Status: {self.statuss}"
    def status(self):
        stad=None
        if self.avialable_books>0:
            stad = "Available"
        elif self.avialable_books==0:
            stad = "BOOK OUT OF STOCK"
            loggerr.warning(f"THE BOOK (TITLE : {self.titlee} , AUTHOR : {self.author} , ID : {self.id}) HAS RUN OUT OF STOCK")
        self.statuss=stad
        return stad
11
    
class Members:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.borrowed=[]
        loggerr.info(f"MEMBER OBJECT CREATED (NAME : {self.name} , ID : {self.id})")
    def __repr__(self):
        return f"MEMBER: {self.name}, ID: {self.id}"
    def display_borrowed(self):
        for i in self.borrowed:
            print(i)