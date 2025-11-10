from book import Book
from library import Library
from user import User
my_library=Library()
def menu():
    choice = None 
    user_name = ""
    user_id = ""
    while choice != "7": 
        print("click on 1 number to add a library subscription. click 2 to borrow a book. click 3 to return  a book. click 4 to add a book to the library .click on  7 to leave the library website.") 
        choice = input("Enter your choice: ")    
        if choice == "1": 
            user_name = input("Please enter your name ")
            user_id = input("please enter your id number ")
            my_library.add_user(User(user_name,user_id))
        elif choice == "2":
            book_number=input("please enter the book id number")
            user_id=input("enter yoer id number")
            my_book=my_library.borrow_book(user_id,book_number)
            print(my_book)

 
        elif choice == "3": 

            break    
             
        

        
menu()
print(my_library.list_of_users[0])
