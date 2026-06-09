# package delivery cost based on location and total amount

total = int(input("Enter the amount for the item: "))
state = input("Enter the state name in USA: ")

if state == "Texas":
    if total <= 150:
        print("Shipping Cost in Texas is $30")
    elif total > 150 and total <= 250:
        print("Shipping Cost in Texas is $20")
    else:
        print("Shipping Cost in Texas is $5")

elif state == "Florida":
    if total <= 150:
        print("Shipping Cost in Florida is $45")
    elif total > 150 and total <= 250:
        print("Shipping Cost in Florida is $35")
    else:
        print("Shipping Cost in Florida is $10")

elif state == "Virginia":
    if total <= 150:
        print("Shipping Cost in Virginia is $23")
    elif total > 150 and total <= 250:
        print("Shipping Cost in Virginia is $15")
    else:
        print("Shipping Cost in Virginia is $5")

elif state == "New Jersey":
    if total <= 150:
        print("Shipping Cost in New Jersey is $40")
    elif total > 150 and total <= 250:
        print("Shipping Cost in New Jersey is $10")
    else:
        print("Shipping Cost is FREE")

else:
    print("Invalid State name")