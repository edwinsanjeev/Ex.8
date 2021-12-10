# Programmer: Edwin
# Date: 12/07/2021
# Description: Exercise 08
from sys import *

grade = int(input("What is your percent grade? "))
if grade < 0:
    print("Invalid percent!", file=stderr)
    exit()
print()

if grade > 100:
    print("Invalid percent!")
elif grade >= 95:
    print("Your level grade is 4+.")
elif grade >= 87:
    print("Your level grade is 4.")
elif grade >= 80:
    print("Your level grade is 4-.")
elif grade >= 77: 
    print("Your level grade is 3+.")
elif grade >= 73:
    print("Your level grade is 3.")
elif grade >=  70:
    print("Your level grade is 3-.")
elif grade >= 67:
    print("Your level grade is 2+.")
elif grade >= 63:
    print("Your level grade is 2.")
elif grade >= 60:
    print("Your level grade is 2-.")
elif grade >= 57:
    print("Your level grade is 1+.")
elif grade >= 53:
    print("Your level grade is 1.")
elif grade >= 50:
    print("Your level grade is 1-.")
elif grade < 50:
    print("Your level grade is R.")

