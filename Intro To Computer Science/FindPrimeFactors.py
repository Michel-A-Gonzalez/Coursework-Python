# File: FindPrimeFactors.py
# Student: Michel Gonzalez
# UT EID: Mag9989
# Course Name: CS303E
# 
# Date Created: 04/08/2021
# Date Last Modified: 04/09/2021
# Description of Program: The purpose of this program is to return the prime
# factorization of a given number.

print("Find Prime Factors:")

num = int(input("Enter a positive interger (or 0 to stop): "))

while(num != 0):

    if (num < 0):                       # Checks for negative inputs

        print("  Negative integer entered. Try again.\n")

        num = int(input("Enter a positive interger (or 0 to stop): "))

    elif (num == 1):                    # Checks if 1 was entered and returns
                                        # appropriate message
        print("  1 has no prime factorization.\n" )

        num = int(input("Enter a positive interger (or 0 to stop): "))


    elif (num > 1):             

        l = []

        num1 = num

        for d in range(2 , num // 2):    # Finds all factorization numbers

            while (num1 % d == 0):

                l.append(int(d))

                num1 = num1 // d

        if (num1 == num):               # If num1 was never modifed then num
                                        # is prime
            l.append(int(num))

        print("  The prime factoization of " + str(num) + " is: " + str(l) + "\n")
                
        num = int(input("Enter a positive interger (or 0 to stop): "))

if (num == 0):

    print("Goodbye!")



            

                

                    

                    

                    

            
