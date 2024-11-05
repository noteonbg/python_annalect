# Sample user data (username: password)
user_data = {
    "user1": "password123",
    "user2": "mypassword",
    "admin": "adminpass"
}

def authenticate(username, password):
    """Check if the username and password match."""
    if username in user_data and user_data[username] == password:
        return True  # User is authenticated
    else:
        return False  # Authentication failed

def main():
    print("Welcome to the User Authentication System")
    
    # Get user input for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Authenticate the user
    if authenticate(username, password):
        print("Authentication successful! Welcome!")
    else:
        print("Authentication failed! Please check your username and password.")

# Run the authentication system
if __name__ == "__main__":
    main()
