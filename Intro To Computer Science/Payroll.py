# File: Payroll.py
# Student: Michel Gonzalez
# UT EID: Mag9989
# Course Name: CS303E
# 
# Date Created: 02/11/2021
# Date Last Modified: 02/11/2021
# Description of Program: The purpose of this program is to calculate the amount owed to an employee after deductions


#Asking user for information and assigning it to variables
print("")
empName = input("Enter employee's name: ")
hrsWorked = float(input("Enter number of hours worked in a week: "))
hrlyRate = float(input("Enter hourly pay rate: "))
fedTax = float(input("Enter federal tax withholding rate: "))
stateTax = float(input("Enter state Tax withholding rate: "))

print("")
print("Employee Name: " + empName) 
print("Hours Worked: ", format(hrsWorked, "2.1f"), sep = "")
print("Pay Rate: $", format(hrlyRate, "2.2f"), sep = "")

#Getting the total a amount of money earned
grossPay = hrsWorked * hrlyRate

print("Gross Pay: $", format(grossPay, "2.2f"), sep = "")
print("Deductions:")

#Calcualting the deductions from federal and state taxes
fedDed = grossPay * fedTax
stateDed = grossPay * stateTax

print("  Federal Withholding (", format(fedTax, "2.1%"), "): $", format(fedDed, "2.2f"), sep = "")
print("  State Withholding (", format(stateTax, "2.1%"), "): $", format(stateDed, "2.2f"), sep = "")

#Getting the total deduction
totalDed = fedDed + stateDed

print("  Total Deduction: $", format(totalDed, "2.2f"), sep = "")

#Getting the total amount of money eraned after deductions
netPay = grossPay - totalDed

print("Net Pay: $", format(netPay, "2.2f"), sep = "")
