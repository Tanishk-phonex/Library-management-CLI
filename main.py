from core import Book,Members
from library import Library
import random
lib=Library()
def id_genrator(item):
    if item=="book":
        while True:
            id=random.randint(1,100)
            book_id="B"+f"{id}"
        
            if book_id not in lib.bookids:
                return book_id
    if item=="member":
        while True:
            id=random.randint(1,100)
            memberid="M"+f"{id}"
            if memberid not in lib.memberids:
                return memberid


while True:
   try: 
    print("--LIBRARY MENU--\n1. ADD BOOK\n2. ADD MEMBER\n3. BORROW BOOK\n4. RETURN BOOK \n5.DISPLAY MEMBERS \n6.SEARCH BOOK \n7.print all members ")
    a=int(input("enter choice"))

    if a==1:
        con=input("enter to add")
        n=input("Book Title: ")
        m=input("Book Author")
        id=id_genrator("book")
        no=int(input("enter total books"))
        noa=int(input("enter avilable books"))
        if id not in lib.bookids: 
            book=Book(n,m,id,no,noa)
            lib.add_book(book)
        else:
            print("member id already exists")
    elif a==2:
        cob=input("press enter to add")
        g=input("Member name: ")
        h=id_genrator("member")
        mem=Members(g,h)
        lib.add_member(mem)
    elif a==3:
        l=input("enter to continue")
        memberid=input("enter id of Member borrowing: ")
        bookid=input("Enter book id: ")
        lib.borrow_book(memberid,bookid)
        for i in lib.books:
            if i.id== bookid:
                i.status()
    elif a==4:
        ccc=input("enter to continue")
        mm=input("Enter Id of Member Returning")
        print("BOOKS BORROWED BY MEMBER")
        for i in lib.members:
            if i.id==mm:
                i.display_borrowed()
        bb=input("Enter of book id")
        lib.return_book(mm,bb)
    elif a==5:
        vv=input("enter to continue")
        lib.display_members()
    elif a==6:
        vb=input("enter to cont")
        bi=input("enter book name to search")
        lib.search_book(bi)
    elif a==7:
        lib.display_members()
   except Exception as e:
       print(e)



