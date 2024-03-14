from storage import Storage 

class UserManager:
   """
   UserManager class is responsible for managing users in the system.
   It uses Storage class to load, save, and manipulate user data.
   """

   def __init__(self):
       """
       Initialize UserManager instance with Storage instance.
       """
       self.storage = Storage()

   def add_user(self, name, user_id):
        """
        Add a new user with the given name and user_id to the users list.
        """
        # Checking if the user ID already exists
        users = self.storage.load_users()
        for user in users:
            if user['user_id'] == user_id:
                print(f"User with the given ID {user_id} already exists.")
                return 

        # If the user ID doesn't exist, adding the new user
        new_user = {"name": name, "user_id": user_id}
        users.append(new_user)
        self.storage.save_users(users)
        print("User added successfully.")

   def update_user(self, user_id, name=None):
    """
    Update the user with the given user_id and name (optional).
    """
    users = self.storage.load_users() 
    # Check if the user with the given user ID exists
    user_found = False
    for user in users:
        if user["user_id"] == user_id:
            user_found = True
            if name:
                user["name"] = name  

    if not user_found:
        print(f"User with the ID {user_id} does not exist.")
        return  
    self.storage.save_users(users)  
    print("User Updated")

   #Delete the user
   def delete_user(self, user_id):
       """
       Delete the user with the given user_id.

       Parameters:
       user_id (str): The user's unique ID.
       """
       users = self.storage.load_users() 
       users = [user for user in users if user["user_id"] != user_id]
       self.storage.save_users(users) 
   def list_users(self):
       """
       Print the list of all users in the system.
       """
       users = self.storage.load_users()
       for user in users:
           print(f"Name: {user['name']}, User ID: {user['user_id']}")

   
   
   def search_user(self, **kwargs):
       """
       Search for users that match the given keyword arguments.
       """
       users = self.storage.load_users()  
       results = []
       for user in users:
           match = True
           for key, value in kwargs.items():
               if user.get(key) != value:
                   match = False
                   break
           if match:
               results.append(user)
       return results 