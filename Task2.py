# Zenith Crest Bank

from datetime import datetime, date

# Welcome the customer  with a greeting
print("Welcome to Zenith Crest Bank. \nPlease proceed with your registration \n")

# Get User details
First_Name = input("Enter First Name: ")
Last_Name = input("Enter Last Name: ")
Midddle_Name = input("Enter Middle Name: ")
Full_Name = (First_Name + Last_Name + Midddle_Name)

Address = input("Enter your address: ")

# Ask the customer for their D.O.B  to determine if they can register
print("Your date of birth (dd mm yyyy): ")
date_of_birth = datetime.strptime(input("--->"), "%d %m %Y")

# Calculate the customer's age
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

Age = calculate_age(date_of_birth)

# Set the Age condition for registration
if (Age < 18):
    print("You are Underage. Please use the I.D of a parent or guardian.")
    input("Enter unique ID:")

# Get more details from the customer if they meet the age requirmenet

Phone_Number = input("Enter your Phone number: ")
Deposit_Amount = int(input("Amount to Deposit: "))

# Set a condition for Deposits  so that a deposit less than 1000 prints an error
if Deposit_Amount < 1000:
    print("Deposit below minimum")
    Deposit_Amount = int(input("Amount to Deposit: "))

# Assign a current balance for a new customer
Cur_Balance = 0

# Set the equation for calculatng the customer's main blance
Main_Balance = (Cur_Balance + Deposit_Amount)

# Assign a promo code
Promo = "ABCDE"

# Ask the customer  if they have a promo code
print("Do You have a Promo Code?: ")
Promo_Question = input("(Y) or (N): ")

# A condition for the promo code answer where having the correct code grants a bonus of 500
if Promo_Question.upper() == "Y":
    Promo_Code = input("Promo Code: ")
    if Promo_Code.upper() == Promo:
        Bonus = 500
        Main_Balance = (Cur_Balance + Deposit_Amount + Bonus)
        print("New Customer Bonus: 500")
    else:
        print("Incorrect Promo Code")
        print("Do You have a Promo Code?: ")
        Promo_Question = input("(Y) or (N): ")
else:
    print("Registration Complete.")

# Print out custiomer details
print("Customer Name:", "%s, %s %s" % (Last_Name.upper(), First_Name.capitalize(), Midddle_Name[0]))
print("Phone Number:", Phone_Number)
print("Address:", Address)
print("Account Balance:", Main_Balance)