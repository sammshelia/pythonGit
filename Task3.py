# Zenith Crest Academy

# Welcome the student
print("Welcome to Zenith Crest Academy. \nPlease proceed with Grading: \n")

# Get student details
First_Name = input("Enter First Name: ")
Last_Name = input("Enter Last Name: ")

print("Welcome,", First_Name, "\n")

Courses = ["Database", "Intro to Programming", "Object Oriented Programming", "Web Programming"]

# Print out their list of offered courses
print("Courses:", Courses, "\n")

# Request grades from student
print("Enter grades obtained in course subjects:")

# Course 1 input and grade calculation
Database = int(input("Database: "))

if (Database >= 70):
    Grade = "A"
    print("Grade: ", Grade)
elif (Database >= 60 and Database <= 79):
    Grade = "B"
    print("Grade: ", Grade)
elif (Database >= 50 and Database <= 59):
    Grade = "C"
    print("Grade: ", Grade)
    print("You Qualify to take the next course")
elif (Database >= 40 and Database <= 49):
    Grade = "D"
    print("Grade: ", Grade)
elif (Database < 40):
    Grade = "F"
    print("Grade: ", Grade, "DO BETTER!")
else:
    print("Unusual Grade")


# Course 2 input and grade calculation
Intro_to_Programming = int(input("Intro to Programming: "))

if (Intro_to_Programming >= 70):
    Grade = "A"
    print("Grade: ", Grade)
elif (Intro_to_Programming >= 60 and Intro_to_Programming <= 79):
    Grade = "B"
    print("Grade: ", Grade)
elif (Intro_to_Programming >= 50 and Intro_to_Programming <= 59):
    Grade = "C"
    print("Grade: ", Grade)
    print("You Qualify to take the next course")
elif (Intro_to_Programming >= 40 and Intro_to_Programming <= 49):
    Grade = "D"
    print("Grade: ", Grade)
elif (Intro_to_Programming < 40):
    Grade = "F"
    print("Grade: ", Grade, "DO BETTER!")
else:
    print("Unusual Grade")


# Course 3 input and grade calculation
Object_Oriented_programming = int(input("OOP: "))

if (Object_Oriented_programming >= 70):
    Grade = "A"
    print("Grade: ", Grade)
elif (Object_Oriented_programming >= 60 and Object_Oriented_programming <= 79):
    Grade = "B"
    print("Grade: ", Grade)
elif (Object_Oriented_programming >= 50 and Object_Oriented_programming <= 59):
    Grade = "C"
    print("Grade: ", Grade)
    print("You Qualify to take the next course")
elif (Object_Oriented_programming >= 40 and Object_Oriented_programming <= 49):
    Grade = "D"
    print("Grade: ", Grade)
elif (Object_Oriented_programming < 40):
    Grade = "F"
    print("Grade: ", Grade, "DO BETTER!")
else:
    print("Unusual Grade")


# Course 4 input and grade calculation
Web_Programming = int(input("Web Programming: "))

if (Web_Programming >= 70):
    Grade = "A"
    print("Grade: ", Grade)
elif (Web_Programming >= 60 and Web_Programming <= 79):
    Grade = "B"
    print("Grade: ", Grade)
elif (Web_Programming >= 50 and Web_Programming <= 59):
    Grade = "C"
    print("Grade: ", Grade)
    print("You Qualify to take the next course")
elif (Web_Programming >= 40 and Web_Programming <= 49):
    Grade = "D"
    print("Grade: ", Grade)
elif (Web_Programming < 40):
    Grade = "F"
    print("Grade: ", Grade, "DO BETTER!")
else:
    print("Unusual Grade")

sum = Database + Intro_to_Programming + Object_Oriented_programming + Web_Programming
Average = sum/4

if (Average <=  30):
    print("Average: ", Average)
    print("You are adviced to retake this assessment")

if (Average >= 70):
    Grade = "A"
    print("Grade Average:", Average, Grade)
elif (Average >= 60 and Average <= 79):
    Grade = "B"
    print("Grade Average:", Average, Grade)
elif (Average >= 50 and Average <= 59):
    Grade = "C"
    print("Grade Average:", Average, Grade)
    print("You Qualify to take the next course")
elif (Average >= 40 and Average <= 49):
    Grade = "D"
    print("Grade Average:", Average, Grade)
elif (Average < 40):
    Grade = "F"
    print("Grade Average:", Average, Grade, "DO BETTER!")

# Print completion
print("Study harder and see you next semester.")