class Link (object):

    def __init__ (self, data, next = None):

        self.data = data

        self.next = next
    
class LinkedList (object):
    # create a linked list
    # you may add other attributes
    def __init__ (self):
        
        self.first = None

    # get number of links 
    def get_num_links (self):

        count = 0

        current = self.first

        if (current == None):

            return count

        while (current != None):

            count += 1

            current = current.next

        return count
  
    # add an item at the beginning of the list
    def insert_first (self, data):

        new_link = Link (data)

        new_link.next = self.first

        self.first = new_link

    # add an item at the end of a list
    def insert_last (self, data):

        new_link = Link (data)

        current = self.first

        if (current == None):

            self.first = new_link

            return

        while (current.next != None):

            current = current.next

        current.next = new_link

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order (self, data):

        new_link = Link (data)

        previous = self.first

        current = self.first

        if (current == None or data < current.data):

            self.insert_first (data)

            return

        while (current != None):

            if (previous.data < data and current.data >= data):

                new_link.next = current

                previous.next = new_link

                return

            else:

                previous = current 

                current = current.next

        self.insert_last(new_link.data)

        return

    # search in an unordered list, return None if not found
    def find_unordered (self, data):

        current = self.first

        if (current == None):

            return None

        while (current.data != data):

            if(current.next == None):

                return None

            else:

                current = current.next

        return current

    # Search in an ordered list, return None if not found
    def find_ordered (self, data):

        current = self.first

        if (current == None):

            return None

        while (current.data != data):

            if(current.next == None):

                return None

            else:

                current = current.next

        return current

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link (self, data):

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

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):

        current = self.first

        num = 0

        if (current == None):

            return ''

        while (current != None):

            if (num == 9):

                print(str(current.data), end = '\n')

                num = 0

                current = current.next

            elif(current.next == None):

                print(str(current.data), end = '\n')

                break

            else:
    
                print(str(current.data), end = '  ')

                num += 1

                current = current.next

        return ''

    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list (self):

        copy_list = LinkedList()

        current = self.first

        if (current == None):

            return copy_list

        while (current != None):

            copy_list.insert_last (current.data)

            current = current.next

        return copy_list

    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list (self):

        reverse_list = LinkedList()

        if(self.first == None):

            return None

        current = self.first

        if (current == None):

            return None

        while (current != None):

            reverse_list.insert_first (current.data)

            current = current.next

        return reverse_list
    
    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list (self):

        sorted_lst = LinkedList()

        current = self.first

        if(current == None):

            return None

        while (current != None):

            sorted_lst.insert_in_order (current.data)

            current = current.next

        sorted_lst.delete_link(self.first)

        return sorted_lst

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):

        current = self.first

        if(current == None):

            return True

        while (current.next != None):

            if(current.data > current.next.data):

                return False

            else:

                current = current.next

        return True

    # Return True if a list is empty or False otherwise
    def is_empty (self):

        current = self.first

        return (current == None)

    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list (self, other):

        merged_list = LinkedList()

        reverse_self = self.reverse_list()

        current_1 = reverse_self.first

        current_2 = other.first

        while (current_1 != None):

            merged_list.insert_first(current_1.data)

            current_1 = current_1.next

        while (current_2 != None):

            merged_list.insert_last(current_2.data)

            current_2 = current_2.next

        merge = merged_list.sort_list()

        return merge

    # Test if two lists are equal, item by item and return True
    def is_equal (self, other):

        current_1 = self.first

        current_2 = other.first

        if (self.is_empty() == True and other.is_empty() == True):

            return True
        
        elif (self.is_empty() == True and other.is_empty() == False):

            return False

        elif (self.is_empty() == False and other.is_empty() == True):

            return False

        while (current_1.next != None and current_2.next != None):

            if (current_1.data != current_2.data):

                return False

            else:

                current_1 = current_1.next

                current_2 = current_2.next

        return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates (self):

        no_dups = LinkedList()

        current = self.first

        while (current != None):

            if (no_dups.find_unordered(current.data) == None):

                no_dups.insert_last(current.data)

                current = current.next

            else:

                current = current.next
            
        return no_dups
def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.

    links = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

    linked_list = LinkedList()

    for i in range(0, len(links)):

        linked_list.insert_last(links[i])

    print(linked_list)

    links5 = [5,18]

    l = LinkedList()

    for i in range(0, len(links5)):

        l.insert_last(links5[i])

    print(l)

    # Test method insert_last()

    linked_list.insert_last(11)

    print(linked_list)

    # Test method insert_in_order()

    links2 = [1,2,3,4,6,7,8,9]

    linked_list2 = LinkedList()

    for i in range (0, len(links2)):

        linked_list2.insert_last(links2[i])

    print(linked_list2)

    linked_list2.insert_in_order(0)

    linked_list2.insert_in_order(5)

    linked_list2.insert_in_order(10)

    print(linked_list2)

    # Test method get_num_links()

    num = linked_list2.get_num_links()

    print(num)

    # Test method find_unordered() 
    # Consider two cases - data is there, data is not there

    not_there = linked_list.find_unordered(99)

    there = linked_list.find_unordered(1)

    print(not_there, there.data)

    # Test method find_ordered() 
    # Consider two cases - data is there, data is not there

    not_there2 = linked_list2.find_ordered(99)

    there2 = linked_list2.find_ordered(2)

    print(not_there2, there2.data)

    # Test method delete_link()
    # Consider two cases - data is there, data is not there

    not_there = linked_list.delete_link(99)

    there = linked_list.delete_link(3)

    print(not_there, there.data)

    # Test method copy_list
    empty = LinkedList()

    copy2 = empty.copy_list()

    print(copy2)

    copy = linked_list.copy_list()

    print(copy)

    # Test method reverse_list()

    reverse = linked_list.reverse_list()

    print(reverse)

    # Test method sort_list()

    sorted_lst = linked_list.sort_list()

    print(sorted_lst)

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted

    print(sorted_lst.is_sorted())

    print(linked_list.is_sorted())

    # Test method is_empty()

    linked_list3 = LinkedList()

    print(linked_list3.is_empty())

    print(linked_list.is_empty())

    # Test method merge_list()

    a = [1,3,5,7]

    l_a = LinkedList()

    b = [2,4,6,8]

    l_b = LinkedList()

    for i in a:

        l_a.insert_last(i)

    for i in b:

        l_b.insert_last(i)

    merge = l_a.merge_list(l_b)

    print(merge)

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal

    c = [1,2,3,4]

    l_c = LinkedList()

    for i in c:

        l_c.insert_last(i)

    print(l_a.is_equal(l_c))

    print(l_a.is_equal(l_b))

    # Test remove_duplicates()

    d = [1,1,1,2,2,3,3,3,4,4,4,5]

    l_d = LinkedList()

    for i in d:

        l_d.insert_last(i)

    no_dups = l_d.remove_duplicates()

    print(no_dups)

if __name__ == "__main__":
    
    main()
