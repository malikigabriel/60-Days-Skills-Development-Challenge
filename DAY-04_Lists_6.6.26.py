#CREATE A LISTS
list1 = ['apple', 'orange', 'banana', 'kiwi']
print(list1)

# CREATYE LIST2
list2 = ['apple', [8, 4, 6], 'banana', 'kiwi']
print(list2)

print(list1[0]) # apple
print(list1[1]) # orange    
print(list1[2]) # banana
print(list1[3]) # kiwi  
print(list2[0]) # apple
print(list2[1]) # [8, 4, 6]
print(list2[2]) # banana
print(list2[3]) # kiwi
print(list2[1][0]) # 8
print(list2[1][1]) # 4
print(list2[1][2]) # 6    
print(list2[1][0:2]) # [8, 4]
print(list1[0:2]) # ['apple', 'orange']
print(list1[1:3]) # ['orange', 'banana']
print(list1[0:4]) # ['apple', 'orange', 'banana', 'kiwi']
print(list1[:]) # ['apple', 'orange', 'banana', 'kiwi']
print(list1[-1]) # 'kiwi'
print(list1[-2]) # 'banana'
print(list1[-3]) # 'orange'
print(list1[-4]) # 'apple'

# HOW TO ADD ELEMENTS TO A LIST
list1.append('grape')
print(list1)

list1.insert(1, 'melon')
print(list1)    
list1.insert(3, 'pear')
print(list1)
list1.insert(5, 'peach')
print(list1)
list1.extend(['strawberry', 'blueberry'])
print(list1)
list1 += ['watermelon', 'pineapple']
print(list1)

# HOW TO REMOVE ELEMENTS FROM A LIST
list1.remove('grape')
print(list1)
list1.pop(1)
print(list1)
list1.pop()
print(list1)
del list1[2]
print(list1)
list2.clear()
print(list1)
list1.reverse()
print(list1)
print(list1.count('apple'))
print(list1.index('orange'))


#Looping through lists
names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(name)


#Example 2: Loop Through IP Addresses
ip_addresses = [
    "192.168.1.10",
    "10.0.0.5",
    "172.16.0.1"
]

for ip in ip_addresses:
    print(ip)


#Example 3: Loop with Index
#Use enumerate() if you want the position of each item:
events = ["login", "logout", "failed_login"]

for index, event in enumerate(events):
    print(index, event)


#Example 4: Using a While Loop
names = ["Alice", "Bob", "Charlie"]

i = 0
while i < len(names):
    print(names[i])
    i += 1



#SOC Analyst Example
failed_ips = [
    "192.168.1.10",
    "10.0.0.5",
    "172.16.0.1"
]

for ip in failed_ips:
    print(f"Failed login detected from: {ip}")


# Create list and print it
my_list = list((1, 2, 3, 4, 5))
print(my_list)

# Create a list in a range
my_list = list(range(1, 10))
print(my_list)

# List of names
names = ["James", "Richard", "Simon", "Elizabeth", "Tricia"]
# Change the wrong name
names[0] = "Alexander"
# Print list
print(names)

# List of names Now, suppose we’ve forgotten a name. We can add it to our list like so:
names = ["James", "Richard", "Simon", "Elizabeth", "Tricia"]
# Append another name
names.append("Alexander")
# Print list
print(names) 

# Create list1 : If we need to concatenate two lists, 
# we have two possibilities: the concatenate method or the extend()one. Let’s see them:
list1 = [1, 2, 3]
# Create list2
list2 = [4, 5, 6]
# Concatenate lists
concatenated_list = list1 + list2
# Print concatenated list
print(concatenated_list)

# Create list1 : So, this method creates a list that 
# is the sum of other lists. Let’s see the extend() method:
list1 = [1, 2, 3]
# Create list2
list2 = [4, 5, 6]
# Extend list1 with list2
list1.extend(list2)
# Print new list1
print(list1)

# Create list: If we want to remove elements, we have two possibilities: 
# we can use the remove() method or del. Let’s see them:
my_list = [1, 2, 3, 'four', 5.0]
# Remove one element and print
my_list.remove('four')
print(my_list)

# Create list
my_list = [1, 2, 3, 'four', 5.0]
# Delete one element and print
del my_list[3]
print(my_list)

# Create shopping list: Suppose we have a shopping list. We want our program to print that 
# we love one fruit and that we don’t like the others on the list. Here’s how we can do so:
shopping_list = ["banana", "apple", "orange", "lemon"]
# Print the one I like
for fruit in shopping_list:
    if fruit == "lemon":
        print(f"I love {fruit}")
    else:
        print(f"I don't like {fruit}")

# Create list: Another example could be the following. Suppose we have a list 
# of numbers and we want to print just the even ones. Here’s how we can do so:
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

# Create listFor example, to create a list with 
# even numbers we can use list comprehension like so:
numbers = [1,2,3,4,5,6,7,8]
# Create list of even numbers
even_numbers = [even for even in numbers if even %2 == 0]
# Print even list
print(even_numbers)

# Create shipping list: Now, let’s create a list with comments on the fruit I love 
# (and the fruit I don’t) with list comprehension:
shopping_list = ["banana", "apple", "orange", "lemon"]
# Create commented list and print it
commented_list = [f"I love {fruit}" if fruit == "banana"
                  else f"I don't like {fruit}"
                  for fruit in shopping_list]
print(commented_list)

# Create lis with students and their grades
students = [
    ["John", [85, 92, 78, 90]],
    ["Emily", [77, 80, 85, 88]],
    ["Michael", [90, 92, 88, 94]],
    ["Sophia", [85, 90, 92, 87]]
]
# Iterate over the list
for student in students:
    name = student[0] # Access names
    grades = student[1] # Access grades
    average_grade = sum(grades) / len(grades) # Calculate mean grades
    print(f"{name}'s average grade is {average_grade:.2f}")