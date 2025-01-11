# Base class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_summary(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."

    def read(self):
        return f"You start reading '{self.title}'."

# Subclass demonstrating inheritance
class Ebook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size 

    def download(self):
        return f"Downloading '{self.title}'... ({self.file_size} MB)"

    # Overriding a method
    def read(self):
        return f"You start reading '{self.title}' on your e-reader."

# Create instances
physical_book = Book("1984", "George Orwell", 328)
ebook = Ebook("Brave New World", "Aldous Huxley", 288, 2.5)

# Test methods
print(physical_book.get_summary())
print(physical_book.read())
print(ebook.get_summary())
print(ebook.download())
print(ebook.read())
