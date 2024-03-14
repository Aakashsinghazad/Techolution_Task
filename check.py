from storage import Storage

class CheckManager:
   """
   This class is responsible for managing book checks in and out for users.
   It uses an instance of the Storage class to load and save checks.
   """
   def __init__(self):
       """
       Initialize a CheckManager object with a Storage instance.
       """
       self.storage = Storage()

   
   def check_out_book(self, user_id, isbn):
        # Checking if the user exists
        users = self.storage.load_users()
        user_exists = False
        for user in users:
            if user["user_id"] == user_id:
                user_exists = True
                break
        if not user_exists:
            print(f"User with ID {user_id} does not exist. Unable to check out the book.")
            return

        # Checking if the book exist
        books = self.storage.load_books()
        book_exists = False
        for book in books:
            if book["isbn"] == isbn:
                book_exists = True
                break

        if not book_exists:
            print(f"Book with ISBN {isbn} does not exist. Unable to check out the book.")
            return

        # If both user and book exist, proceeding to check out the book
        check = {"user_id": user_id, "isbn": isbn, "checked_out": True}
        checks = self.storage.load_checks()
        checks.append(check)
        self.storage.save_checks(checks)
        print("Book checkout")


   def check_in_book(self, user_id, isbn):
        
        checks = self.storage.load_checks()
        # Checking if the user and book exist in the check JSON
        user_exists = any(check["user_id"] == user_id for check in checks)
        book_exists = any(check["isbn"] == isbn for check in checks)
        
        if not user_exists:
            print(f"User with ID {user_id} has not checked out any books. Unable to check in the book.")
            return
        if not book_exists:
            print(f"Book with ISBN {isbn} has not been checked out. Unable to check in the book.")
            return

        # Updating the checked_out status for the specified user and book
        for check in checks:
            if check["user_id"] == user_id and check["isbn"] == isbn:
                check["checked_out"] = False
                print("Book checked in successfully.")
                break
        self.storage.save_checks(checks)


   def list_checks(self):
       """
       Printing the list of checks, displaying user ID, ISBN, and checked_out status.
       """
       checks = self.storage.load_checks()
       if len(checks)==0:
            print("No book available")
       for check in checks:
           print(f"User ID: {check['user_id']}, ISBN: {check['isbn']}, Checked Out: {check['checked_out']}")