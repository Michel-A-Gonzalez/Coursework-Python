# File: RecursiveFunctions.py
# Student: Michel Gonzalez
# UT EID: Mag9989
# Course Name: CS303E
# 
# Date Created: 04/26/2021
# Date Last Modified: 04/26/2021
# Description of Program: The purpose of this program is to become
# familiar with recursive programing by recursively programing multiple
# functions.


def sumItemsInList( L ):
    """ Given a list of numbers, return the sum. """
    
    if(L == []):
        
        return 0
    
    else:
        
        return L[0] + sumItemsInList(L[1:])

def countOccurrencesInList( key, L ):
    """ Return the number of times key occurs in 
    list L. """
    
    if(L == []):
        
        return 0
    
    elif(key == L[0]):
        
        return 1 + countOccurrencesInList(key, L[1:])
    
    else:
        
        return countOccurrencesInList(key, L[1:])

def addToN ( n ):
   """ Add up the non-negative integers to n.
    E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5. """
   
   if n == 0:

       return 0

   else:
    
       return n + addToN(n-1)

def findSumOfDigits( n ):
   """ Return the sum of the digits in a non-negative integer. """
   
   if n == 0:

       return 0

   else:

       i = str(n)

       l = list(i)

       i = l[1:]

       n = "".join(i)

       if i != []:

           n = int(n)
           
       else:

           n = 0

   return int(l[0]) + findSumOfDigits(n)

           
   
def decimalToBinary( n ):
   """ Given a nonnegative decimal integer n, return the 
   binary representation as a string. """

   if(n // 2 == 0):

       if(n == 1):

           return "1"

       else:

           return "0"

   elif(n >= 2):

       return str(decimalToBinary(n//2)) + str(n % 2)

    
    

def decimalToList( n ):
   """ Given a positive decimal integer, return a list of the 
   digits (as strings). """

   if(n == 0):

       return []

   else:

       i = str(n)

       l = i[1:]

       if l != "":

           n = int(l)

           return [i[0]] + decimalToList(n)
           
       else:

           return [i]

def isPalindrome( s ):
   """ Return True if string s is a palindrome and False
   otherwise. Count the empty string as a palindrome. """

   if(len(s) < 2):

       return True

   elif(s[0] != s[len(s) - 1]):

       return False

   return isPalindrome(s[1:len(s) - 1])

def findFirstUppercase( s ):
   """ Return the first uppercase letter in 
   string s, if any.  Return None if there
   is none. """

   if(s == ""):

       return None

   elif(s[0].isupper()):

        return s[0]
    
   return findFirstUppercase(s[1:])

       

def findFirstUppercaseIndexHelper( s, index ):
   """ Helper function for findFirstUppercaseIndex. """

   if(index == len(s)):

       return -1

   elif(s[index].isupper()):

       return index

   else:

       index += 1

   return findFirstUppercaseIndexHelper(s, index)

# The following function is already completed for you.  But 
# make sure you understand what it's doing. 

def findFirstUppercaseIndex( s ):
   """ Return the index of the first uppercase letter in 
   string s, if any.  Return -1 if there is none.  This one 
   requires a helper function, which is the recursive 
   function. """
   return findFirstUppercaseIndexHelper( s, 0 )
