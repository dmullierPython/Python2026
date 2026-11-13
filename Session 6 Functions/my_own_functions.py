# functions should be defined either in a separate file and imported, or in the same file above the main code that calls them.
# When run directly "__name__" will be "__main__", when imported it will be "__my_own_functions--"
import random
if __name__ != "__main__":
    print("--------------------------------------------\n-Random number functions have been imported-\n--------------------------------------------")
# takes no parameters and returns nothing, just prints a random number between 1 and 100
def print_random_int():
    random_number = random.randint(1, 100)
    print(random_number)

# takes no parameters and returns a random number between 1 and 100
def random_int():
    random_number = random.randint(1, 100)
    return random_number

# takes one parameter, maximum, and returns a random number up to maximum
def random_int_range(maximum):
    random_number = random.randint(0,maximum)
    return random_number

def random_int_range2(maximum=100  ):
    random_number = random.randint(0, maximum)
    return random_number


# This set of functions could be imported and used in another program. We can tell if it has been imported by checking the __name__ variable. If it is "__main__" then it is being run as a program, otherwise it has been imported.
# so, the code below will only run when it isn't being imported but run as a script, see the program that does import it, importing_my_own_functions.py, to see that it doesn't run the code below.
if __name__ == "__main__":
    print("==============\n=Welcome to the my_own_functions library=\n==============")
    print("blah blah blah, here's some examples, why not import it into your own code?")
    print("import my_own_functions")
    print("\nprint_random_int() prints a random integer")
    print_random_int()

    print("random_int() returns a random integer (0-100)")
    random_integer = random_int()
    print(random_integer)

    print(" random_int_range(range) returns a random integer (0-range)")
    print(random_int_range(50))

    print("random_int_range2(range) returns a random integer (0-range) or (o-100) if no value is passed")
    print(random_int_range2(10000))

    print("random_int_range2() with no value returns random value 0-100")
    print(random_int_range2())

    # demonstrating local variable
    random_num = 10
    print(f"Random integer before call ({random_num})")
    new_number = random_int_range(100)
    print(f"Random integer after call ({random_num})\nNew random integer ({new_number})")


