from book import BookManager
from user import UserManager
from check import CheckManager

def main_menu():
    """
    Displays the main menu of the Library Management System.
    """
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. List Books")
    print("5. Search Book")
    print("6. Add User")
    print("7. Update User")
    print("8. Delete User")
    print("9. List Users")
    print("10. Search User")
    print("11. Check Out Book")
    print("12. Check In Book")
    print("13. List Checkouts")
    print("14. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    """
    The main function that manages the Library Management System.
    It initializes the BookManager, UserManager, and CheckManager instances,
    and handles user choices in an infinite loop until the user decides to exit.
    """
    book_manager = BookManager()
    user_manager = UserManager()
    check_manager = CheckManager()

    while True:
        choice = main_menu()
        # Handle user's choice to add a book
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book_manager.add_book(title, author, isbn)
            
        # Handle user's choice to update a book
        elif choice == '2':
            isbn = input("Enter ISBN of the book to update: ")
            title = input("Enter new title (leave blank to keep current): ")
            author = input("Enter new author (leave blank to keep current): ")
            book_manager.update_book(isbn, title, author)
            
        # Handle user's choice to delete a book
        elif choice == '3':
            isbn = input("Enter ISBN of the book to delete: ")
            book_manager.delete_book(isbn)

        # Handle user's choice to list all books
        elif choice == '4':
            book_manager.list_books()

        # Handle user's choice to search for a book
        elif choice == '5':
            title = input("Enter title to search (leave blank to skip): ")
            author = input("Enter author to search (leave blank to skip): ")
            isbn = input("Enter ISBN to search (leave blank to skip): ")
            books = book_manager.search_book(title=title, author=author, isbn=isbn)
            if books:
                print("Matching books:")
                for book in books:
                    print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
            else:
                print("No matching books found.")
        
        # Handle user's choice to add a user
        elif choice == '6':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user_manager.add_user(name, user_id)
            
        
        # Handle user's choice to update a user
        elif choice == '7':
            user_id = input("Enter user ID of the user to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            user_manager.update_user(user_id, name)
            

        # Handle user's choice to delete a user
        elif choice == '8':
            user_id = input("Enter user ID of the user to delete: ")
            user_manager.delete_user(user_id)
            
        
        # Handle user's choice to list user
        elif choice == '9':
            user_manager.list_users()

        # Search for users based on name and user ID
        elif choice == '10':
            name = input("Enter user name to search (leave blank to skip): ")
            user_id = input("Enter user ID to search (leave blank to skip): ")
            users = user_manager.search_user(name=name, user_id=user_id)
            if users:
                print("Matching user:")
                for user in users:
                    print(f"Name: {user['name']}, User ID: {user['user_id']}")
            else:
                print("No matching users found.")
        
        # Checkout a book to a user
        elif choice == '11':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            check_manager.check_out_book(user_id, isbn)
            
        # Check-in a book from a user   
        elif choice == '12':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to check in: ")
            check_manager.check_in_book(user_id, isbn)

        # Display the list of checks
        elif choice == '13':
            check_manager.list_checks()

        # Exit the program
        elif choice == '14':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
