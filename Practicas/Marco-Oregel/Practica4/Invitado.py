from RoleProtocol import RoleProtocol
from Book import Book 
class Invitado(RoleProtocol):

    def __init__(self, name,admin):
        super().__init__(name)
        self.admin = admin
        

    def loginProcess(self):
        print(f"You are logged in as a guest, Welcome {self._name}!")
        print("Here are all our books: ")
        self.showAllBooks()
        print("If you want to borrow a book, you need to log in as a user.")

    
    def showAllBooks(self):
        print("All our books:")
        for book in self.admin.catalog:
            print(book.description()) 