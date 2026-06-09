# Day 4: Conditionals - if, elif, else

# ---- BASIC IF STATEMENT ----
severity = "high"

if severity == "high":
    print("Alert: Page the on-call engineer")

# ---- IF-ELSE ----
port = 22

if port == 22:
    print("SSH port - allow")
else:
    print("Other port - investigate")


# ---- IF-ELIF-ELSE (Multiple conditions) ----
http_status = 404

if http_status == 200:
    print("OK - normal traffic")
elif http_status == 404:
    print("Not found - check if directory brute force")
elif http_status == 403:
    print("Forbidden - possible permission issue")
elif http_status == 500:
    print("Internal server error - investigate")
else:
    print(f"Status {http_status} - log for review")


# ---- COMBINING CONDITIONS (and / or) ----
source_ip = "203.0.113.5"
attempt_count = 5

if source_ip == "203.0.113.5" or attempt_count > 3:
    print("Suspicious: Known bad IP or too many attempts")

if attempt_count > 3 and source_ip != "192.168.1.1":
    print("BLOCK: High attempts from non-internal IP")

# ---- NESTED CONDITIONALS ----
user_role = "analyst"
resource = "logs"

if user_role == "admin":
    print("Full access")
else:
    if resource == "logs":
        print("Read-only access to logs")
    else:
        print("Access denied")