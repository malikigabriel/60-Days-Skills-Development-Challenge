# Day 1: Variables, Data Types, Basic Math
# 1. Create variables
name = "Gabriel"
age = 42
height = 5.9
cert_count = 16
aws_score = 838

# 2. Print variables
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Certifications earned: {cert_count}")
print(f"AWS exam score: {aws_score}")

# 3. Basic math
total_study_hours = 300
days_studied = 60
avg_hours_per_day = total_study_hours / days_studied
print(f"Average hours per day: {avg_hours_per_day}")

# 4. Simple IP check (security relevant)
ip = "232.68.1.1"
octets = ip.split(".")
print(f"IP octets: {octets}")

if octets[0] == "192" and octets[1] == "168":
    print(f"{ip} is a private IP address")
else:
    print(f"{ip} is a public IP address")

    # 5. calculate simple interest (finance relevant)
principal = 7000
rate = 7.5
time = 5
simple_interest = (principal * rate * time) / 100
print(f"Simple Interest: ${simple_interest}")


