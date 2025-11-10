class Book:
    def __init__(self, title: str, author:str, ISBN:int):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_available =True


    def __str__(self):
        return f"title: {self.title},author: {self.author}, {"available" if self.is_available else "not available"}, ISBN: {self.ISBN}"