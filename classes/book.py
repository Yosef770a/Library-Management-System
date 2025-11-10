class Book:
    def __init__(self,  ISBN:int, title: str, author:str):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.is_available =True


    def __str__(self):
        return f"title: {self.title},author: {self.author}, {"available" if self.is_available else "not available"}, ISBN: {self.ISBN}"