# Introduction to Variables In Python, variables are used to store data. You do not need to declare a variable 
#with a specific data type like in C#. Python automatically assigns the type based on the value you provide.
#Example:
temperature = 36  # Here, temperature is an integer

#Basic Data Types in Python
#int: Stores whole numbers (e.g., 10, -5, 100)
#float: Stores decimal numbers (e.g., 10.5, -3.14).
#str: Stores text (e.g., "Hello", "World").
#bool: Stores True or False.
#Example:
age = 42  # int
height = 1.75  # float
name = "Gabriel"  # str
is_student = True  # bool

#Declaring and Initializing Variables
##In Python, you can declare and initialize variables simply by assigning a value to them. There is no need to specify the type, as Python infers it from the assigned value.
#Syntax
#variable_name = value
#Example:
age = 42
height = 1.75
name = "Gabriel"
is_student = True

#Adding Numbers and Simple Equations: You can perform arithmetic operations 
#like addition, subtraction, multiplication, and division with numeric variables in Python.
#Example:
# Adding two numbers
num1 = 10
num2 = 20
sum_value = num1 + num2

# Subtraction
difference = num1 - num2

# Multiplication
product = num1 * num2

# Division
quotient = num1 / num2

print("Sum:", sum_value)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

#User Input in Python 
#In Python, you can ask the user for input using the input() function. This always returns a string. If you need to handle numbers, you'll need to convert the input to the appropriate data type, such as int or float.
#Example:
name = input("Enter your name: ")  # input always returns a string
age = int(input("Enter your age: "))  # convert the input to an integer
print("Hello,", name, "you are", age, "years old.")


#Combining Text (String Concatenation) and Printing
#In Python, you can combine strings (concatenation) and 
#print them in several ways. Here are a few examples:
#Example:
first_name = "Gabriel"
last_name = "MALIKI"
full_name = first_name + " " + last_name  # Concatenating strings

print("Full Name:", full_name)

#Example: Using Comma Separation in print()
first_name = "Gabriel"
last_name = "MALIKI" \
""

print("Full Name:", first_name, last_name)  # No need for explicit concatenation

#Example: Using f-strings (Python 3.6+)
first_name = "Gabriel"
last_name = "MALIKI"
age = 42

print(f"Full Name: {first_name} {last_name}, Age: {age}")


#Example: Using the format() Method
first_name = "Gabriel"
last_name = "MALIKI"
age = 42

print("Full Name: {} {}, Age: {}".format(first_name, last_name, age))

#Example: Using % Formatting (Old Method)
first_name = "Gabriel"
last_name = "MALIKI"
age = 42

print("Full Name: %s %s, Age: %d" % (first_name, last_name, age))