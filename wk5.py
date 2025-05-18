class Book:
    def __init__(self, title, author, publication_year, genre):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.is_borrowed = False

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author} ({self.publication_year}), Genre: {self.genre}, Borrowed: {self.is_borrowed}"

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed.")

class EBook(Book):  # Inheritance: EBook is a type of Book
    def __init__(self, title, author, publication_year, genre, file_format):
        super().__init__(title, author, publication_year, genre)
        self.file_format = file_format
        self.reader_app = None

    def __str__(self):
        return f"{super().__str__()} (EBook, Format: {self.file_format}, Reader App: {self.reader_app})"

    def set_reader_app(self, app_name):
        self.reader_app = app_name
        print(f"'{self.title}' can be read with {self.reader_app}.")

# Creating instances of Book and EBook
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979, "Science Fiction")
ebook1 = EBook("Pride and Prejudice", "Jane Austen", 1813, "Romance", "EPUB")

print(book1)
print(ebook1)

book1.borrow()
print(book1)
book1.return_book()
print(book1)

ebook1.set_reader_app("Kindle")
ebook1.borrow()
print(ebook1)
