from typing import List, Optional

#Without List, Python's type system wouldn't know if a list contains integers,
#  strings, or any other type. With List[str], you're telling both the developer 
# and type-checking tools that this list is intended to hold only strings.

class User:
    def __init__(self, name: str, age: Optional[int], roles: List[str]):
        self.name = name
        self.age = age
        self.roles = roles

# Creating a User instance with a list of roles and an optional age
user = User(name="abc", age=None, roles=["admin", "user"])

print(user.name)  # "abc"
print(user.age)   # None
print(user.roles) # ["admin", "user"]
