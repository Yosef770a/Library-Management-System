
class Library:
    def __init__(self):
        self.list_of_books=[]
        self.list_of_users=[]

    def __str__(self):
        return f"  books {self.list_of_books}, users {self.list_of_users}"


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


