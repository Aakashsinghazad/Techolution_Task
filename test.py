from storage import Storage

class BookManager:
    def __init__(self):
        self.storage = Storage()

    def add_book(self, title, author, isbn):
        book = {"title": title, "author": author, "isbn": isbn}
        books = self.storage.load_books()
        print(books)
        books.append(book)
        self.storage.save_books(books)

bok=BookManager()
bok.add_book("R", "Aakash Singh",2309)