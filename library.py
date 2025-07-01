import logging
from decorators import secure
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler=logging.FileHandler("Library.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)



class Library:
    def __init__(self):
        self.books=[]
        self.bookids=[]
        self.members=[]
        self.memberids=[]


    def add_member(self,member):
        self.members.append(member)
        self.memberids.append(member.id)
        print(f"member added :{member}")
        logger.info(f"MEMBER ({member}) ADDED ")
    def remove_member(self,memberid):
        for i in self.members:
            if i.id == memberid:
                self.members.remove(i)


    def add_book(self,book):
        self.books.append(book)
        self.bookids.append(book.id)
        print(f"book added {book}")
        logger.info(f"BOOK ({book}) ADDED ")


    def borrow_book(self,memberid,bookid):
     
        f_member= None
        f_book=None
        for i in self.members:
            if memberid==i.id:
                f_member=i
        for i in self.books:
            if bookid==i.id:
                f_book=i
        if f_book.avialable_books > 0:
         if f_member != None and f_book != None :
            f_member.borrowed.append(f_book)
            f_book.avialable_books-=1
            logger.info(f"BOOK : {f_book} ,BORROWED BY : {f_member}")
            print("book borrowed")
         elif f_member == None:
            print("INVALID MEMBER ID")
            logger.error(f"INVALID MEMBER ID: {memberid}")

         elif f_book == None:
            print("INVALID BOOK ID")
            logger.error(f"INVALID BOOK ID : {bookid}")
        else:
            print("BOOK IS NOT AVIALABLE")
            logger.error(f"{f_book.titlee} WAS NOT AVAILABLE DUE TO OUT OF STOCK")        

    def return_book(self,memberid,bookid):
        f_member=None
        f_book=None
        for i in self.members:
            if memberid==i.id:
                f_member=i
                for j in i.borrowed:
                    if j.id==bookid:
                        f_book=j
        f_member.borrowed.remove(f_book)
        f_book.avialable_books+=1
        logger.info(f"BOOK : {bookid} RETURNED BY : {memberid}")
        print("BOOK RETURNED")
    def display_members(self):
        for i in self.members:
            print(i)
        logger.info("DISPLAYED MEMBERS")
    def search_book(self,book_name):
        for i in self.books:
            if book_name == i.titlee:
                print(i , f"STATUS : {i.statuss}")
        logger.info(f"SEARCHED IN BOOKS: {book_name}")
    @secure
    def print_member(self):
        j=input("WARNING YOU WILL PRINT ALL THE MEMEBERS WITH THIS PRESS ENTER TO CONTinue")
        for i in self.members:
            print(f"name : {i.name} , id : {i.id}")