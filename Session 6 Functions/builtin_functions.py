# These examples show some uses of Python's built in functions.

# some functions that are built into Python and don't need to be imported.
print(dir(__builtins__))
# the main ones are
#• Core Functions: print(), input(), type(), range(), sum(), max(), min(), abs()
#• Data Type Constructors: str(), int(), float(), list(), dict(), set(), tuple()

# Working with a String (counts characters)
length = len("hello")
print(f"number of letters in hello is {length}")         # Output: 5

# Working with a List (counts elements) and calling the len() function inside the print() function
print(len(["apple", "banana", "cherry"]))  # Output: 3

# Working with a Dictionary (counts key-value pairs)
print(len({"Alice": 95, "Bob": 82}))       # Output: 2

# Working with a list of numbers (numerical order)
print(sorted([5, 2, 9, 1]))     # Output: [1, 2, 5, 9]

# Working with a string (alphabetical order of characters)
print(sorted("python"))         # Output: ['h', 'n', 'o', 'p', 't', 'y']

# With Numbers: It performs mathematical addition
print(5 + 10)               # Output: 15

# With Strings: It glues them together (concatenation)
print("Hello, " + "World!") # Output: Hello, World!

# Some examples of using functions incorrectly
# comment out each one to run the nexdt one (as the first one encountered will stop execution
#print(len())
#print(len("hello", "world"))
#print(len(12345))
