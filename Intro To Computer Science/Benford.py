# File: Benford.py
# Student: Michel Gonzalez
# UT EID: Mag9989
# Course Name: CS303E
# 
# Date Created: 04-20-2021
# Date Last Modified: 04-21-2021
# Description of Program: The purpose of this program is verify that the U.S.
# census of 2009 follows Benford's Law. The data was provided for this
# assignment.


import os.path

                            # Stips off anny extra spaces before
                            # or after text of input
                            
filename = input("Enter the name of a file of census data: ").strip()

                            # checks if the input file exists at all in
                            # the system
                            
if not os.path.isfile(filename):

    print("File does not exist", end = "")

    quit()

dataSet = set()

count = 0

dataDictionary = {}

for i in range(1, 10):
    
                            # fills dictionary [digits:count] where digits
                            # range from 1 to 9 and count is temporarly 0
                            
    dataDictionary[i] = count

print(dataDictionary)

infile = open(filename, "r")

text = infile.read().split()

countC = 0

for j in range (1, 10):

    for i in range(3, len(text)):
        
                            # checks the text for numbers
                            
        if(text[i].isdigit() == True):
            
                            # countC counts the number of cities in the census 
            countC += 1

                            # using sets to find the unique number of populations

            dataSet.add(text[i])

            strNumber = str(text[i])
            
                            # checks if the first digit is a certain digit and
                            # adds one to the counter each time a number has
                            # a certain digit as its first digit
                            
            if(int(strNumber[0]) == j):

                count += 1
                    
            else:

                continue
    
        else:

            continue
        
                            # replaces the previous count in the dictioanry
                            # with counted values for each digit
                            
    dataDictionary[j] = count

    count = 0
    
                            # since countC was counted 9 times, dividing it
                            # by 9 gave us the actual number of cities
                            
countC = countC // 9

populations = len(dataSet)

digits = list(dataDictionary.keys())

values = list(dataDictionary.values())

infile.close()

                            # creats the output file benford.txt and writes
                            # the needed information in it

print("Output written to benford.txt", end = "")

outfile = open("benford.txt", "w")

outfile.write("Total number of cities: " + str(countC) + "\n")

outfile.write("Unique population counts: " + str(populations) + "\n")

outfile.write("First digit frequency distributions:\n")

outfile.write("Digit\t" + "Count\t" + "Precentage\n")

i = 0

while(i < 9):

    percent = (values[i]/countC) * 100

    outfile.write(str(digits[i]) + "\t" + str(values[i]) + "\t" + format(percent, "1.1f") + "\n")

    i += 1

outfile.close()


          



        

    
    
