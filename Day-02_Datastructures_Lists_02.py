# In Python, a list is a collection of ordered elements 
# that can be of any type: strings, integers, floats, etc…
# Example:
# Create list of integers
my_integers = [1, 2, 3, 4, 5, 6]
# print(my_integers)

# Create a mixed list
mixed_list = [1, 3, "dad", 101, "apple"]
# print(mixed_list)

# To create a list, we can also use the Python
# built-in function list(). This is how we can use it: Example:
# Create list and print it
my_list = list((1, 2, 3, 4, 5))
# print(my_list)

# Create a list in a range
my_list = list(range(1, 10))
print(my_list)

# Lists manipulation
# For example, let’s say we have a list of names, 
# but we made a mistake and we want to change one. Here’s how we can do so:
# List of names
names = ["James", "Richard", "Simon", "Elizabeth", "Tricia"]
# Change the wrong name
names[0] = "Alexander"
# Print list
print(names)

# Now, suppose we’ve forgotten a name. We can add it to our list like so:
# List of names
names = ["James", "Richard", "Simon", "Elizabeth", "Tricia"]
# Append another name
names.append("Alexander")
# Print list
print(names) 

# If we need to concatenate two lists, we have two possibilities: 
# the concatenate method or the extend()one. Let’s see them:
# Create list1
list1 = [1, 2, 3]
# Create list2
list2 = [4, 5, 6]
# Concatenate lists
concatenated_list = list1 + list2
# Print concatenated list
print(concatenated_list)

# So, this method creates a list that is the sum of other lists. 
# Let’s see the extend() method:
# Create list1
list1 = [1, 2, 3]
# Create list2
list2 = [4, 5, 6]
# Extend list1 with list2
list1.extend(list2)
# Print new list1
print(list1)

# If we want to remove elements, we have two possibilities: 
# we can use the remove() method or del. Let’s see them:
# Create list
my_list = [1, 2, 3, 'four', 5.0]
# Remove one element and print
my_list.remove('four')
print(my_list)

# Let’s see the other method:
# Create list
my_list = [1, 2, 3, 'four', 5.0]
# Delete one element and print
del my_list[3]
print(my_list)

#List comprehension
#Suppose we have a shopping list. We want our program to print 
# that we love one fruit and that we don’t like the others on the list. Here’s how we can do so:
# Create shopping list
shopping_list = ["banana", "apple", "orange", "lemon"]
# Print the one I like
for fruit in shopping_list:
    if fruit == "lemon":
        print(f"I love {fruit}")
    else:
        print(f"I don't like {fruit}")


# Another example could be the following. 
# Suppose we have a list of numbers and we want to print just the even ones. Here’s how we can do so:
# Create list
numbers = [1,2,3,4,5,6,7,8]
# Create empty list
even_list = []
# Print even numbers
for even in numbers:
    if even %2 == 0:
        even_list.append(even)
    else:
        pass

print(even_list)

# Create list
numbers = [1,2,3,4,5,6,7,8]
# Create list of even numbers
even_numbers = [even for even in numbers if even %2 == 0]
# Print even list
print(even_numbers)

# Now, let’s create a list with comments on the fruit I love 
# (and the fruit I don’t) with list comprehension:
# Create shipping list
shopping_list = ["banana", "apple", "orange", "lemon"]
# Create commented list and print it
commented_list = [f"I love {fruit}" if fruit == "banana"
                  else f"I don't like {fruit}"
                  for fruit in shopping_list]
print(commented_list)

#List of lists
# There is also the possibility to create lists of lists, that are lists nested into one list. 
# This possibility is useful when we want to represent listed data as a unique list.
# Create list with students and their grades
students = [
    ["John", [85, 92, 78, 90]],
    ["Emily", [77, 80, 85, 88]],
    ["Michael", [90, 92, 88, 94]],
    ["Sophia", [85, 90, 92, 87]]
]

#This is a useful notation if, for example, 
# we want to calculate the mean grade for each student. We can do it like so:
# Iterate over the list
for student in students:
    name = student[0] # Access names
    grades = student[1] # Access grades
    average_grade = sum(grades) / len(grades) # Calculate mean grades
    print(f"{name}'s average grade is {average_grade:.2f}")