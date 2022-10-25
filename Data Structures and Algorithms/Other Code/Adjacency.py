#  File: Adjacency.py

#  Description: Converts an edge list into an adjacency matrix

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number: 
        
# Given an edge list of a weighted directed graph where each edge is provided as [src, dest, weight],
# return the corresponding adjancency matrix as a 2D list of INTEGERS where the columns and rows are
# sorted by vertex label. Labels may be provided as strings or integers.
def edge_to_adjacency(edge_list):

    length  = len (edge_list)

    table = []

    for i in range (length):

            first = edge_list[i][0]

            second = edge_list[i][1]

            if(first not in table):

                table.append(first)

            if(second not in table):

                table.append(second)


    table.sort()

    adjMat = [[0 for i in range(len(table))] for j in range (len(table))]

    for j in range(length):

        first = edge_list[j][0]

        second = edge_list[j][1]

        weight = edge_list[j][2]

        first_index = table.index(first)

        second_index = table.index(second)

        adjMat[first_index][second_index] = weight

    return adjMat
    
# ------ DO NOT CHANGE BELOW HERE ------ #
import ast

def main():
    matrix = edge_to_adjacency(ast.literal_eval(input()))

    print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))

if __name__ == "__main__":
    main()
