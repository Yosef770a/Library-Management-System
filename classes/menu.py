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
            user_name = input("\nPlease enter the subscriber name: ")
            user_id = input("please enter the subscriber id number: ")
            print(library.add_user(User(user_name, user_id)))

        elif choice == "2":
             ISBN = input("\nPlease enter ISBN: ")
             title = input("Enter the book title: ")
             author = input("Enter the author's name: ")
             library.add_book(Book(ISBN, title, author))
            
        elif choice == "3":
            user_id=input("\nplease enter the subscriber id number: ")
            book_number=input("Enter the book's ISBN: ")
            print(library.borrow_book(user_id, book_number))

        elif choice == "4":
            user_id=input("\nplease enter the subscriber id number: ")
            book_number=input("Enter the book's ISBN: ")
            print(library.return_book(user_id,book_number))

        elif choice=="5":
            if library.list_available_books():
                print(f"\nThere are {len(library.list_available_books())} books available\n")
                for i,book in enumerate(library.list_available_books()):
                    print(f"{i+1}. ISBN: {book.ISBN}, Title: {book.title}, Author: {book.author}")
                print("\nEnd of list")
            else:
                print("\nNo available books found")
                

        elif choice=="6":
            search_content = input("\nPlease enter the name or title of the book to search for: ")
            library.search_book(search_content)

menu()