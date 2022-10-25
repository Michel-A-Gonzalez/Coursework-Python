#   File: Josephus.py

#   Description:

#   Student Name: Michel Gonzalez

#   Student UT EID: Mag9989

#   Course Name: CS 313E

#   Unique Number: 86610

#   Date Created: 07/29/21

#   Date Last Modified: 07/29/21

import sys

class Link(object):

    # creates the Link object with data and a next link fucntion

    def __init__ (self, data, next = None):

        self.data = data

        self.next = next


class CircularList(object):
    
    # Constructor
    
    def __init__ ( self ):

      self.first = None

      
    # Insert an element (value) in the list

    # used the insert last mehtod to construct
    # the linked list
    
    def insert ( self, data ):

        new_link = Link (data)

        current = self.first

        if (current == None):

            self.first = new_link

            return

        while (current.next != None):

            current = current.next

        current.next = new_link

        return

    # Find the Link with the given data (value)
    # or return None if the data is not there

    # used the find method from the singly linked
    # list program
    
    def find ( self, data ):

        current = self.first

        if (current == None):

            return None

        while (current.data != data):

            if(current.next == None):

                return None

            else:

                current = current.next

        return current

    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there

    # used the delete method from the singly linked
    # list program
    
    def delete ( self, data ):

        previous = self.first

        current = self.first

        if (current == None):

            return None
        
        while (current.data != data):

            if (current.next == None):

                return None

            else:

                previous = current

                current = current.next

        if (current == self.first):

            self.first = self.first.next

        else:

            previous.next = current.next

        return current

    # Added a helper function and gets the
    # numebr of links in the linked list

    def get_num_links (self):

        count = 0

        current = self.first

        if (current == None):

            return count

        while (current != None):

            count += 1

            current = current.next

        return count

    # Delete the nth Link starting from the Link start 
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order

    # This fucntion allows the linked list to become circular by
    # having the last link connect to the first
    
    def delete_after ( self, start, n ):

        current = self.find(start)

        # the fuction will run until one link is left
        # which is the survivor

        while (self.get_num_links() != 1):

            i = 1

            while i <= n:

                # quick check to see if the list has been
                # reduced to the last number

                if(self.get_num_links() == 1):

                    break

                # 'i' is used as a dummy variable to allow
                # the program to go to the nth link and
                # deletes it

                elif (i == n):
                
                    i = 1
                
                    deleted_num = self.delete(current.data).data

                    # connects the last link to the first

                    if(current.next == None):

                        current = self.first

                    else:

                        current = current.next

                    print(deleted_num)

                else:

                    # connects the last link to the first

                    if(current.next == None):

                        current = self.first

                        i += 1

                    else:

                        current = current.next

                        i += 1


        # once the linked list has been reduce it returns the survivor

        return self.first.data

    # Return a string rqepresentation of a Circular List
    # The format of the string will be the same as the __str__ 
    # format for normal Python lists
    def __str__ ( self ):

        # returns a list representation of the
        # linked list

        lst = []

        current = self.first

        num = 0

        if (current == None):

            return str(lst)

        while (current != None):

            lst.append(current.data)

            current = current.next

        return str(lst)

def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int (line)
  
    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int (line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int (line)

    # your code

    soldiers = []

    # creates a list of the data that will be
    # used in the linked list

    for i in range(1, num_soldiers + 1):

        soldiers.append(i)

    linked_soldiers = CircularList()

    # inserts the data from the list to the
    # linked list

    for i in range(0, len(soldiers)):

        linked_soldiers.insert(soldiers[i])

    print(linked_soldiers.delete_after(start_count, elim_num))

if __name__ == "__main__":
    main()

