# 1. Write code that checks if a number is positive, negative, or zero
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# 2. Write code that checks if a port number is well-known (1-1023), 
#    registered (1024-49151), or dynamic (49152-65535)
port = int(input("Enter a port number: "))

if 1 <= port <= 1023:
    print("The port is well-known.")
elif 1024 <= port <= 49151:
    print("The port is registered.")
elif 49152 <= port <= 65535:
    print("The port is dynamic.")
else:
    print("The port is not valid.")


# 3. Write code that takes a log level (INFO, WARNING, ERROR, CRITICAL) 
#    and prints a different response for each
log_level = input("Enter a log level (INFO, WARNING, ERROR, CRITICAL): ").upper()

if log_level == "INFO":
    print("This is an informational message.")
elif log_level == "WARNING":
    print("This is a warning message.")
elif log_level == "ERROR":
    print("This is an error message.")
elif log_level == "CRITICAL":
    print("This is a critical message.")
else:
    print("Invalid log level.")
    

# Build a simple firewall rule checker:
# 4. Write code that checks if a given IP address is in a specific subnet (e.g., 192.168.1.0/24)
ip_address = input("Enter an IP address: ")
subnet = input("Enter a subnet (e.g., 192.168.1.0/24): ")

# Simple implementation - in a real-world scenario, you would use a more 
# robust IP handling library
ip_parts = ip_address.split(".")
subnet_parts = subnet.split("/")[0].split(".")

if ip_parts[:3] == subnet_parts[:3]:
    print("The IP address is in the subnet.")
else:
    print("The IP address is not in the subnet.")

# Ask user for source IP, destination port, and protocol (TCP/UDP)
source_ip = input("Enter source IP address: ")
destination_port = int(input("Enter destination port: "))
protocol = input("Enter protocol (TCP/UDP): ").upper()
# Check if the source IP is in a specific subnet
if source_ip.startswith("192.168.1."):
    print("Source IP is in the subnet.")
else:    print("Source IP is not in the subnet.")
# Check if the destination port is a well-known port
if 1 <= destination_port <= 1023:
    print("Destination port is a well-known port.")
else:
    print("Destination port is not a well-known port.")
# Check if the protocol is TCP or UDP
if protocol == "TCP":
    print("Protocol is TCP.")
elif protocol == "UDP":
    print("Protocol is UDP.")
else:
    print("Invalid protocol.")


# Use conditionals to decide if traffic is ALLOW or BLOCK   
if source_ip.startswith("192.168.1.") and 1 <= destination_port <= 1023 and protocol == "TCP":
    print("Traffic is ALLOWED.")
else:
    print("Traffic is BLOCKED.")


# Rules: BLOCK port 23 (Telnet), BLOCK port 445 (SMB) from external IPs,
#        ALLOW everything else
if destination_port == 23:
    print("Traffic is BLOCKED (Telnet).")
elif destination_port == 445:
    print("Traffic is BLOCKED (SMB).")
else:
    print("Traffic is ALLOWED.")
    