# File: ComparingLinearBinarySearch.py
# Student: Michel Gonzalez
# UT EID: Mag9989
# Course Name: CS303E
# 
# Date Created: 04-12-2021
# Date Last Modified: 04-12-2021
# Description of Program: The purpose of this program is to compare
# the efficency of the linear and binary search functions by
# comparing how many probes each function had to preform.
# (Note: both search fucntions were provided)

import random

import math

def linearSearch( lst, key ):
    """ Search for key in unsorted list lst.  Note that
        the index + 1 is also the number of probes. """
    for i in range( len(lst) ):
        if key == lst[i]:
            return i    
    return -1

def binarySearch( lst, key ):
    """ Search for key in sorted list lst. Return
        a pair containing the index (or -low - 1)
        and a count of number of probes. """
    count = 0
    low = 0
    high = len(lst) - 1
    while (high >= low):
        count += 1
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return (mid, count)
        else:
            low = mid + 1
    # Search failed
    return (-low - 1, count)





lst = []                                # Part: 1

for i in range(0, 1000):

    lst.append(i)

random.shuffle(lst)

for j in range(0, 6):

    n = (10 ** j)

    count = 0

    total = 0

    for i in range(0, n + 1):

        k = random.randint(0, 999)

        count = (linearSearch(lst, k) + 1)

        total += count

    if (j == 1):                        # Getting the different averages based
                                        # on the number of tests
            avg1 = (total / n)          

    elif (j == 2):

            avg2 = (total / n)

    elif (j == 3):

            avg3 = (total / n)

    elif (j == 4):

            avg4 = (total / n)

    elif (j == 5):

            avg5 = (total / n)

avgList = [avg1, avg2, avg3, avg4, avg5]





lst2 = []                               # Part: 2

for i in range(0, 1000):

    lst2.append(i)

nB = 1000

countB = 0

totalB = 0

for i in range(0, nB + 1):

    j = random.randint(0, 999)

    countB = int(binarySearch(lst2, j)[1])  # Retreving only the count of the
                                            # output
    totalB += countB

avgB = (totalB/nB)

diffB = (math.log(nB,2) - avgB)





print("Linear search:")                     # Prints values into table format

for j in range (1, 6):

    n = 10 ** j

    print("  Tests:", format(n, "<8d"), \
          "Avgerage probes:", avgList[j - 1]) 

print("Binary search:")

print("  Average number of probes:", avgB)
print("  Differs from log2(1000) by:", diffB)




    



    



