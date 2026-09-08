# E28.Library Management System in Python.
class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []
    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)
    def showInfo(self):
        print(f"The Library has {self.noBooks} Books.\nThe Books are :")
        for book in self.books:
            print(book)
l1 = Library()
l1.addBook("Harry Potter and the Sorcerer's Stone.")
l1.addBook("Harry Potter and the Chamber of Secrets.")
l1.addBook("Harry Potter and the Prisoner of Azkaban.")
l1.addBook("Harry Potter and the Goblet of Fire.")
l1.addBook("Harry Potter and the Order of the Phoenix.")
l1.addBook("Harry Potter and the Half-Blood Prince.")
l1.addBook("Harry Potter and the Deathly Hallows Part 1.")
l1.addBook("Harry Potter and the Deathly Hallows Part 2.")
l1.showInfo()