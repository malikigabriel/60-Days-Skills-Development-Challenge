# Exercise 1. Print first 10 natural numbers using while loop
# Initialize the counter
#i = 1

# Iterate until i is greater than 10
#while i <= 10:
    #print(i)
    # Increment the counter to move to the next number
   # i += 1


#Exercise 2. Display numbers from -10 to -1 using for loop
# Start at -10, stop before 0
#for i in range(-10, 0):
    #print(i)


# Exercise 3. Display a message “Done” after successful execution of for loop
#for i in range(5):
   # print(i)
#else:
    # This block executes only after the loop finishes naturally
    #print("Done!")


# Exercise 4. Calculate the sum of all numbers from 1 to N
# Take input from user and convert to integer
#n = int(input("Enter number: "))

# Variable to store the sum
#s = 0

# Loop from 1 to n (n+1 is used because range is exclusive)
#for i in range(1, n + 1):
    #s += i

#print("Sum is:", s)


# Exercise 4. Print multiplication table of a given number
num = 5

# Iterate 10 times
for i in range(1, 13):
    # Calculate product
    product = num * i
    print(product)


# Exercise 4b. Print multiplication table of a given number
num = int(input("Enter number: "))
for i in range(1, 13):
    product = num * i
    print(num, "*", i, "=", product)