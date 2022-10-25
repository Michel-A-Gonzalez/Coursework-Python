# File: MyStringFunctions.py
# Student: Michel Gonzalez
# UT EID: Mag9989
# Course Name: CS303E
# 
# Date Created: 03-28-2021
# Date Last Modified: 03-28-2021
# Description of Program: The purpose of this program is to construct
# the functions of built in commands for string class objects that
# may modify a string or give information about a string.

def myAppend(str, ch):

    # This will return a new string that is like str but with 
    # character ch added at the end

    return str + ch

def myCount(str, ch):

    # This will return the number of times character ch appears
    # in str.

    i = 0

    count = 0

    size = len(str)

    for i in range (0, size):

        j = str[i]

        if (j == ch):

            count += 1

        else:

            continue

    return count

def myExtend(str1, str2):

    # This will return a new string that contains the elements of
    # str1 followed by the elements of str2

    str3 = str1 + str2

    return str3

def myMin(str):

    # This will return the character in str with the lowest ASCII
    # code

    if (str == ""):

        print("Empty string: no min value")

        return None
    
    else:

        minNum = ord(str[0])

        for i in str:

            x = ord(i)

            if (x > minNum):

                continue
            
            else:

                minNum = x

    minCh = chr(minNum)

    return minCh

def myInsert(str , i, ch):

    # Return a new string like str except that ch has been
    # inserted at the ith position.
    l = len(str)

    if (i > l):

        print("Invalid index")

        return None

    else:

        if (i == 0):

            str = ch + str

            return str

        elif (i == l):

            str = str + ch

            return str

        else:

            j = str[i : l]

            j = ch + j 

            h = str[-l : i - l]

            str = h + j

            return str

def myPop(str, i):

    # This will return a new string that is like str but with the ith
    # element removed and the value that was removed.
    
    l = len(str)

    if( i >= l):

        print("Invalid index")

        print ("('" + str + "', None)")

        return None
    
    else:

        ch = str[i]

        j = str[i + 1 : l]

        h = str[-l : i - l]

        str = h + j

        print("('" + str + "', '" + ch + "')")

        return

def myFind(str, ch):

    # This will return the index of the first occurrence of 
    # ch in str, if any.

    if(ch not in str):

        return -1
    
    else:

        l = len(str)

        for i in range(0, l):

            if (ch == str[i]):

                return i
            
            else:

                continue

def myRFind(str, ch):

    # This will return the index of the last occurrence of 
    # ch in str, if any.

    if(ch not in str):

        return -1

    else:

        l = len(str)

        n = l - 1

        str1 = ""

        for i in range (0, l):

            h = str[n]

            n -= 1

            str1 = str1 + h

        for i in range (-l, 0):

            if (ch == str1[i]):

                num = -1 * (i + 1)

                return num

def myRemove(str, ch):

    # This will return a new string with the first occurrence of ch 
    # removed.

    if(ch not in str):

        return str

    else:

        l = len(str)

        for i in range(0, l):

            if(ch == str[i]):

                j = str[i + 1 : l]

                h = str[-l : i]

                str = h + j

                return str

            else:

                continue

def myRemoveAll(str, ch):

    # This will return a new string with all occurrences of ch.
    # removed.

    if(ch not in str):

        return str

    else:

        for i in range(0, len(str)):

            if (i >= len(str)):

                return str

            elif (ch == str[i]):

                j = str[i + 1 : len(str)]

                h = str[-len(str) : i]

                str = h + j

def myReverse(str):

    # Return a new string like str but with the characters
    # in the reverse order.

    l = len(str)

    n = l - 1

    str1 = ""

    for i in range (0, l):

        h = str[n]

        n -= 1

        str1 = str1 + h

    return str1
    
    
        
