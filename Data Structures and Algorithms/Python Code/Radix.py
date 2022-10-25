#  File: Radix.py

#  Description: This program sorts a list of given numbers in decending
#               oreder by using queues as the sorting machenism based on
#               the decimal place and the value of the number at that palce

#  Student Name: Michel Gonzalez

#  Student UT EID: Mag9989

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 07/16/2021

#  Date Last Modified: 07/18/2021

import sys

class Queue (object):
    
    def __init__ (self):

        self.queue = []

  # add an item to the end of the queue
    def enqueue (self, item):

      self.queue.append (item)

  # remove an item from the beginning of the queue
    def dequeue (self):
      
        return (self.queue.pop(0))

  # check if the queue if empty
    def is_empty (self):

        return (len(self.queue) == 0)

  # return the size of the queue
    def size (self):

        return (len(self.queue))

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):

    # Creates 38 Queue objects

    queues = [Queue() for i in range(0,38)]

    # Gets the number of passes n needed to sort the list

    length  = len(max(a, key = len))

    for i in range(0, len(a)):

        # Makes all string the same length but adds a
        # space characters to the end of the string

        if(len(a[i]) < length):

            a[i] = a[i] + (' ' * (length - len(a[i])))

    # Puts the list into the out Queue

    for i in range(0, len(a)):

        queues[37].enqueue(a[i])

    queues_dic = {
                 ' ' : queues[0],
                 '0' : queues[1],
                 '1' : queues[2],
                 '2' : queues[3],
                 '3' : queues[4],
                 '4' : queues[5],
                 '5' : queues[6],
                 '6' : queues[7],
                 '7' : queues[8],
                 '8' : queues[9],
                 '9' : queues[10],
                 'a' : queues[11],
                 'b' : queues[12],
                 'c' : queues[13],
                 'd' : queues[14],
                 'e' : queues[15],
                 'f' : queues[16],
                 'g' : queues[17],
                 'h' : queues[18],
                 'i' : queues[19],
                 'j' : queues[20],
                 'k' : queues[21],
                 'l' : queues[22],
                 'm' : queues[23],
                 'n' : queues[24],
                 'o' : queues[25],
                 'p' : queues[26],
                 'q' : queues[27],
                 'r' : queues[28],
                 's' : queues[29],
                 't' : queues[30],
                 'u' : queues[31],
                 'v' : queues[32],
                 'w' : queues[33],
                 'x' : queues[34],
                 'y' : queues[35],
                 'z' : queues[36],
                }
    # Runs through the list n times and sorts it through
    # radix sort

    for i in range(length - 1, -1, -1):

        # enqueues and dequeues strings to the appropriate
        # queue object, an additional queue is used for the
        # spaces added to match the lengths needed

        while not (queues[37].is_empty()):

            q_value = queues[37].dequeue()

            queues_dic[q_value[i]].enqueue(q_value)

        for j in range(0, 37):

            while not(queues[j].is_empty()):

                q_value_2 = queues[j].dequeue()

                queues[37].enqueue(q_value_2)

    sorted_lst = []

    # dequeues the out queue into a list

    while not  (queues[37].is_empty()):

        sorted_lst.append(queues[37].dequeue())

    # gets rid of the spaces

    for i in range (0, len(sorted_lst)):

        sorted_lst[i] = sorted_lst[i].strip()

    # returns the radix sorted list

    return sorted_lst

def main():
  # read the number of words in file
    line = sys.stdin.readline()

    line = line.strip()

    num_words = int (line)

  # create a word list
    word_list = []

    for i in range (num_words):

        line = sys.stdin.readline()

        word = line.strip()

        word_list.append (word)

  # use radix sort to sort the word_list

    sorted_list = radix_sort (word_list)

  # print the sorted_list

    print (sorted_list)

if __name__ == "__main__":

    main()

