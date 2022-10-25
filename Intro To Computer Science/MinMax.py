# File: MinMax.py
# Student: Michel Gonzalez
# UT EID: Mag9989
# Course Name: CS303E
# 
# Date Created: 02/23/2021
# Date Last Modified: 02/23/2021
# Description of Program: The purpose of this program is to give back the minimum and maximum value entered by the user before the string 'stop' is entered.

value = input("Enter an integer or 'stop' to end: ")

if value != 'stop':
#assigning the integer entered to be both the inital max and min
    maximum = int(value)
    minimum = int(value)
    
    while value != 'stop':
        num1 = int(value)
        value = input("Enter an integer or 'stop' to end: ")

#if user stops program this will return the max and min values from the user input.
        if value == 'stop':
            print("The maximum is", maximum)
            print("The minimum is", minimum)
            break
#checks if the current maximum is lower than the integer entered
        elif int(value) >= num1:
            if maximum < int(value):
                maximum = int(value)
            else:
                continue
#checks if the current minimum is higher than the integer entered
        elif int(value) < num1:
            if minimum > int(value):
                minimum = int(value)
            else:
                continue

else:
    print("You didn't enter any numbers")
