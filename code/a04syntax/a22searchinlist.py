class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
    
    # Override equality to compare two Person objects based on their attributes
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

# Create a list of Person objects
people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35),
    Person("Bob", 25)  # Another person with the same name and age
]

# Remove a specific Person object
person_to_remove = Person("Bob", 25)

# Using remove() to remove the first matching object
people.remove(person_to_remove)

# Output the modified list
print(people)
