import my_own_functions #this causes execution to jump to my_own_functions but __name__ will not be "__main--" it will be "__my_own_functions--"

if __name__ == "__main__":
    random_value = my_own_functions.random_int_range(55)
    print(random_value)