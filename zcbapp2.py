# Task 1.

# Get User details
Firstname = input("Enter First Name: ")
Lastname = input("Enter Last Name: ")
Midddlename = input("Enter Middlename: ")
Phonenumber = input("Enter your  Phone number: ")
Balance = 2500

# Stored Nuban numbers
Nubanaccts = [6032795095, 4646095300, 8884995437, 4004298057, 4045952615]

# Assigning a variable to the Nuban account being assigned
Account_number = Nubanaccts[2]

# Store User details in a list
User_details = [Firstname, Lastname, Midddlename, Balance, Phonenumber]

# Append the assigned Nuban account to user details
User_details.append(Account_number)

# Printing formatted Full name
Full_Name = (Lastname + Firstname + Midddlename)
print("Full Name:", "%s, %s %s" % (Lastname.upper(), Firstname.capitalize(), Midddlename[0]))

# Generating Full name to text document
Detailsfile = open("FullName.txt", "w+")
Detailsfile.write("Full Name: %s, %s %s" % (Lastname.upper(), Firstname.capitalize(), Midddlename[0]))

# Retrieving Phone number, & Nuban number and Account balance
print("Phone Number:", User_details[4])
print("Account Number:", User_details[5])
print("Account Balance:", User_details[3])

# Changing last name of user after marriage
User_details[1] = 'Bwala'

# Deleting the Middle name from the user details
del User_details[2]

# Printing updated User details
print("User Details:", User_details)
