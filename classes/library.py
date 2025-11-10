from user import User
from book import Book
class Library:
    def __init__(self):
        self.list_of_books=[]
        self.list_of_users=[]

    def __str__(self):
        return f"  books {self.list_of_books}, users {self.list_of_users}"

    def add_book(self,book):
        self.list_of_books.append(book)
        return self.list_of_books
    

    def add_user(self,user):
        self.list_of_users.append(user)
        return self.list_of_users
    
    
        


      