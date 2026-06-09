# Project 1: Password Attempt Tracker Requirements: Allow 3 login attempts,
#  Lock the account after 3 failures 
# Display remaining attempts
# Example
##correct_password = "admin123"
#max_attempts = 3
#attempts = 0

#while attempts < max_attempts:
    #password = input("Enter password: ")

    #if password == correct_password:
        #print("Login successful!")
        #break
    #else:
       # attempts += 1
        #remaining = max_attempts - attempts

        #if remaining > 0:
            #print(f"Incorrect password. {remaining} attempt(s) remaining.")
        #else:
            #print("Account locked. Too many failed login attempts.")


#Project 2: Security Event Counter: Create a list such as: 
#["login", "login", "logout", "login", "failed_login", "failed_login"]
#Count:
#1. Total logins
#2. Total failed logins
#3. Total logouts

events = [
    "login",
    "login",
    "logout",
    "login",
    "failed_login",
    "failed_login"
]

total_logins = events.count("login")
total_failed_logins = events.count("failed_login")
total_logouts = events.count("logout")

print("Security Event Summary")
print(f"Total logins: {total_logins}")
print(f"Total failed logins: {total_failed_logins}")
print(f"Total logouts: {total_logouts}")