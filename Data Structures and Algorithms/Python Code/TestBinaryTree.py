#  File: TestBinaryTree.py

#  Description: The purpose of this program is to learn about and
#               implement new functions to the Binary Tree Class

#  Student Name: Michel Gonzalez

#  Student UT EID: Mag9989

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 08/05/2021

#  Date Last Modified 08/05/2021

import sys

class Node (object):

    def __init__ (self, data):

        self.data = data

        self.lChild = None

        self.rChild = None

class Tree (object):

    def __init__ (self):

        self.root = None   

    def insert (self, val):

        newNode = Node (val)

        if (self.root == None):

            self.root = newNode

        else:
            
            current = self.root

            parent = self.root

            while (current != None):

                parent = current

                if (val < current.data):

                    current = current.lChild

                else:

                    current = current.rChild

            if (val < parent.data):

                parent.lChild = newNode

            else:

                parent.rChild = newNode

    # Returns true if two binary trees are similar
    
    def is_similar (self, pNode):

        return self.is_similar_helper (self.root, pNode.root)

    # is_similar_helper does a traverses through the tree recursively

    def is_similar_helper (self, root1, root2):

        # checks if both trees are empty

        if (root1 == None and root2 == None):

            return True

        # checks if only one tree is empty

        elif ((root1 == None and root2 != None) or \
              (root1 != None and root2 == None)):

            return False

        # goes through the tree recursively and compares every node
        # through a brute force method, if the nodes always equal
        # eachother then they are similar and returns True

        else:

            if (root1.data == root2.data):

                return self.is_similar_helper (root1.lChild, root2.lChild) and \
                       self.is_similar_helper (root1.rChild, root2.rChild)

            else:

                return False

    # Returns a list of nodes at a given level from left to right
    
    def get_level (self, level):

        lst = self.get_level_helper (self.root, level, [])

        return lst

    # helper function for the get_level function,
    # gets all the nodes on a given level recursively
    # similarly to the target problems in the recusrsion
    # assigment

    def get_level_helper (self, aNode, level, lst):

        current = aNode

        # if the program has reached an end return the current lst

        if (current == None):

            return lst

        # if the level has been reached
        
        elif (level == 0 and current != None):

            lst.append (current)

        # node with two children

        elif (current.lChild != None and current.rChild != None):

            return self.get_level_helper (current.lChild, level - 1, lst) and \
                   self.get_level_helper (current.rChild, level - 1, lst)

        # node with right child

        elif (current.lChild == None and current.rChild != None):

            return self.get_level_helper (current.rChild, level - 1, lst)

        # node with left child

        elif (current.lChild != None and current.rChild == None):

            return self.get_level_helper (current.lChild, level - 1, lst)

        # node is a leaf node, gets the next child value None and returns
        # the list in the next recursive call

        else:

            return self.get_level_helper (current.lChild, level - 1, lst)

        return lst

    # Returns the height of the tree
    
    def get_height (self):

        return self.get_height_helper (self.root)

    # helper function for get_height function

    def get_height_helper (self, aNode):

        # The fucntion goes through the tree recursively by comparing
        # the heights of the left and right subtrees and begins comparing at
        # the leafs of the tree

        current = aNode

        # checks if the tree is empty (base case)

        if (current == None):

            return 0

        # gets the height of the left sub tree and
        # the right sub tree

        else:

            lHeight = self.get_height_helper (current.lChild)

            rHeight = self.get_height_helper (current.rChild)

            # returns the largest sub tree

            if (lHeight > rHeight):

                return lHeight + 1

            else:

                return rHeight + 1

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    
    def num_nodes (self):

        root = self.root

        if (root == None):

            return 0

        else:

            # root of the left sub tree

            left_root = root.lChild

            # root of the right sub tree

            right_root = root.rChild

            # gets a list of the nodes in the left

            lLst = self.num_nodes_helper (left_root, [])

            # gets a list of the nodes in the right

            rLst = self.num_nodes_helper (right_root, [])

            # add the root to the total value

            return len(lLst) + len(rLst) + 1

    # goes through each sub trees and makes a list of all
    # of the nodes

    def num_nodes_helper (self, aNode, lst):

        current = aNode

        # goes through the tree in order and
        # creates a list

        if (current != None):

           self.num_nodes_helper (current.lChild, lst)
           
           lst.append(current)

           self.num_nodes_helper (current.rChild, lst)

        return lst
   
def main():

    # Create three trees - two are the same and the third is different

    line = sys.stdin.readline()

    line = line.strip()

    line = line.split()

    tree1_input = list (map (int, line))    # converts elements into ints

    line = sys.stdin.readline()

    line = line.strip()

    line = line.split()

    tree2_input = list (map (int, line))    # converts elements into ints

    line = sys.stdin.readline()

    line = line.strip()

    line = line.split()

    tree3_input = list (map (int, line))    # converts elements into ints

    # Create Tree Objects

    tree1 = Tree()

    tree2 = Tree()

    tree3 = Tree()

    # insert data into each tree

    for i in tree1_input:

        tree1.insert (i)

    for i in tree2_input:

        tree2.insert (i)

    for i in tree3_input:

        tree3.insert (i)

    # Test your method is_similar()

    print(tree1.is_similar(tree3))

    print(tree1.is_similar(tree2))

    # Print the various levels of two of the trees that are different

    print(tree1.get_level (0))

    print(tree1.get_level (1))

    print(tree1.get_level (2))

    print(tree1.get_level (3))

    # Get the height of the two trees that are different

    print(tree1.get_height())

    print(tree3.get_height())

    # Get the total number of nodes a binary search tree

    print(tree1.num_nodes())

    print(tree3.num_nodes())

if __name__ == "__main__":

    main()
