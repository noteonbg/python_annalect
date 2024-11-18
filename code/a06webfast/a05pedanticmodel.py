from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

# Define the Pydantic model
class User(BaseModel):
    id: int
    name: str
    email: EmailStr  # Pydantic will validate that this is a valid email address
    age: Optional[int] = None  # age is optional, default is None
    active: bool = True  # default value is True
    roles: List[str] = []  # a list of roles, default is an empty list

    # Custom validation
    @classmethod
    def validate_roles(cls, v):
        if not v:
            raise ValueError("Roles must have at least one value")
        return v

# Example of using the Pydantic model to create a user

# Valid data
user_data = {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "age": 23,
    "roles": ["admin", "user"]
}

# Creating a User object using valid data
user = User(**user_data)
print(user)


# Converting the User object to JSON (string)
user_json = user.model_dump_json()  # This converts the Pydantic model to a JSON string
print("User as JSON:")
print(user_json)

# Now let's parse the JSON string back into a Pydantic model
user_from_json = User.parse_raw(user_json)
print("\nUser object parsed from JSON:")
print(user_from_json)
