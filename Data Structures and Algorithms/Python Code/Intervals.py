#  File: Intervals.py

#  Description:              

#  Student Name: Michel Gonzalez

#  Student UT EID: MAG9989

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 06/07/2021

#  Date Last Modified: 06/08/2021

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples (tuples_list):

    if(len(tuples_list) == 1 and tuples_list[0][0] != tuples_list[0][1]):

        return tuples_list

    i = 0

    while(i < len(tuples_list)):

        if(tuples_list[i][0] == tuples_list[i][1]):

            tuples_list.pop(i)

        else:

            i +=1

    if(tuples_list == []):

        return tuples_list

    i = 0

    while(i < len(tuples_list)):                             # This section of the code 'cleans up' the list of
                                                            # tuples to simplify the list as much as possible.
        i_low = tuples_list[i][0]                           # Also, I used while loops so it can pop off any
                                                            # uneccesary tuples
        i_high = tuples_list[i][1]

        j = 0

        while(j < len(tuples_list)):

            j_low = tuples_list[j][0]

            j_high = tuples_list[j][1]

            if(i_low < j_low and i_high > j_high):          # Checks if the current tuple (i) covers more range
                                                            # than the tuples its being compared to (j), if true
                if(i < j):                                  # then we don't need the (j) tuple in our list
                    
                    tuples_list.pop(j)

                    i -= 1

                    break


                elif(j < i):

                    tuples_list.pop(j)

                    i -= 2

                    break

            elif(i_low == j_low  and j_high < i_high):      # Checks if the current tuple (i) starts at the same
                                                            # number as the (j) tuple and checks if the (i) tuples
                if(i < j):                                  # covers more range                         
                    
                    tuples_list.pop(j)

                    i -= 1

                    break

                elif(j < i):
                    
                    tuples_list.pop(j)

                    i -= 2

                    break

            elif(i_low < j_low and i_high == j_high):       # Checks if the current tuple (i) ends at the same
                                                            # number as the (j) tuple and checks if the (i) tuple
                if(i < j):                                  # covers more range, if true then it pops off the (j) tuple
                    
                    tuples_list.pop(j)

                    i -= 1

                    break

                elif(j < i):

                    tuples_list.pop(j)

                    i -= 2

                    break

            elif(i_low == j_high):
                                                            # Checks if the ending number of the (j) tuple is the start
                if(i < j):                                  # of the (i) tuple and replaces the (i) tuple to cover the
                                                            # ranges of both the (i) and (j) tuples 
                    tuples_list[i] = (j_low, i_high)        # Also, subtractes one from i so it can check the new (i)      
                                                            # tuple that replaced the old (i) tuple
                    tuples_list.pop(j)

                    i -= 1

                    break

                elif(j < i):

                    tuples_list[i] = (j_low, i_high)

                    tuples_list.pop(j)

                    i -= 2

                    break
                
            elif(i_high == j_low):
                                                            # Works the same as the code right above this code except
                if(i < j):                                  # it checks if the ending number of the (i) tuple is the
                                                            # start of the (j) tuple
                    tuples_list[i] = (i_low, j_high)

                    tuples_list.pop(j)

                    i -= 1

                    break

                elif(j < i):

                    tuples_list[i] = (i_low, j_high)

                    tuples_list.pop(j)

                    i -= 2

                    break

            else:

                j += 1

        i += 1
    
    i = 0

    while i < len(tuples_list):                             # This section of the code merges the cleaned tuple list
                                                            # by finding an intersection between the (i) and (j) tuples                           
        i_low = tuples_list[i][0]                           
                                                            
        i_high = tuples_list[i][1]

        j = 0

        while(j < len(tuples_list)):

            j_low = tuples_list[j][0]

            j_high = tuples_list[j][1]

            if(i_low < j_low and j_high < i_high):

                if(i < j):

                    tuples_list.pop(j)

                    break

                elif(i > j):

                    tuples_list.pop(j)

                    i -= 1

                    break


            elif(i_low < j_low and j_low < i_high):         # Checks if the starting number of the (i) tuple is lower
                                                            # than the (j) tuple and also checks if the starting number
                if(i_high < j_high):

                    if(i < j):
                        
                        tuples_list[i] = (i_low, j_high)    # of the (j) tuple is lower the ending number of the (i) tuple
                                                            # if this is true then it ckecks if the ending (j) tuple is higher
                        tuples_list.pop(j)                  # and assignes a new tuple value to i and pops off the (j) tuple from
                                                            # the list, also subtractes one to check the new (i) tuple
                        i -= 1

                        break

                    elif(i > j):

                        tuples_list[i] = (i_low, j_high)

                        tuples_list.pop(j)

                        i -= 2

                        break

                else:

                    j += 1
                    
            else:

                j += 1

        i += 1

    tuples_list.sort()

    return tuples_list

# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):
    
    length_list = []

    for i in range(0, len(tuples_list)):                                    # Gets all the different ranges from each tuple

        length_list.append(tuples_list[i][1] - tuples_list[i][0])

    length_list.sort()

    for i in range(0, len(length_list)):                                    # Sorts the tuples into order from smalles range to largest and if ranges
                                                                            # equal it puts the tuples in numerical order, it looks for a match and 
        for j in range(0, len(length_list)):                                # replaces the length with the tuple in the length_list list, and pops
                                                                            # off the tuple from the tuples_list list so no repreats will occur
            if(tuples_list[j][1] - tuples_list[j][0] == length_list[i]):    # Note* this method only works when the input list of tuples is sorted
                                                                            # if it is not sorted then any tuples with the same ranges will
                length_list[i] = (tuples_list[j][0],tuples_list[j][1])      # be placed incorrectly in the list of tuples.
                                                                            # I approched this problem knowing that the input tuple list will
                tuples_list.pop(j)                                          # always be sorted from the previous fucntion merge_tuples

                break

            else:

                continue

    return length_list

# Input: no input
# Output: a string denoting all test cases have passed

def test_cases ():

    assert merge_tuples([(1,2)]) == [(1,2)]

    assert merge_tuples([(1,2),(0,3)]) == [(0,3)]

    assert merge_tuples([(1,2),(-1,1)]) == [(-1,2)]

    assert merge_tuples([(1,1)]) == 0

    assert merge_tuples([(1,2), (-5,-2),(19,25),(1,12)]) == [(-5,-2),(1,12),(19,25)]

    assert merge_tuples([(0,5),(-8,-3),(-4,-1),(3,8),(9,12),(-1,6)]) == [(-8,8),(9,12)]
    

    assert sort_by_interval_size([(1,3),(4,5)]) == [(4,5),(1,3)]

    assert sort_by_interval_size([(1,2),(4,5)]) == [(1,2),(4,5)]

    assert sort_by_interval_size([(-5,-3),(1,7),(8,9)]) == [(8,9),(-5,-3),(1,7)]

    assert sort_by_interval_size([(1,3)]) == [(1,3)]

    assert sort_by_interval_size([(-8,8),(9,12)]) == [(9,12),(-8,8)]
    
  
    return "all test cases passed"

def main():

    import sys

    tuples_list = []
    
    in_file = sys.stdin.readlines()

    print(in_file)

    for i in range(0, len(in_file)):                            # converts the text file into list of tuples that are 
                                                                # used in each fucntion
        in_file[i] = in_file[i].replace('\n', '')

        in_file[i] = in_file[i].split(' ')

        for j in range(0, len(in_file[i])):

            in_file[i][j] = int(in_file[i][j])

    for i in range(1, len(in_file)):                            # creates the list of tuples from the text file

        in_file[i] = tuple(in_file[i])

        tuples_list.append(in_file[i])

    merged_list = merge_tuples(tuples_list)                     # prints out the sorted list of merged tuples and
                                                                # the sorted by interval size list of tuples 
    print(merged_list)

    sorted_list = sort_by_interval_size(merged_list)

    print(sorted_list)

if __name__ == "__main__":
  main()
