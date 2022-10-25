# File: Project3.py
# Student: Michel Gonzalez
# UT EID: Mag9989
# Course Name: CS303E
# 
# Date Created: 04-27-2021
# Date Last Modified: 04-27-2021
# Description of Program: The purpose of this program is to simulate a database
# with a search feture thorugh commands using infomation about Covid-19 cases
# and deaths in Texas counties and statewide.

import os.path

dataDictionary = {}

count = 0

infile = open("county-covid-data.txt", "r")

text = infile.read().split("\n")

lengthText = len(text)

i = 0

while(i < lengthText):                  # \
                                        #  \
    if ("#" in text[i]):                #   \
                                        #    \
            text.pop(i)                 #     \
                                        #       This loop will get rid of all list items with
            lengthText -= 1             #     / a "#" in it.
                                        #    /
    else:                               #   /
                                        #  /
        i += 1                          # /

text = ",".join(text)                   # creats new list "text" with splitings on the commas
                                        # after the previous "text" list was joined by commas
text = text.split(",")                  #
                                        # gets rid of the empty string item at the end of the
text.pop(len(text) - 1)                 # list

totalCases = 0                          # \
                                        #  \
totalDeaths = 0                         #   \
                                        #    \
countyNum = []                          #     \
                                        #       Setting up our variables
counties = []                           #     /
                                        #    /
j = 1                                   #   /
                                        #  /
k = 3                                   # /

for i in range(0, len(text) - 1, 4):

    if(i < len(text)):                  #  
                                        # creats a list of just the counties
         counties.append(text[i])       #

    if( j < len(text)):

        countyNum.append((int(text[j]), int(text[j+2])))

        totalCases += int(text[j])      # creats a list with tuple values of confirmed cases
                                        # and deaths, also gives the total confirmed cases in Texas
        j += 4                          #

    if(k < len(text)):
                                        # gives the total deaths in texas
        totalDeaths += int(text[k])     #
                                        #
        k += 4

    else:

        break

j = 0

for i in counties:
                                        # creats a dictioanry with counties being the keys
    dataDictionary[i] = countyNum[j]    # and the tuple covid cases and deaths being the 
                                        # assigend values
    j += 1

dataDictionary["Texas"] = (totalCases, totalDeaths)     # adds Texas to the list

commandList = ["Help", "Quit", "Counties", "Cases", "Deaths"] # used to check if an invalid command was entered

print("Welcome to the Texas Covid Database Dashboard.")                                         # \
                                                                                                # \
print("This provides Covid data in Texas as of 1/26/21.")                                       #  \
                                                                                                #  \
print("Creating dictionary from file: county-covid-data.txt\n")                                 #   \
                                                                                                #   \
print("Enter any of the following commands:")                                                   #    \
                                                                                                #    \
print("Help - list available commands;")                                                        #      Prints out the Welcome message
                                                                                                #    /
print("Quit - exit this dashboard;")                                                            #    /
                                                                                                #   /
print("Counties - list all Texas counties;")                                                    #   /
                                                                                                #  /
print("Cases <countyName>/Texas - confirmed Covid cases in specified county or statewide;")     #  /
                                                                                                # /
print("Deaths <countyName>/Texas - Covid deaths in specified county or statewide.\n")           # /

commandInput =  input("Please enter a command: ").strip()
                                        #
n = commandInput                        # changes input command into a string that can be
                                        # read by the program. This makes the input not 
commandInput = commandInput.lower()     # case sensetive
                                        #
commandInput = commandInput.capitalize()#
                                        
while(commandInput != "Quit"):          # loops a command input until a varation of "Quit"
                                        # is entered
    if(commandInput == "Help"):         
                                        # prints out "Help" fucntion of program
        print("Help - list available commands;")

        print("Quit - exit this dashboard;")

        print("Counties - list all Texas counties;")

        print("Cases <countyName>/Texas - confirmed Covid cases in specified county or statewide;")

        print("Deaths <countyName>/Texas - Covid deaths in specified county or statewide.\n")

    elif(commandInput == "Counties"):
                                        # prints out the name of the counties 10 
        for i in counties:              # at a time

                count += 1

                if(count < 10):

                    print(i, end = " ")

                if count == 10:

                    count = 0

                    print(i, end = "\n")
                    
        print("\n")

    # Parse the command into a list of words (assuming there's no punctuation).     # \
    commWords = commandInput.split()                                                #  \
                                                                                    #   \
    # Extract the first word in the command (which is always a one-word command):   #    \
    comm = commWords[0]                                                             #      given to us and deals with
                                                                                    #    / coutnies with two names.
    # Extract the rest of the words and re-assemble them into a single string,      #   /
    # separated by spaces.                                                          #  /
    args = commWords[1:]                                                            # /
    arg = " ".join(args)                                                            

    if (len(args) == 2):
                                        # checks if the coutny entered has two names
        arg = arg.lower()               # and converts it to a usable command by the
                                        # program
        arg = arg.title()               #
        
    else:                               
                                        # If the county entered only has one name
        arg = arg.lower()               # then it is still convereted to a usable 
                                        # command by the program
        arg = arg.capitalize()          #

    if(comm == "Cases"):
                                        # Checks if the intial command is valid and
        if(arg == "Texas"):             # if it is "cases"
                                        # checks if Texas was the "county" entered
            print(arg + " total confirmed Covid cases: ", totalCases, "\n")

        elif(arg in counties):                      
                                                    # checks if the county enterd is in the
            for i in range(0 , len(counties)):      # list of counties
                                                    #
                if (counties[i] == arg):            # if the county is valid it prints out
                                                    # appropriate information for covid
                    v = dataDictionary.get(arg)     # cases
                                                    # 
                    print(arg + " county has", v[0], "confirmed Covid cases.\n")

        else:                                       # gives error message for invalid county
                                                    #
            print("County " + n + " is not recognized. \n")

    elif(comm == "Deaths"):             # this works the same way as the "cases" command
                                        # except it deals with the data for deaths
        if(arg == "Texas"):
        
                print(arg + " total confirmed Covid cases:", totalDeaths, "\n")

        elif(arg in counties):

            for i in range(0 , len(counties)):

                if (counties[i] == arg):

                    v = dataDictionary.get(arg)

                    print(arg + " county has", v[1], "fatalities.\n")

        else:

            print("County " + n + " is not recognized.\n")

    elif(commandInput not in commandList):          # checks if the input command is valid 
                                                    # and gives error message if not
        print("Command is not recognized. Try again!\n")

    commandInput =  input("Please enter a command: ").strip()       # allows for multiple commands to be entered until
                                                                    # a variation of "quit" is entered
    n = commandInput                                                #
                                                                    #
    commandInput = commandInput.lower()                             #
                                                                    #
    commandInput = commandInput.capitalize()                        #
                                                                    #

print("Thank you for using the Texas Covid Database Dashboard.  Goodbye!")
                                                                                # after quit is entered Goodbye message is
infile.close()                                                                  # printed and file is closed




            


        

        
