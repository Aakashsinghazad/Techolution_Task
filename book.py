from storage import Storage

class BookManager:
   """
   This class is responsible for managing books in a storage system.
   It provides methods to add, update, delete, list, and search books.
   """
   def __init__(self):
       """
       Initializes the BookManager class with a Storage object.
       """
       self.storage = Storage()

   def add_book(self, title, author, isbn):
       """
       Adds a new book to the storage system with the given title, author, and isbn.
       """
   def add_book(self, title, author, isbn):
        book = {"title": title, "author": author, "isbn": isbn}
        books = self.storage.load_books()
        
        # Checking if a book with the same ISBN already exists
        for existing_book in books:
            if existing_book["isbn"] == isbn:
                print("A book with the ISBN {isbn} already exists.")
                return  
        # checking If the book does not exist, append it to the list of books
        books.append(book)
        self.storage.save_books(books)
        print("Book added successfully.")

   
   def update_book(self, isbn, title=None, author=None):
        """
        Updates the book with the given ISBN in the storage system.
        """
        books = self.storage.load_books()
        book_found = False

        for book in books:
            if book['isbn'] == isbn:
                book_found = True
                if title:
                    book['title'] = title
                if author:
                    book['author'] = author

        if book_found:
            self.storage.save_books(books)
            print("Book updated successfully.")
        else:
            print("Book with the given ISBN does not exist.")


   def delete_book(self, isbn):
        """
        Deletes the book with the given ISBN from the storage system.
        """
        books = self.storage.load_books()
        books_to_keep = [book for book in books if book['isbn'] != isbn]

        if len(books_to_keep) == len(books):
            print("Book with the given ISBN does not exist.")
        else:
            self.storage.save_books(books_to_keep)
            print("Book deleted successfully.")


   def list_books(self):
       """
       Lists all books in the storage system.
       """
       books = self.storage.load_books()
       for book in books:
           print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")

   def search_book(self, **kwargs):
       """
       Searches for books in the storage system that match the given criteria.
       """
       books = self.storage.load_books()
       results = []
       for book in books:
           match = True
           for key, value in kwargs.items():
               if book.get(key) != value:
                   match = False
                   break
           if match:
               results.append(book)
       return results