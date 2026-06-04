# Define a tuple and print it
#my_tuple = (1, 3.0, "John")
#print(my_tuple)


# Create a tuple with names
#names = ("James", "Jhon", "Elizabeth")
# Try to append a name
#names.append("Liza")


#names = ("Alice", "Bob", "Charlie")
#names = names + ("David",)
#print(names)


# Create a tuple in a range
#my_tuple = tuple(range(1, 10))
#print(my_tuple)


# Dictionaries: A dictionary is a way to store data that are coupled as keys and values. 
# This is how we can create one:
# # Create a dictionary
#my_dictionary = {'key_1':'value_1', 'key_2':'value_2'}


# Dictionaries manipulation: 
# Both keys and values of a dictionary can be of any type: strings, 
# integers, or floats. So, for example, we can create a dictionary like so:
# Create a dictionary of numbers and print it
#numbers = {1:'one', 2:'two', 3:'three'}
#print(numbers)


# Create a dictionary of numbers and print it
numbers = {'one':1, 'two':2.0, 3:'three'}
#print(numbers)


# Access values and keys
keys = list(numbers.keys())
values = tuple(numbers.values())
# Print values and keys
print(f"The keys are: {keys}")
print(f"The values are: {values}")


# Create a shopping list with fruits and prices
shopping_list = {'banana':2, 'apple':1, 'orange':1.5}
# Iterate over the values
for values in shopping_list.values():
    # Values greater than threshold
    if values > 1:
        print(values)


# Create the dictionary
person = {'name': 'John', 'age': 30}
# Add value and key and print
person['city'] = 'New York'
print(person)


# Create a dictionary
person = {'name': 'John', 'age': 30}
# Change age value and print
person['age'] = 35
print(person)


#Nested dictionaries:
# We have seen before that we can create lists of lists and tuples of tuples. 
# Similarly, we can create nested dictionaries. Suppose, for example, 
# we want to create a dictionary to store the data related 
# to a class of students. We can do it like so:

# Create a classroom dictionary
classroom = {
    'student_1': {
        'name': 'Alice',
        'age': 15,
        'grades': [90, 85, 92]
    },
    'student_2': {
        'name': 'Bob',
        'age': 16,
        'grades': [80, 75, 88]
    },
    'student_3': {
        'name': 'Charlie',
        'age': 14,
        'grades': [95, 92, 98]
    } }
    # Access student_3 and print
student_3 = classroom['student_3']
print(student_3)


# Define initial dictionary
products = {'shoes': 100, 'watch': 50, 'smartphone': 250, 'tablet': 120}
# Define threshold
max_price = 150
# Filter for threshold
products_to_buy = {fruit: price for fruit, price in products.items() if price <= max_price}
# Print filtered dictionary
print(products_to_buy)


# Define names and ages in lists
names = ['John', 'Jane', 'Bob', 'Alice']
cities = ['New York', 'Boston', 'London', 'Rome']
# Create dictionary from lists and print results
name_age_dict = {name: city for name, city in zip(names, cities)}
print(name_age_dict)