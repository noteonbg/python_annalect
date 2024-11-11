class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"


# Generator function that yields Person objects
def person_generator(names, ages):
    for name, age in zip(names, ages):
        yield Person(name, age)


# Sample input data
names = ["Alice", "Bob", "Charlie", "Diana"]
ages = [25, 30, 17, 22]

# Create a generator object
person_gen = person_generator(names, ages)

# Using the generator to iterate over Person objects
for person in person_gen:
    print(person)
