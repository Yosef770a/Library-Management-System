from user import User
from book import Book
class Library:
    def __init__(self):
        self.list_of_books=[]
        self.list_of_users=[]

    def __str__(self):
        return f"  books {self.list_of_books}, users {self.list_of_users},"

    def add_book(self,book):
        self.list_of_books.append(book)
        return self.list_of_books
    

    def add_user(self,user):
        self.list_of_users.append(user)
        return self.list_of_users
    
    def list_available_books(self):
        self.list_of_available_books=[]
        for book in self.list_of_books:
            if book not in self.list_of_available_books:
                if book.is_available==True:
                    self.list_of_available_books.append(book)
                  
            else:
                if book.is_available==False:
                    self.list_of_available_books.pop(book)
        return self.list_of_available_books



    def search_book(self,Search_name):
        for book in self.list_of_books:
            if book.title == Search_name or book.author==Search_name:
                return f"We have the {book.title} by {book.author}"
            
        return (f"We don't have this book")
             



                    

                  
                









    
    
        


      