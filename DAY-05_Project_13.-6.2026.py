# Project 1: Login Report Generator
def login_report(successful, failed):
    print("Login Report:")
    print("Successful Logins:", successful)
    print("Failed Logins:", failed)
# Example usage of the function
login_report(150, 25)


# Project 2_Network Device Inventory_Use dictionaries.
def device_inventory():
    inventory = {
        "Router": 5,
        "Switch": 10,
        "Firewall": 3,
        "Access Point": 7
    }
    return inventory

# Example usage of the function
print(device_inventory())


# Project 3: Network Performance Metrics_Calculate average latency and packet loss.
def network_devices():
    devices = {
        "Server01": {
            "hostname": "Server01",
            "ip": "192.168.1.10",
            "status": "Online"
        }
    }
    return devices

# Example usage of the function
print(network_devices())


# Day 5: Functions - Reusable blocks of code

#-1 ---- BASIC FUNCTION (no parameters, no return) ----
def print_banner():
    print("=" * 50)
    print("SECURITY SCAN TOOL")
    print("=" * 50)

# Call the function
print_banner()


#-2 ---- FUNCTION WITH PARAMETERS ----
def check_port(ip, port):
    """Simulate checking if a port is open"""
    print(f"Checking {ip}:{port}...")
    # In real life, you'd use socket.connect_ex()
    if port in [22, 80, 443]:
        return "OPEN"
    else:
        return "CLOSED"
# Example usage
result = check_port("192.168.1.10", 80)
print(result)


#-3 Call with arguments
result = check_port("192.168.1.1", 22)
print(f"Result: {result}")

# ---- FUNCTION WITH RETURN VALUE ----
def calculate_risk_score(failed_logins, is_external_ip):
    """Calculate risk score based on failed logins"""
    score = failed_logins * 10
    if is_external_ip:
        score = score * 2
    return score

risk = calculate_risk_score(5, True)
print(f"Risk score: {risk}")