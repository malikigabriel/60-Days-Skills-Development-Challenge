# Day 2: Lists, Tuples, Dictionaries

# ---- LISTS (mutable, ordered) ----
# Store multiple IP addresses
ip_list = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]
print(f"IPs: {ip_list}")

# Add a new IP
ip_list.append("8.8.8.8")
#print(f"After adding: {ip_list}")

# Loop through list
for ip in ip_list:
    if ip.startswith("192"):
        print(f"{ip} is private")



# ---- TUPLES (immutable, ordered) ----
# Good for fixed data like credentials or config
credentials = ("admin", "Sup3rS3cr3t!")
print(f"Username: {credentials[0]}")

# ---- DICTIONARIES (key-value pairs) ----
# Perfect for log entries or asset tracking
log_entry = {
    "timestamp": "2025-06-03 10:30:00",
    "source_ip": "203.0.113.5",
    "event_type": "failed_login",
    "user": "gmaliki"
}
print(f"Event: {log_entry['event_type']} from {log_entry['source_ip']}")