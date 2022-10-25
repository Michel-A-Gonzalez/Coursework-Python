# File: Student.py
# Student: Michel Gonzalez
# UT EID: Mag9989
# Course Name: CS303E
# 
# Date Created: 03/23/2021
# Date Last Modified: 03/23/2021
# Description of Program: The purpose of this program is develpoe a class that
# allows the user to input a name of a student and two exam grades which can
# be computed to give the avergae grade of that student.

class Student:

    def __init__(self, name, ex1 = "None", ex2 = "None"):
        ''' Construct a Studnet object with a name and two exam grades
            (exam grades default to None). '''
        
        self.__name = name
        self.__ex1 = ex1
        self.__ex2 = ex2
        

    def __str__(self):

        return " Student: " + str(self.__name) \
               + "\n   Exam1: " + str(self.__ex1) \
               + "\n   Exam2: " + str(self.__ex2)

    
    def getName(self):

        return self.__name

    def getExam1Grade(self):

        if(self.__ex1 != "None"):

            return self.__ex1
        
        else:

            return

    def setExam1Grade(self, ex1):

        self.__ex1 = ex1

    def getExam2Grade(self):

        if(self.__ex2 != "None"):

            return self.__ex2

        else:

            return

    def setExam2Grade(self, ex2):

        self.__ex2 = ex2

    def getAverage(self):

        if(self.__ex1 != "None" and self.__ex2 != "None"):

            self.__avg = (int(self.__ex1) + int(self.__ex2))/2

            return float(format(self.__avg, "2.1f"))

        else:

            return "Some exam grades not available."
        
    

    
