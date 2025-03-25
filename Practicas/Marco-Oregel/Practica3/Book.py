class Book:

    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.isBorrowed = False

    def description(self):
        return f"- {self.title} by {self.author} - {"Borrowed" if self.isBorrowed else "Available"}"
        