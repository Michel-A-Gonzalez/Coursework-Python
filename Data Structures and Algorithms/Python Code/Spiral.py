#  File: Spiral.py

#  Description: The purpose of this program is to obtain the sum
#               of numbers adjecient to a chosen number on the
#               spiral. The spiral was created by using triangles of values
#               for the four sides of the 2-D matrix.
#               

#  Student Name: Michel Gonzalez

#  Student UT EID: MAG9989

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 06/07/2021

#  Date Last Modified: 06/08/2021

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral ( n ):

    if( n < 0 or  n < 1 or n > 100):                                            # checks that a valid integer is used for this program
                                                                                # and returns a 0 if its invalid
        return 0

    elif( n % 2 == 0):                                                          # Checks for any even integeres and turns them odd
                                                                                # by adding one to n
        n += 1

    spiral = [[0  for i in range(0, n)] for j in range(0, n)]                   # creates the 2-D list full of 0's and has dimension 
                                                                                # n x n
    for i in range(1, n):

        start = (n - (2*(i-1))) ** 2                                            # Sets the starting value of each box of numbers

        k = 0

        for j in range(n - i, -2 + i, -1):                                      # creates the upper triangle of numbers

            spiral[i - 1][j] = start - k

            k += 1

        k = 0

        for j in range(0 +(i - 1), n - (i - 1)):                                # creates the right side triangle of numbers

            if(start == 1):

                break

            else:
                spiral[j][i - 1] = (start - ((n - 1) - 2*(i - 1))) - k

                k +=1

        k = 0

        for j in range(0 + (i - 1), n - (i - 1)):                               # creates the lower triangle of numbers

            if(start == 1):

                break

            else:

                spiral[n - i][j] = (start - (2*((n - 1) - 2*(i - 1)))) -k

                k += 1

        k = 0

        for j in range(n - i, -1 + i, -1):                                      # creates the left side triangle of numbers

            if(start == 1):

                break

            else:

                spiral[j][n - i] = (start - (3*((n - 1) - 2*(i - 1)))) - k

                k += 1

    return spiral                                                               # Note** Each triangle was created by knowing that the north-east
                                                                                # diagonal consists of only perfect square values of odd numbers
                                                                                # and changing the starting value depednig on the side of the spiral
                                                                                # and how close the starting value is to the tip of the triangle         
                                                                                #(the value 1)


# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers (spiral, n):

    if(n > spiral[0][len(spiral) - 1]):                                         # Checks if the integer n is within the range n*n
    
        return 0

    total = 0

    for i in range(0 , len(spiral)):

        for j in range(0, len(spiral[i])):

            if(spiral[i][j] == n):                                                              # finds the required indicies i and j

                if(i - 1 < 0 and j - 1 < 0):                                                    # The following if - elif - else statements check
                                                                                                # the position of the integer n in the 2-D matrix
                    total = spiral[i][j + 1] + spiral[i + 1][j] + spiral[i + 1][j + 1]          # and depednding on the postion summates the appropriate
                                                                                                # adjacent numbers and breaks the loop once the total is gotten
                    break
        
                elif(i + 1 > (len(spiral) - 1) and j - 1 < 0):

                    total = spiral[i - 1][j] + spiral[i - 1][j + 1] + spiral[i][j + 1]

                    break
         
                elif(j + 1 > (len(spiral) - 1) and i - 1 < 0):

                    total = spiral[i][j - 1] + spiral[i + 1][j - 1] + spiral[i + 1][j]

                    break

                elif(i + 1 > (len(spiral) - 1) and j + 1 > (len(spiral) - 1)):

                    total = spiral[i - 1][j] + spiral[i][j - 1] + spiral[i - 1][j - 1]

                    break
        
                elif(i - 1 < 0):

                    total = spiral[i][j - 1] + spiral[i][j + 1] + spiral[i + 1][j - 1] + \
                            spiral[i + 1][j] + spiral[i + 1][j + 1]

                    break
        
                elif(j - 1 < 0):

                    total = spiral[i - 1][j] + spiral[i + 1][j] + spiral[i + 1][j + 1] + \
                            spiral[i][j + 1] + spiral[i - 1][j + 1]
        
                elif(i + 1 > (len(spiral) - 1)):
        
                    total = spiral[i][j - 1] + spiral[i][j + 1] + spiral[i - 1][j - 1] + \
                            spiral[i - 1][j] + spiral[i - 1][j + 1]

                    break
        
                elif(j + 1 > (len(spiral) - 1)):

                    total = spiral[i - 1][j] + spiral[i + 1][j] + spiral[i + 1][j - 1] + \
                            spiral[i][j - 1] + spiral[i - 1][j - 1]

                    break
   
                else:

                    total = spiral[i - 1][j - 1] + spiral[i - 1][j] + spiral[i - 1][j + 1] + \
                            spiral[i][j - 1] + spiral[i][j + 1] + spiral[i + 1][j - 1] + \
                            spiral[i + 1][j] + spiral[i + 1][j + 1]

                    break
                
            else:

                continue
        
    return total

def main():                                                         # reads in the file and uses the number in first line as
                                                                    # the dimension of the 2-D list, then the spiral is created
    import sys                                                      # lastly it gets the sum of the adjacent numbers of the integer n
                                                                    # for all numbers n in the file and prints the total.
    in_file = sys.stdin.readlines()

    dimension_of_spiral = int(in_file[0])

    spiral = create_spiral(dimension_of_spiral)

    for i in range(1, len(in_file)):

        total = 0

        total = sum_adjacent_numbers (spiral, int(in_file[i]))

        print(total)

    return

if __name__ == "__main__":
  main()
