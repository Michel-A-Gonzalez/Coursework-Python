#  File: Boxes.py

#  Description: This program comapres n boxes of different dimensions and
#               returns the largest amount of boxes that fit in eachother
#               and also returns the number of different sets with the largest
#               number of boxes

#  Student Name: Michel Gonzalez

#  Student UT EID: Mag9989

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 07/06/2021

#  Date Last Modified: 07/06/2021

import sys

# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes

def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):

    # This function is preformed through recursion and gathers all sub sets
    # of the given list of boxes

    # Base case of the recursive problem
    
    if (idx >= len(box_list)):

        all_box_subsets.append(sub_set)

        return

    
    # Assignes and creates a new list with all the previous elements in the
    # sub set list and preformes a recursive call to the fucntion with the new
    # sub set and the old sub set
    
    else:

        current_sub = sub_set[:]

        sub_set.append(box_list[idx])

        sub_sets_boxes (box_list, sub_set, idx + 1, all_box_subsets)

        sub_sets_boxes (box_list, current_sub, idx + 1, all_box_subsets)

    return all_box_subsets

# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is

def largest_nesting_subsets (all_box_subsets, largest_size, all_nesting_boxes):
    
    # Uses a for loop to iterate through all the sub sets of boxesin the 3-D list
    
    for i in range(0, len(all_box_subsets)):

        j = 0

        k = 1

        # Uses a while loop since this method pops of any box that doesn't fit
        # in the previous box, it also uses the given function does_fit which
        # checks the current box is smaller than the next box. This method assumes
        # that the 3-D list is sorted 

        while j < len(all_box_subsets[i]):

            # If the next box doesn't fit in the current box then it is poped off
            # from the 3-D list and keeps all boxes that nest

            if (k < len(all_box_subsets[i]) and \
                does_fit (all_box_subsets[i][j], all_box_subsets[i][k]) == False):

                all_box_subsets[i].pop(k)

            else:

                k += 1

                j += 1

    # Iterates through the modified 3-D list and keeps all unique nested sub sets in
    # the list all_nesting_boxes

    for i in range(0, len(all_box_subsets)):

        if(all_box_subsets[i] not in all_nesting_boxes):

            all_nesting_boxes.append(all_box_subsets[i])

        else:

            continue

    # Finds the largest number of nested boxes from the list all_nesting_boxes

    for i in range(0, len(all_nesting_boxes)):

        large = len(all_nesting_boxes[i])

        if (large > largest_size):

            largest_size = large

    # I appended the largest value to the end of the 3-D list all_nesting_boxes
    # to print it later

    all_nesting_boxes.append(largest_size)

    return all_nesting_boxes

# returns True if box1 fits inside box2

def does_fit (box1, box2):

    return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
# read the number of boxes

    line = sys.stdin.readline()

    line = line.strip()

    num_boxes = int (line)

# create an empty list for the boxes
    box_list = []

# read the boxes from the file
    for i in range (num_boxes):

        line = sys.stdin.readline()

        line = line.strip()

        box = line.split()
        
        for j in range (len(box)):
        
            box[j] = int (box[j])

        box.sort()
        
        box_list.append (box)

# sort the box list
    box_list.sort()

# create an empty list to hold all subset of boxes
    all_box_subsets = []

# create a list to hold a single subset of boxes
    sub_set = []

# generate all subsets of boxes and store them in all_box_subsets
    sub_sets_boxes (box_list, sub_set, 0, all_box_subsets)

# all_box_subsets should have a length of 2^n where n is the number
# of boxes

# go through all the subset of boxes and only store the
# largest subsets that nest in all_nesting_boxes
    all_nesting_boxes = largest_nesting_subsets (all_box_subsets, 0, [])

# print the largest number of boxes that fit

    # gets the largest number of nested boxes and prints it

    largest_size = all_nesting_boxes[len(all_nesting_boxes) - 1]

    print(largest_size)

# print the number of sets of such boxes

    # Counts the number of nested boxes that are the largest nested boxes

    count = 0

    for i in range(0, len(all_nesting_boxes) - 1):

        if (len(all_nesting_boxes[i]) == largest_size):

            count += 1

        else:

            continue

    print(count)

if __name__ == "__main__":
  main()
