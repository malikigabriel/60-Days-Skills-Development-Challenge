# Python Functions Exercises: 18 Coding Problems with Solutions
# Exercise 1. Create a Function with Parameters
def demo(name, age):
    # Print the values passed into the function
    print(name, age)

# Call the function with specific arguments
demo("Kelly", 25)


# Exercise 2. Variable Length of Arguments (*args)
def func1(*args):
    print("Printing values:")
    for i in args:
        print(i)

# Calling with 3 arguments
func1(20, 40, 60)

# Calling with 2 arguments
func1(80, 100)


#Exercise 3. Return Multiple Values from a Function
def calculation(a, b):
    addition = a + b
    subtraction = a - b
    # Return multiple values separated by comma
    return addition, subtraction

# Get results in a single line
res = calculation(40, 10)
print(res)


# Exercise 4. Function with Default Argument
def showEmployee(name, salary=9000):
    print("Name:", name, "Salary:", salary)

# Call the function with and without the salary argument
showEmployee("Ben", 12000)
showEmployee("Jess")


# Exercise 5. Create an Inner Function
def outer_function():
    print("This is the outer function")

    def inner_function():
        print("This is the inner function")

    inner_function()

# Call the outer function
outer_function()


# Exercise 5b Create an Inner Function
def outer_func(a, b):
    # Inner function
    def addition(a, b):
        return a + b

    # Call inner function and add 5 to the result
    add = addition(a, b)
    return add + 5

result = outer_func(5, 10)
print(result)


#Exercise 6. Create a Recursive Function
def addition(num):
    if num:
        # Recursive Case: add current num to the result of addition(num - 1)
        return num + addition(num - 1)
    else:
        # Base Case: stop at 0
        return 0

res = addition(10)
print(res)

#Exercise 7. Assign a Different Name to Function and Call It
def display_student(name, age):
    print(name, age)

# Assign the function object to a new variable name
show_student = display_student

# Call the function using the new name
show_student("Emma", 26)


#Exercise 8. Generate a List of Even Numbers (Range Function)
def even_numbers():
    # range(start, stop, step)
    # Use 30 as stop to exclude 30, or 31 to include it if required
    return list(range(4, 30, 2))

print(even_numbers())


# Exercise 9. Find the Largest Item in a List
def find_largest(list_input):
    # Assume the first item is the largest
    largest = list_input[0]
    for num in list_input:
        if num > largest:
            largest = num
    return largest

x = [4, 6, 8, 24, 12, 2]
print(find_largest(x))


#Exercise 10. Call Function using Positional and Keyword Arguments
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.\n")

# Positional arguments: Order matters
describe_pet("hamster", "Harry")

# Keyword arguments: Order does not matter
describe_pet(pet_name="Willie", animal_type="dog")


# Exercise 11. Create a Function with Keyword Arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling with three different pieces of named data
print_info(name="Gabriel", age=42, city="Lagos")
print_info(name="Alice", age=30, city="New York")
print_info(name="Bob", age=35, city="Chicago")
print_info(name="Ben", age=27, city="Iyara")


# Exercise 12. Modifying Global Variables
global_var = 10

def modify_variable():
    global global_var  # Access the variable from the global scope
    global_var = 20

print("Initial:", global_var)
modify_variable()
print("Modified:", global_var)


# Exercise 13. Recursive Factorial (Non-Negative Integers)
def recur_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * recur_factorial(n - 1)

num = 5
print(f"The factorial of {num} is {recur_factorial(num)}")


# Exercise 14. Create a Lambda Function to Square a Number
# Define the lambda and assign it to a variable
square_num = lambda x: x * x

# Call the lambda just like a regular function
result = square_num(5)
print(result)


# Exercise 15. Filter a List Using Lambda and filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter(function, iterable)
even_nums = list(filter(lambda x: x % 2 == 0, numbers))

print(even_nums)


# Exercise 16. Transform a List Using Lambda and map()
numbers = [1, 2, 3, 4, 5]

# map(function, iterable)
doubled_numbers = list(map(lambda x: x * 2, numbers))

print(doubled_numbers)


# Exercise 17. Sort Complex Data with sorted() and Lambda
students = [("Alice", 88), ("Bob", 75), ("Charlie", 92)]

# Sort using the second element (index 1) of each tuple
sorted_students = sorted(students, key=lambda student: student[1])

print(sorted_students)
# Exercise 18. Create a Higher-Order Function
def apply_operation(func, x, y):
    return func(x, y)

# Define simple operations
def add(a, b): return a + b
def multiply(a, b): return a * b

# Use the higher-order function
res_add = apply_operation(add, 5, 3)
res_mult = apply_operation(multiply, 5, 3)

print("Addition Result:", res_add)
print("Multiplication Result:", res_mult)