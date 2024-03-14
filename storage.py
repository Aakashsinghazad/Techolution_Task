import json

class Storage:
   """
   This class is responsible for handling the storage and retrieval of data in JSON files.
   It has methods to save and load data for books, users, and checks.
   If a file is not found, an empty list is returned.
   """
   def __init__(self):
       """
       Initializes the Storage class with three file names for books, users, and checks.
       """
       self.books_file = "books.json"
       self.users_file = "users.json"
       self.checks_file = "checks.json"

   def save_books(self, books):
       """
       Saves the given list of books to the books.json file.
       """
       with open(self.books_file, "w") as f:
           json.dump(books, f)

   def load_books(self):
       """
       Loads the books data from the books.json file.
       Returns:
       list: The deserialized list of books from the JSON file or an empty list if the file is not found.
       """
       try:
           with open(self.books_file, "r") as f:
               return json.load(f)
       except FileNotFoundError:
           return []

   def save_users(self, users):
       """
       Saves the given list of users to the users.json file.
       """
       with open(self.users_file, "w") as f:
           json.dump(users, f)

   def load_users(self):
       """
       Loads the users data from the users.json file.
       Returns:
       list: The deserialized list of users from the JSON file or an empty list if the file is not found.
       """
       try:
           with open(self.users_file, "r") as f:
               return json.load(f)
       except FileNotFoundError:
           return []

   def save_checks(self, checks):
       """
       Saves the given list of checks to the checks.json file.
       """
       with open(self.checks_file, "w") as f:
           json.dump(checks, f)

   def load_checks(self):
       """
       Loads the checks data from the checks.json file.
       Returns:
       list: The deserialized list of checks from the JSON file or an empty list if the file is not found.
       """
       try:
           with open(self.checks_file, "r") as f:
               return json.load(f)
       except FileNotFoundError:
           return []