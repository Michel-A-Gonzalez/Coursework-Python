#  File: Triangle.py

#  Description: This program runs through four different methods of
#               solving for the path with the largest sum. It will return
#               the largest sum value and the time it takes for the program
#               to find it.

#  Student Name: Michel Gonzalez

#  Student UT EID: Mag9989

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 07/09/2021

#  Date Last Modified: 07/09/2021

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force (grid):
        

    # I used two funtions to get the largest path sum of the given
    # triangle by having this fucntion get the list that is created
    # in the helper fucntion

    lst_sum = []

    brute_force_helper (grid, 0, 0, lst_sum, 0)

    return max(lst_sum)

def brute_force_helper (grid, idx_i, idx_j, lst_sum, total):

    # Generates a list of all the possible path sums in the
    # given triangle

    if (idx_i == len(grid)):

        lst_sum.append(total)

    else:

        total += grid[idx_i][idx_j]

        return brute_force_helper(grid, idx_i + 1, idx_j, lst_sum, total) or \
               brute_force_helper(grid, idx_i + 1, idx_j + 1, lst_sum, total)

    
# returns the greatest path sum using greedy approach
def greedy (grid):

    total = 0

    i = 0

    j = 0

    while (i < len(grid)):

        # checks all number on the greedy path except the last number

        if( i + 1 < len(grid) and j + 1 < len(grid[i])):

            # adds the current number and then looks for the larger
            # adjacent number to it

            total += grid[i][j]

            # if the left adjacent number is larger then the path
            # just moves down, else it moves down and to the right
            # one

            if (grid[i + 1][j] > grid[i + 1][j + 1]):

                i += 1

            else:

                i += 1

                j += 1

        # Adds the final number to the total and breaks the loop since
        # it reached the end

        else:

            total += grid[i][j]

            break

    return total

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):

    # I used a helper function to get the greates path and
    # the inital value starts at the peak of the triangle

    total = 0

    divide_conquer_helper(grid, 0, 0, total)

    return total

def divide_conquer_helper(grid, idx_i, idx_j, total):

    # This method approchaes the problem by simplifying
    # the triangle into a single digit in which case
    
    if (len(grid) == 1):

        return total

    else:

        # Creates two seperate tringles everytime the program
        # runs through the fucntion which are simplified versions
        # of the original triangle

        grid_1 = grid[1:]

        grid_2 = grid[1:]

        cut = 1

        for i in range(0, len(grid_1)):

            grid_1[i] = grid_1[i][:cut]

            cut += 1

        for i in range(0, len(grid_2)):

            grid_2[i] = grid_2[i][1:]

        # The totals will get all the possible totals however it will only
        # the largest sum once it has reached the end

        total_1 = total

        total += grid_1[0][0]

        total_1 += grid_2[0][0]

        # I assigned variables since the tringle is always split into two
        # seperate tringles in which case I check which tringle has a larger
        # sum and return that sum

        x = divide_conquer_helper(grid_1, total)

        y = divide_conquer_helper(grid_2, total_1)

        if(y > x):

            return y

        else:

            return x


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):

    # This approach begins the problem at the bottom of the triangle
    # and checks which number has a greater sum with the number above

    for i in range(len(grid) - 1, -1, -1):

        for j in range(0, len(grid[i])):

            if(i - 1 > -1 and j + 1 < len(grid)):

                left_adj = grid[i][j]

                right_adj = grid[i][j + 1]

                num_above = grid[i - 1][j]

                # Checks weather the left adjacent number has a greater
                # sum than the right, and assignes the greater sum as the
                # new value of the number above the two adjacent numbers

                if(num_above + left_adj > num_above + right_adj):

                    grid[i - 1][j] = num_above + left_adj

                else:

                    grid[i - 1][j] = num_above + right_adj

            else:

                break

    return grid[0][0]

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
    # read number of lines
    line = sys.stdin.readline()
    
    line = line.strip()
    
    n = int (line)

    # create an empty grid with 0's
    grid = [[0 for i in range (n)] for j in range (n)]

    # read each line in the input file and add to the grid
    for i in range (n):

        line = sys.stdin.readline()
        
        line = line.strip()
        
        row = line.split()
        
        row = list (map (int, row))
        
        for j in range (len(row)):
        
            grid[i][j] = grid[i][j] + row[j]

    return grid 

def main ():
    # read triangular grid from file
    grid = read_file()
  
    
    # check that the grid was read in properly
    
    # output greatest path from exhaustive search

    print('The greatest path sum through exhaustive search is')

    print(brute_force (grid))

    times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)

    times = times / 10
    
    # print time taken using exhaustive search

    print('The time taken for exhaustive search in seconds is')

    print(times)

    # output greatest path from greedy approach

    print('The greatest path sum through greedy search is')

    print(greedy (grid))
    
    times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)

    times = times / 10
    
    # print time taken using greedy approach

    print('The time taken for greedy approach in seconds is')

    print(times)

    # output greatest path from divide-and-conquer approach

    print('The greatest path sum through recursive search is')

    print(divide_conquer (grid))

    times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)

    times = times / 10
    
    # print time taken using divide-and-conquer approach

    print('The time taken for recursive search in seconds is')

    print(times)

    # output greatest path from dynamic programming

    print('The greatest path sum through dynamic programming is ')

    print(dynamic_prog (grid))
    
    times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)

    times = times / 10
    
    # print time taken using dynamic programming

    print('The time taken for dynamic programming in seconds is')

    print(times)

if __name__ == "__main__":
    main()
