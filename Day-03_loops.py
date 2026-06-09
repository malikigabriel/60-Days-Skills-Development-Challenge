# Day 3: FOR loops and WHILE loops

# ---- FOR LOOPS (iterate through sequences) ----

# Loop through a list of IPs
#ip_addresses = ["192.168.1.1", "10.0.0.1", "8.8.8.8", "1.1.1.1"]
#for ip in ip_addresses:
    #if ip.startswith("192") or ip.startswith("10"):
        #print(f"{ip} -> Private IP")
    #else:
        #print(f"{ip} -> Public IP")

# Loop through a range of numbers (ports 1-10)
#print("\nScanning ports 1-10:")
#for port in range(1, 11):
   #print(f"Checking port {port}")

# Loop through dictionary items
#failed_logins = [
   # {"user": "admin", "ip": "203.0.113.5", "count": 3},
    #{"user": "gabriel", "ip": "198.51.100.2", "count": 1},
    #{"user": "root", "ip": "203.0.113.5", "count": 7}
#]

#print("\nSuspicious activity:")
#for attempt in failed_logins:
   # if attempt["count"] > 5:
       # print(f"ALERT: {attempt['user']} from {attempt['ip']} has {attempt['count']} failures")

# ---- WHILE LOOPS (continue until condition changes) ----

# Countdown timer
#print("\nCountdown:")
#seconds = 5
#while seconds > 0:
    #print(f"T-minus {seconds}")
    #seconds -= 1
#print("Launch!")

# Keep asking until valid input (useful for security tools)
#user_input = ""
#while user_input.lower() != "quit":
    #user_input = input("Enter 'quit' to exit: ")
    #print(f"You entered: {user_input}")


# ---- PRACTICE TASKS ----
# 1. Use a for loop to print only ports that are even numbers (2,4,6...20)
for port in range(2, 21, 2):
    print(f"Checking port {port}")

# 2.
print("\nCountdown")


# 2. Use a while loop to count from 10 down to 1, then print "Scan complete"
seconds = 10
while seconds > 0:
    print(f"T-minus {seconds}")
    seconds -= 1        
print("Scan complete")


# 3. Create a list of 5 suspicious IPs, loop through and print each with "ALERT:" in front
suspicious_ips = ["203.0.113.5", "198.51.100.2", "203.0.113.5", "192.168.1.1", "10.0.0.1"]
print("\nSuspicious IPs:")
for ip in suspicious_ips:
    print(f"ALERT: {ip}")
        

# Write a script that asks the user for an IP address, then uses a while loop to let them keep entering IPs until they type "done". 
#Store all IPs in a list, then use a for loop to print them all at the end.
ip_addresses = []

while True:
    ip = input("Enter an IP address (or type 'done' to finish): ")

    if ip.lower() == "done":
        break

    ip_addresses.append(ip)

print("\nIP Addresses Entered:")

for ip in ip_addresses:
    print(ip)