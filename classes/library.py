
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
             
    def borrow_book(self, user_id, book_isbn):
        for book in self.list_of_books:
            if book.ISBN == book_isbn:
                if book.is_available:
                    for user in self.list_of_users:
                        if user.id == user_id:
                            user.borrowed_books.append(book)
                            book.is_available = False
                            return f"The book has been successfully loaned to you {user.name}"
                    return "User not found"
                else:
                    return "The requested book is not available"
        return "Book does not exist"


    def return_book(self, user_id, book_isbn):
        for book in self.list_of_books:
            if book.ISBN == book_isbn:
                if not(book.is_available):
                    for user in self.list_of_users:
                        if user.id == user_id:
                            user.borrowed_books.remove(book)
                            book.is_available = True
                            return f"The book was successfully returned to the library"
                    return "User not found"
                else:
                    return "The book is already available"
        return "Book does not exist"

