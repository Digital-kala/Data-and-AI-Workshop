# --- Opening and Closing Files ---

# Open the file "example.txt" for reading
file1 = open("example.txt", "r")
# Close the file
file1.close()

# Open the file "example.txt" for writing, using 'with' to ensure it closes automatically
with open("example.txt", "w") as file2:
    pass  # Do nothing (just opening and closing the file)


# --- Reading a File ---

# Open the file "example.txt" for reading, using 'with' to ensure it closes automatically
with open("example.txt", "r") as file:
    lines = file.readlines()  # Read all lines from the file
    for line in lines:
        print(line)  # Print each line


# --- Writing a File ---

# Open the file "example.txt" for appending, using 'with' to ensure it closes automatically
with open("example.txt", "a") as file:
    file.write("\nThis is a new line\n")  # Write a new line to the file


# --- Classes and Objects ---

class Person:
    # This method initialises the Person class with name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # This method prints a greeting with the person's name and age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create a Person object named "Alice" who is 30 years old
person = Person("Alice", 30)

# Call the greet method to print the greeting
person.greet()