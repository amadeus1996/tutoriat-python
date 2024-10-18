# 1. Hello World: Simple syntax, no need for a main function or headers
def hello_world():
    print("Hello, Python World!")

# 2. Variables and Dynamic Typing
def variable_types():
    # No need to declare types in Python
    x = 42           # Integer
    pi = 3.1415      # Float
    name = "Alice"   # String
    is_active = True # Boolean
    
    print(f"x: {x}, pi: {pi}, name: {name}, is_active: {is_active}")
    print(f"Type of x: {type(x)}, Type of pi: {type(pi)}")

# 3. Control Flow: if-else and loops
def control_flow():
    x = 4
    if x > 5:
        print(f"{x} is greater than 5")
    elif x > 3:
        print(f"{x} is between 3 and 5")
    else:
        print(f"{x} is less than or equal 3")

    # Loops are similar but with different syntax
    for i in range(5):
        print(f"Loop {i}")

    # While loop
    count = 0
    while count < 3:
        print(f"While loop count: {count}")
        count += 1

# 4. Functions: No need for return types or argument types
def add(a, b):
    return a + b

def demonstrate_functions():
    result = add(10, 5)
    print(f"10 + 5 = {result}")

# 5. Lists: Dynamic arrays in Python
def list_operations():
    numbers = [1, 2, 3, 4, 5]
    print("List:", numbers)
    
    # Append to list
    numbers.append(6)
    print("After appending:", numbers)
    
    # Slicing
    sublist = numbers[2:5]
    print("Sliced list:", sublist)
    
    # List comprehensions
    squares = [x ** 2 for x in numbers]
    print("Squares:", squares)

# 6. Dictionaries: Key-Value Pairs
def dictionary_operations():
    student = {
        "name": "Alice",
        "age": 20,
        "gpa": 9.75
    }
    print("Dictionary:", student)
    
    # Access value by key
    print(f"Name: {student['name']}, Age: {student['age']}")
    
    # Add new key-value
    student["major"] = "Computer Science"
    print("Updated Dictionary:", student)

# 7. Strings: Python makes string manipulation easy
def string_operations():
    s = "Hello, World!"
    print("Original String:", s)
    
    # String concatenation
    full_name = "Alice" + " " + "Smith"
    print("Concatenated String:", full_name)
    
    # f-strings for formatting
    age = 20
    print(f"{full_name} is {age} years old.")
    
    # String slicing
    print("First 5 characters:", s[:5])
    
    # String methods
    print("Uppercase:", s.upper())
    print("Lowercase:", s.lower())
    print("Reversed:", s[::-1])  # Reverse string using slicing

# 8. Exception Handling
def demonstrate_exceptions():
    try:
        x = 5 / 0
    except ZeroDivisionError:
        print("You can't divide by zero!")

# 9. Classes and Objects
class Dog:
    # Constructor
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    # Method
    def bark(self):
        print(f"{self.name} says: Woof!")
        
def demonstrate_classes():
    my_dog = Dog("Rex", "German Shepherd")
    my_dog.bark()

# 10. File Handling: Reading and writing files
def file_operations():
    # Writing to a file
    with open('example.txt', 'w') as file:
        file.write("Hello, this is a test file.")
    
    # Reading from a file
    with open('example.txt', 'r') as file:
        content = file.read()
        print("File content:", content)

def trivia_question():
    a = [1,2,3,[4,5,6]]
    b = a.copy()
    a[3] = [4,5,7]
    #Ce se va afisa in acest print?
    print(b)

# Main function to run all examples
def main():
    print("1. Hello World:")
    hello_world()

    print("\n2. Variables and Dynamic Typing:")
    variable_types()

    print("\n3. Control Flow:")
    control_flow()

    print("\n4. Functions:")
    demonstrate_functions()

    print("\n5. Lists:")
    list_operations()

    print("\n6. Dictionaries:")
    dictionary_operations()

    print("\n7. Strings:")
    string_operations()

    print("\n8. Exceptions:")
    demonstrate_exceptions()

    print("\n9. Classes and Objects:")
    demonstrate_classes()

    print("\n10. File Handling:")
    file_operations()

    print("\n11. Trivia question:")
    # trivia_question()

# Entry point
if __name__ == "__main__":
    main()
