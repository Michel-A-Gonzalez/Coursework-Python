# File: Project1.py
# Student: Michel Gonzalez
# UT EID: Mag9989
# Course Name: CS303E
# 
# Date Created: 03-09-2021   
# Date Last Modified: 03-09-2021
# Description of Program: The purpose of this program is to compute the final grade based on the grades
#                         on 3 homworks weighed at 30% of the final grade, 2 exams weighed at 40% of the
#                         final grade, and 2 projects weighed at 30% of the final grade.

print("")

name = input("Enter the student's name: ")

print("")

print("HOMEWORKS")

hw1 = int(input("  Enter HW1 grade: "))

# This will make the user inputs a valid number or the program will not continue #

while (hw1 < 0 or 10 < hw1):
    print("Grade must be in range [0..10]. Try again.")

    hw1 = int(input("  Enter HW1 grade: "))

hw2 = int(input("  Enter HW2 grade: "))

while (hw2 < 0 or 10 < hw2):
    print("Grade must be in range [0..10]. Try again.")

    hw2 = int(input("  Enter HW2 grade: "))

hw3 = int(input("  Enter HW3 grade: "))

while (hw3 < 0 or 10 < hw3):
    print("Grade must be in range [0..10]. Try again.")

    hw3 = int(input("  Enter HW3 grade: "))

print("")

print("PROJECTS:")

proj1 = int(input("  Enter Project1 grade: "))

while (proj1 < 0 or 100 < proj1):
    print("Grade must be in range [0..100]. Try again.")

    proj1 = int(input("  Enter Project1 grade: "))

proj2 = int(input("  Enter Project2 grade: "))

while (proj2 < 0 or 100 < proj2):
    print("Grade must be in range [0..100]. Try again.")

    proj2 = int(input("  Enter Project2 grade: "))

print("")

print("EXAMS:")

ex1 = int(input("Enter Exam1 grade: "))

while(ex1 < 0 or 100 < ex1):
    print("Grade must be in range [0..100]. Try again")

    ex1 = int(input("Enter Exam1 grade: "))

ex2 = int(input("Enter Exam2 grade: "))

while(ex2 < 0 or 100 < ex2):
    print("Grade must be in range [0..100]. Try again")

    ex2 = int(input("Enter Exam2 grade: "))

print("")

print("Grade report for :", name)

# Getting the average values for each catagory and overall course #

hwAvg =((hw1 + hw2 + hw3)/30) * 100  

projAvg = ((proj1 + proj2)/200) * 100

exAvg = ((ex1 + ex2)/200) * 100

courseAvg = (hwAvg * 0.3) + (projAvg * 0.3) + (exAvg * 0.4)

print("  Homework average (30% of grade):", format(hwAvg, "2.2f"))

print("  Project average (30% of grade):", format(projAvg, "2.2f"))

print("  Exam average (40% of grade):", format(exAvg, "2.2f"))

print("  St/udent course average:", format(courseAvg, "2.2f"))

# Providing a letter grade based on the course average #

if (90 <= courseAvg <= 100):
    print("  Course grade (CS303E: Spring, 2021): A")
             
elif (80 <= courseAvg < 90):
    print ("  Course grade (CS303E: Spring, 2021): B")

elif (70 <= courseAvg < 80):
    print ("  Course grade (CS303E: Spring, 2021): C")
    
elif (60 <= courseAvg < 70):
    print ("  Course grade (CS303E: Spring, 2021): D")

elif (0 <= courseAvg < 60):
    print ("  Course grade (CS303E: Spring, 2021): F")




