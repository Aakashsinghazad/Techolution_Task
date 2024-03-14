class Book:
   """
   This class represents a Book with properties title, author, and isbn.
   """
   def __init__(self, title, author, isbn):
       self.title = title
       self.author = author
       self.isbn = isbn

   def display_dict(self):
       """
       Convert the Book object to a dictionary representation.
       """
       return {
           "title": self.title,
           "author": self.author,
           "isbn": self.isbn
       }

class User:
   """
   This class represents a User with properties name and user_id.
   """
   def __init__(self, name, user_id):
       self.name = name
       self.user_id = user_id

   def display_dict(self):
       """
       Convert the User object to a dictionary representation.
       """
       return {
           "name": self.name,
           "user_id": self.user_id
       }

