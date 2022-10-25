#  File: Work.py

#  Description: This program 

#  Student Name: Michel Gonzalez

#  Student UT EID: Mag9989

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 06/30/2021

#  Date Last Modified: 06/30/2021

import sys

import time

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):

    # Gets the sum of the series by adding all terms until
    # v // k ** p < 0 and returns the summation of the series

    i = 0

    total = 0

    while (v // (k ** i) > 0):

        total += v // (k ** i)

        i += 1

    return total

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):

    # Checks if the number of lines required is less than the prodoction
    # factor in whihc case it returns n which would be the minimum number
    # of lines needed

    if(n <= k):

        return n

    # If the number of lines required is greater than the production
    # factor then it will looks for the minimum lines of code to write
    # in a linear fashinon by checking all instances until it finds
    # the minimum. This is done using the sum_series function

    else:

        lst = []

        for i in range(1, n + 1):

            lst.append(i)

        for i in range(0, len(lst)):

            if (sum_series(lst[i],k) >= n):

                return lst[i]

            else:

                continue

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):

    # Checks if the number of lines required is less than the prodoction
    # factor in whihc case it returns n which would be the minimum number
    # of lines needed

    if(n <= k):

        return n

    # If the number of lines required is greater than the production
    # factor then it will looks for the minimum lines of code to write
    # in a logarithmic fashinon by starting in the middle of the array
    # and checking if the sum_seires total of that number is greater than
    # the total number of lines needed and if the previous number's
    # sum_series total is less than the total number of lines needed

    else:

        lst = []

        for i in range(1, n + 1):

            lst.append(i)

        low = 0

        high = len(lst) - 1

        mid = 0

        while (low <= high):

            mid = (high  + low) // 2

            if (sum_series(lst[mid], k) < n):

                low = mid + 1

            elif (sum_series(lst[mid], k) >= n):
                
                if (not (sum_series(lst[mid - 1], k) >= n)):

                    return lst[mid]

                else:

                    high = mid - 1

            else:

                break

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
    
    # write your own test cases

    assert sum_series (1, 2) == 1

    assert sum_series (50, 5) == 62

    assert sum_series (200, 100) == 202

    assert sum_series (5, 50) == 5

    assert linear_search (2, 5) == 2

    assert linear_search (30, 5) == 25

    assert linear_search (300, 2) == 152

    assert linear_search (500, 500) == 500

    assert binary_search (5, 2) == 4

    assert binary_search (30, 25) == 29

    assert binary_search (300, 2) == 152

    assert binary_search (1, 2) == 1

    assert linear_search (200, 10) == binary_search (200, 10)

    return "all test cases passed"

def main():
    # read number of cases
    line = sys.stdin.readline()
    line = line.strip()
    num_cases = int (line)

    for i in range (num_cases):
        line = sys.stdin.readline()
        line = line.strip()
        inp =  line.split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()

if __name__ == "__main__":
  main()
