# File: DaysInMonth.py
# Student: Michel Gonzalez
# UT EID: Mag9989
# Course Name: CS303E
# 
# Date Created: 02/12/2021
# Date Last Modified: 02/12/2021
# Description of Program: The purpose of this program is to indicate the days of a month in a desired year, assuming the year is a four digit number.

month = int(input("Enter a Month number: "))

year = int(input("Enter a Year: "))

#Checking if the year is a leap year
if ((year % 400 == 0) and not (year % 100 == 0) or (year % 4 == 0)):

    if (month == 2):
        print( "Februray", year, "has 29 days")

    else:
        #This lets other months print if the month entered is not febuary but the year is a leap year 
        if (month == 1):
            print("January", year, "has 31 days")

        elif (month == 3):
            print("March", year, "has 31 days")

        elif (month == 4):
            print("April", year, "has 30 days")

        elif (month == 5):
            print("May", year, "has 31 days")

        elif (month == 6):
            print("June", year, "has 30 days")
    
        elif (month == 7):
            print("July", year, "has 31 days")

        elif (month == 8):

            print("August", year, "has 31 days")

        elif (month == 9):
            print("September", year, "has 30 days")

        elif (month == 10):
            print("October", year, "has 31 days")

        elif (month == 11):
            print("November", year, "has 30 days")

        elif (month == 12):
            print("December", year, "has 31 days")

        #Checks for incorrect numbers entered for the month
        elif (month < 1 or  month > 12):
            print("Invalid month number entered")
else:
    #This is for non-leap years
    if (month == 1):
        print("January", year, "has 31 days")

    elif (month == 2):
        print("February", year, "has 28 days")

    elif (month == 3):
        print("March", year, "has 31 days")

    elif (month == 4):
        print("April", year, "has 30 days")

    elif (month == 5):
        print("May", year, "has 31 days")

    elif (month == 6):
        print("June", year, "has 30 days")
    
    elif (month == 7):
        print("July", year, "has 31 days")

    elif (month == 8):
        print("August", year, "has 31 days")

    elif (month == 9):
        print("September", year, "has 30 days")

    elif (month == 10):
        print("October", year, "has 31 days")

    elif (month == 11):
        print("November", year, "has 30 days")

    elif (month == 12):
        print("December", year, "has 31 days")

    #Checks for incorrect numbers entered for the month
    elif (month < 1 or  month > 12):
        print("Invalid month number entered")
    

    
            
