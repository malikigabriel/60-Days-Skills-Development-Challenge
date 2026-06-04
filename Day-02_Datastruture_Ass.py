# 1. Create a list of 5 open ports
open_ports = [22, 80, 443, 3306, 8080]
print(open_ports)


# 2. Create a dictionary for a server: name, IP, OS, status
server = {
    "name": "WebServer01",
    "IP": "192.168.1.10",
    "OS": "Ubuntu 22.04",
    "status": "Online"
}
print(server)


# 3. Loop through the dictionary and print each key-value pair
#You can loop through the dictionary using the .items() method:
server = {
    "name": "WebServer01",
    "IP": "192.168.1.10",
    "OS": "Ubuntu 22.04",
    "status": "Online"
}

for key, value in server.items():
    print(f"{key}: {value}")


#Write a script that stores 3 failed login attempts (as dictionaries in a list), 
#then loops through and prints each one.
failed_logins = [
    {
        "username": "alice",
        "ip": "192.168.1.10",
        "time": "2026-06-04 09:15:00"
    },
    {
        "username": "bob",
        "ip": "192.168.1.15",
        "time": "2026-06-04 09:20:00"
    },
    {
        "username": "charlie",
        "ip": "192.168.1.20",
        "time": "2026-06-04 09:25:00"
    }
]

for attempt in failed_logins:
    print("Failed Login Attempt")
    for key, value in attempt.items():
        print(f"{key}: {value}")
    print("-" * 20)