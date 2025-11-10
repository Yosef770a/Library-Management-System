class User:
    def __init__(self,name:str,id:int,borrowed_books:list):
        self.name=name
        self.id=id
        self.borrowed_books=borrowed_books
    def __str__(self):
        return f"name {self.name}, id {self.id}, borrowd_books {self.borrowed_books}"    
        




       