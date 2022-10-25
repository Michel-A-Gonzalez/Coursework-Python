#  File: DNA.py

#  Description: The purpose of this program is to compare the
#               two strands of DNA that are no longer than 80 characters long
#               and findS the longest substrings between both DNA strands
#               

#  Student Name: Michel Gonzalez

#  Student UT EID: MAG9989

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 06/06/2021

#  Date Last Modified: 06/07/2021

#  Input: s1 and s2 are two strings that represent strands of DNA
#  Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.


def longest_subsequence (s1, s2):

    len_s1 = len(s1)

    len_s2 = len(s2)

    longest_sub = []

    if(len_s1 > 80 or len_s2 > 80):         # checks for srings that are too long
                                            # and returns if they exceed the limit
        return longest_sub

    elif(len_s1 >= len_s2):                 # uses the smaller string to find
                                            # substrings through for loops
        for i in range(0, len_s1):

            for j in range(0, len_s2):                                      

                k = 0

                sub_str = []

                while(i + k < len_s1 and j + k < len_s2):

                    if(s1[i + k] == s2[j + k]):                     # Creates a list of elemetns that are
                                                                    # in a substring
                        sub_str.append(s1[i + k])

                        k += 1

                    else:

                        break

                longest_sub.append(sub_str)                         # stores all found substirngs in each run

    elif(len_s2 > len_s1):                                          # Preformes the same way as the code above
                                                                    # by keeping the smaller string as the 
        for i in range(0, len_s2):                                  # nested for loop

            for j in range(0, len_s1):

                k = 0

                sub_str = []

                while(i + k < len_s2 and j + k < len_s1):

                    if(s2[i] == s1[j] and s2[i + k] == s1[j + k]):

                        sub_str.append(s2[i + k])

                        k += 1

                    else:

                        break

                longest_sub.append(sub_str)

    longest_sub = [''.join(i) for i in longest_sub]                 # joins all list of elemts to become substrings

    i = 0

    while i < len(longest_sub):                                     # gets rid of all single character substirngs found

        if(len(longest_sub[i]) <= 1 or '\n' in longest_sub[i]):

            longest_sub.pop(i)

        else:

            i += 1

    longest_str = 0

    for i in range(0, len(longest_sub)):                            # finds the length of the longest substring

        if(longest_str < len(longest_sub[i])):

            longest_str = len(longest_sub[i])

    i = 0

    longest_sub.sort()

    while(i < len(longest_sub)):                                    # pops off all substrings that are shorter
                                                                    # than the longest substring
        if not(len(longest_sub[i]) == longest_str):

            longest_sub.pop(i)

        else:

            i += 1
                                                                    # sorts the list found in alphabetical order 
    i = 0
    
    if(len(longest_sub) > 1):                                       # checks if the list of substrings has any repeats                                 
                                                                    # and omits any repeat
        while(i < len(longest_sub)):

            if(i + 1 < len(longest_sub)):

                if(longest_sub[i] == longest_sub[i + 1]):

                    longest_sub.pop(i)

                else:
                    i += 1
            else:

                break

    return longest_sub

def main():

    import sys
    
    in_file = sys.stdin.readlines()                                             # creats a list of all the contents in dna.in file

    num_of_pairs = int(in_file[0])

    for i in range(1, num_of_pairs * 2, 2):                                     # uses the integer givin at the top of the file to
                                                                                # let the computer iterate through that many pairs
        if(longest_subsequence(in_file[i], in_file[i+1]) == []):                # calls the fucntion and prints out
                                                                                # appropriate output
            print("No Common Sequence Found")

        else:

            for i in longest_subsequence(in_file[i], in_file[i+1]):

                print(i)

        print()

    return

if __name__ == "__main__":
  main()
