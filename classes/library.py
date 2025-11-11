
class Library:
    def __init__(self):
        self.list_of_books=[]
        self.list_of_users=[]

    def __str__(self):
        return f"books {self.list_of_books},users {self.list_of_users},"

    def add_book(self,book):
        for bookf in self.list_of_books:
            if book.ISBN == bookf.ISBN:
                return "\nThe book already exists in the library"
        self.list_of_books.append(book)
        return "\nThe book has been successfully added to the library"
    
    def add_user(self,user):
        for userf in self.list_of_users:
            if user.id == userf.id:
                return "\nThe subscription already exists in the system" 
        self.list_of_users.append(user)
        return "\nThe subscription has been successfully added to the system"
                
    
    def list_available_books(self):
        list_of_available_books=[]
        for book in self.list_of_books:
            if book not in list_of_available_books:
                if book.is_available:
                    list_of_available_books.append(book)               
            else:
                if not book.is_available:
                    list_of_available_books.pop(book)
        return list_of_available_books


    def search_book(self,search_content):
        for book in self.list_of_books:
            if book.title == search_content or book.author==search_content:
                print (f"We have the {book.title} by {book.author}, ISBN: {book.ISBN} ")
                return True
            
        print(f"We don't have this book")
        return False
             
    def borrow_book(self, user_id, book_isbn):
        for book in self.list_of_books:
            if str(book.ISBN) == book_isbn:
                if book.is_available:
                    for user in self.list_of_users:
                        if str(user.id) == user_id:
                            user.borrowed_books.append(book)
                            book.is_available = False
                            return f"\n The book was successfully loaned to user {user.name}"
                    return "User not found"
                else:
                    return "The requested book is not available"
        return "Book does not exist"


    def return_book(self, user_id, book_isbn):
        for book in self.list_of_books:
            if str(book.ISBN) == book_isbn:
                if not(book.is_available):
                    for user in self.list_of_users:
                        if str(user.id) == user_id:
                            user.borrowed_books.remove(book)
                            book.is_available = True
                            return f"The book was successfully returned to the library"
                    return "User not found"
                else:
                    return "The book is already available"
        return "Book does not exist"