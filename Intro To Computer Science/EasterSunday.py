# File: EasterSunday.py
# Student: Michel Gonzalez
# UT EID: Mag9989
# Course Name: CS303E
# 
# Date Created: 02-01-2021
# Date Last Modified: 02-04-2021
# Description of Program: The purpose of this program is to be able to give the the date of Eatser Sunday on a requested year by the user.


y = int(input( "Enter year: " )) #Saving the input year number into variable y.

a = y % 19  

b = y // 100

c = y % 100

d = b // 4

#print(a,b,c,d)
 
e = b % 4

g = ((8 * b) + 13) // 25

h = ((19 * a) + b - d - g + 15) % 30

j = c // 4

#print (e,f,g,h)

k = c % 4

m = (a + (11 * h)) // 319

r = ((2 * e) + (2 * j) - k - h + m + 32) % 7

n = (h - m + r + 90) // 25

p = (h - m + r + n + 19) % 32

#print (a,b,c,d,e,g,h,j,k,m,n,p)

print( "In", y ,"Easter Sunday is on month", n ,"and day", p)





