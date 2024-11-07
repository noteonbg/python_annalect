# Importing necessary modules
import re

class User:
    """A class to represent a user for login authentication."""

    def __init__(self, username, password):
        """Initialize the User with username and password."""
        self.username = username
        self.password = password

    def __str__(self):
        """Return a string representation of the User object."""
        return f"User(username={self.username})"


class LoginSystem:
    """A class to handle user login functionality."""

    def __init__(self):
        """Initialize the login system with an empty list of users."""
        self.users = []

    def add_user(self, username, password):
        """
        Add a new user to the system.
        
        The username must be unique and password must follow certain rules:
        - At least 8 characters long
        - Contains at least one letter and one number
        """
        if self.is_username_taken(username):
            raise ValueError(f"Username '{username}' is already taken.")
        
        if not self.is_valid_password(password):
            raise ValueError("Password must be at least 8 characters long and contain at least one letter and one number.")

        user = User(username, password)
        self.users.append(user)

    def is_username_taken(self, username):
        """Check if the username is already taken."""
        return any(user.username == username for user in self.users)

    def is_valid_password(self, password):
        """
        Check if the password is valid.
        
        A valid password:
        - Is at least 8 characters long
        - Contains at least one letter and one number
        """
        if len(password) < 8:
            return False
        if not re.search(r"[a-zA-Z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        return True

    def authenticate(self, username, password):
        """
        Authenticate the user by checking if the username and password match.
        
        Returns True if authentication is successful, else False.
        """
        user = self.find_user(username)
        if user and user.password == password:
            return True
        return False

    def find_user(self, username):
        """Find a user by username."""
        for user in self.users:
            if user.username == username:
                return user
        return None


# Example usage:
if __name__ == "__main__":
    login_system = LoginSystem()
    
    # Adding users to the system
    try:
        login_system.add_user("abc", "Password123")
        login_system.add_user("def", "SecurePass1")
    except ValueError as e:
        print(f"Error: {e}")

    # Authenticating users
    print(login_system.authenticate("abc", "Password123"))  # True
    print(login_system.authenticate("def", "WrongPassword"))  # False

"""

Key PEP 8 Guidelines 

Imports are on top of the file. If there were more imports, we would group them into standard libraries, third-party libraries, and application-specific imports.
Each import is on a separate line.

Class names follow the CapWords convention. Each word in the class name starts
 with a capital letter.

 Method and function names are written in lowercase with words separated by underscores 
 (snake_case).

Docstrings:

Each class and method includes a docstring (triple quotes) that
describes its purpose and behavior. Docstrings are placed immediately 
after the function or class definition.

Line Length:
Lines should not exceed 79 characters. If they do, break them into
multiple lines (e.g., long strings or function calls). In this example,
the lines are kept short to maintain readability.

Blank Lines:
Two blank lines are used before class and function definitions to separate them from the surrounding code. This improves readability.
One blank line is used to separate methods within the class.

Variable names are written in lowercase, with words separated by underscores.

things to avoid
Use of Mixed Case in Variables:
For example, using userName instead of user_name.

Long Lines:
Lines exceeding 79 characters make the code hard to read and should be avoided. Break long expressions into multiple lines.

Too Little or Too Much Whitespace:
There should be no extra spaces around parentheses, function calls, or assignments.

Inconsistent Naming:
The code should consistently use either snake_case 
(for variables and function names) or
CamelCase (for classes) — not a mixture of both.












"""
