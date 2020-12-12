# OGrill App

from datetime import datetime


Product = [" ", "BBQ Wings", "Mac & Cheese", "Rocky Fries", "Grilled Corn", "Soda"]
Price = [0, 3500, 5500, 2500, 1000, 750]

print("Welcome to OGrill. \nWhat would you like today? \n")

print("MENU: \n1. BBQ Wings \n2. Mac & Cheese \n3. Rocky Fries \n4. Grilled Corn \n5. Soda \n6. Exit")
Customer_Order = int(input("Select an Item: "))

Quantity = int(input("How Many?: "))


if Customer_Order == 1:
    Order_Amount = (Price[1] * Quantity)
    print(Product[1])
    print(Price[1], "x", Quantity)
elif Customer_Order == 2:
    Order_Amount = (Price[2] * Quantity)
    print(Product[2])
    print(Price[2], "x", Quantity)
elif Customer_Order == 3:
    Order_Amount = (Price[3] * Quantity)
    print(Product[3])
    print(Price[3], "x", Quantity)
elif Customer_Order == 4:
    Order_Amount = (Price[4] * Quantity)
    print(Product[4])
    print(Price[4], "x", Quantity)
elif Customer_Order == 5:
    Order_Amount = (Price[5] * Quantity)
    print(Product[5])
    print(Price[5], "x", Quantity)


if (Quantity > 3):
    Delivery = 0.0
elif (Quantity < 3):
    Delivery = 10
elif (Order_Amount > 7000):
    Delivery = 0.0
    print("You Qualify for a Free Drink!")


Total_Order = Order_Amount + Delivery

# Get User details
First_Name = input("Enter First Name: ")
Last_Name = input("Enter Last Name: ")
Phone_Number = input("Enter your  Phone number: ")
Address = input("Enter your address: ")
Customer_Name = (First_Name + Last_Name)

Delivery_date = input("Enter a delivery date in YYYY-MM-DD format: ")
Year, Month, Day = map(int, Delivery_date.split('-'))

print("Customer Name:", "%s %s" % (First_Name.capitalize(), Last_Name.capitalize()))

Order_date = datetime.now()
print("Order Date:", Order_date)

print("Total Order:  ", Total_Order)
print("Delivery:", Delivery)
print("Delivery Date: ", Delivery_date)

Receipt = open("OGrill Receipt.txt", "w+")
Receipt.write("Order Details: \n%s %s \n%s \n%s \n%s \n%s \n%s" % (First_Name.capitalize(), Last_Name.capitalize(), Customer_Order, Quantity, Address, Delivery, Order_date))