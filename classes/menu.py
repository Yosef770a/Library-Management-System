from book import Book
from library import Library
from user import User
library=Library()
def menu():
    choice = None 
    while choice != "7": 
        print("""
    Menu: 
    1 Add a library subscription
    2 Add a book to the library
    3 Borrow a book from the library
    4 Return a book to the library
    5 View all available books
    6 Search for a book by title or author
    7 Exit
              """) 
        choice = input("Enter your choice: ")    
        if choice == "1": 
            user_name = input("Please enter the subscriber name: ")
            user_id = input("please enter the subscriber id number: ")
            library.add_user(User(user_name, user_id))

        elif choice == "2":
             ISBN = input("Enter ISBN: ")
             title = input("Enter the book title: ")
             author = input("Enter the author's name: ")
             library.add_book(Book(ISBN, title, author))
            
        elif choice == "3":
            user_id=input("please enter the subscriber id number: ")
            book_number=input("Enter the book's ISBN: ")
            print(library.borrow_book(user_id, book_number))

        elif choice == "4":
            user_id=int(input("please enter the subscriber id number: "))
            book_number=int(input("Enter the book's ISBN: "))
            print(library.return_book(user_id,book_number))

        elif choice=="5":
            library.list_available_books()

        elif choice=="6":
            search_content = input("Please enter the name or title of the book to search for: ")
            library.search_book(search_content)

