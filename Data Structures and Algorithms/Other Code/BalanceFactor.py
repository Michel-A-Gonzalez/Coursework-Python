#  File: BalanceFactor.py

#  Description: Determines the balance factor of a binary tree

#  Student Name: Michel Gonzalez

#  Student UT EID: Mag9989

#  Course Name: CS 313E

#  Unique Number: 86610

class Node (object):
  def __init__ (self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

# Return the integer balance factor of a tree rooted at the given node.    
def balance_factor(node):

  left = node.left

  right = node.right

  height_left_tree = balance_factor_helper (left)

  height_right_tree = balance_factor_helper (right)

  return height_right_tree - height_left_tree

def balance_factor_helper (node):

  root = node

  if (root == None):

    return 0

  lheight = balance_factor_helper (node.left)

  rheight = balance_factor_helper (node.right)

  if (rheight > lheight):

    return rheight + 1

  else:

    return lheight + 1   

# ------ DO NOT CHANGE BELOW HERE ------ #
import pickle
import sys

def main():
    data_in = ''.join(sys.stdin.readlines())
    node = pickle.loads(str.encode(data_in))

    print(balance_factor(node))

if __name__ == "__main__":
    main()
