#age = int(input("Enter your age: "))

#if age >= 18:
    #print("Adult")
#else:
    #print("Minor")


# Cybersecurity Login Simulator in Python that checks a username and password and grants or denies access.
# Cybersecurity Login Simulator

# Stored credentials
#correct_username = "admin"
#correct_password = "SecurePass123"

# User input
#username = input("Enter username: ")
#password = input("Enter password: ")

# Check credentials
#if username == correct_username and password == correct_password:
    #print("Access Granted")
#else:
    #print("Access Denied")


# Cybersecurity Login Simulator in Python that checks a username and password and grants or denies access.
# # Cybersecurity Login Simulator with 3 Attempts

#correct_username = "admin"
#correct_password = "SecurePass123"

#max_attempts = 3

#for attempt in range(max_attempts):
    #username = input("Username: ")
    #password = input("Password: ")

    #if username == correct_username and password == correct_password:
        #print("Access Granted")
        #break
    #else:
        #remaining = max_attempts - attempt - 1
        #print(f"Access Denied. Attempts remaining: {remaining}")

#else:
    #print("Account Locked")


# simple Python Password Strength Checker based on the rules you provided:
password = input("Enter a password: ")

length = len(password)

if length < 8:
    print("Password Strength: Weak")
elif 8 <= length <= 11:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")