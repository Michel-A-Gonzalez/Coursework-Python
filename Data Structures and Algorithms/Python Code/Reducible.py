#  File: Reducible.py

#  Description: This program will run through an entier list of
#               valid English words and return a list of the
#               longest reducable words in the list

#  Student Name: Michel Gonzalez

#  Student UT EID: MAG9989

#  Course Name: CS 313E

#  Unique Number: 86601

#  Date Created: 07/12/2021

#  Date Last Modified: 07/12/2021

import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise

# This fucntion was provided in the skeleton of the code

def is_prime (n):

    if (n == 1):
        
        return False

    limit = int (n ** 0.5) + 1
    
    div = 2
    
    while (div < limit):
        
        if (n % div == 0):
            
          return False
        
        div += 1
        
    return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into

# This fucntion was provided in the skeletone of the code

def hash_word (s, size):
    
    hash_idx = 0
  
    for j in range (len(s)):

        letter = ord (s[j]) - 96
    
        hash_idx = (hash_idx * 26 + letter) % size
	
    return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string

# finds the step size by double hashing mehtod

def step_size (s, const):

    # num_string is an int varible that is changed to resemble
    # a unique number depending on the string by using
    # string hashing mehtods with double hashing

    num_string = 0


    # I used the starting exponent to be zero to reduce strain
    # of large numbers and instead it will create still unique
    # but small numbers (largest number will be 26.xxx)

    # num_string is the number representation of the given string
    
    expo = 0

    for i in range(0, len(s)):

        letter = ord(s[i]) - 96

        # double hashing methode

        num_string += letter * (26 ** (expo - i))

    step = const - (num_string % const)

    return int(step) 

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):

    # gets the inital index for a certian word

    idx = hash_word (s, len(hash_table))

    # Checks if the slot is avalable and if so
    # it inserts the string

    if (hash_table[idx] == ''):

        hash_table[idx] =  s

    # if the slot is full then the algorithm will
    # move and check the next slot by adding a constant
    # step to the current index

    else:

        # If the algorithm finds an empty slot it will insert
        # at that index

        step = step_size(s, len(hash_table))

        while (hash_table[idx] != ''):

            idx = idx + step

            # If the index is larger than the table
            # it loops the index

            if (idx >= len(hash_table)):

                idx = idx - (len(hash_table))

            else:

                continue

        hash_table[idx] = s

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):

    # gets the index of the unique word and does an
    # inital check

    index = hash_word (s, len(hash_table))

    if(hash_table[index] == s):

        return True

    # if it is not at the inital index it checks other
    # slots through the double hashing method step size

    else:

        step = step_size(s, len(hash_table))

        while (hash_table[index] != ''):

            index = index + step

            if(index >= len(hash_table)):

                index = index - (len(hash_table))

            # if it finds the word it returns True
            # but if it ever hits an empty slot then that
            # word is not in the hash_table

            if(hash_table[index] == s):

                return True

            else:

                continue

        return False

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):

    # does an inital check if the current word was found
    # to be reducible before through other words

    if (find_word (s, hash_memo)):
        
        return True

    # once the word is reduced to a single letter it
    # checks if it is an accpetable word

    elif (len(s) == 1):

        return s == 'a' or s == 'i' or s == 'o'

    else:

        # the for loop allows to check every word that
        # comes out of removing a single character
        
        for i in range(0, len(s)):

            s_lst = list(s)

            s_lst.pop(i)

            s2 = ''.join(s_lst)

            if (find_word (s2, hash_table)):

                if(is_reducible (s2, hash_table, hash_memo)):

                    # if the word is reducible then it adds it to
                    # the hash_memo and the sub_word

                    if not (find_word (s2, hash_memo)):

                            insert_word (s2, hash_memo)

                    if not (find_word (s, hash_memo)):

                            insert_word (s, hash_memo)
                            
                    return True

                # if the word did excist but is not reducible then
                # the original word is recreated

                else:

                    s2 = list(s)
                
            else:

                s2 = list(s)

        return False

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):

    longest = 0

    current_length = 0

    # gets the longest length in the list of
    # reducible words

    for i in range(0, len(string_list)):

        current_length = len(string_list[i])

        if (current_length > longest):

            longest = current_length

        else:

            continue

    # gets rid of all the strings that are not the longest
    # reducible words
    
    j = 0

    while j < len(string_list):

        if(len(string_list[j]) < longest):

            string_list.pop(j)

        else:

            j += 1

    return string_list

def main():

    # create an empty word_list

    word_list = []

    # read words from words.txt and append to word_list

    word_list.append('a')

    word_list.append('i')

    word_list.append('o')

    # adds the words 'a', 'i', and 'o' for validity
    # checking purposes then sorts the word_list 
    
    for line in sys.stdin:
        
        line = line.strip()
        
        word_list.append (line)

    word_list.sort()
           
    # find length of word_list

    length = len(word_list)

    # determine prime number N that is greater than twice
    # the length of the word_list

    n = 2 * length

    while (is_prime (n) != True):

        n += 1
        
    # create an empty hash_list
    # populate the hash_list with N blank strings

    hash_list = ['' for i in range(0, n)]

    # hash each word in word_list into hash_list
    # for collisions use double hashing

    for i in range(0, length):

        insert_word (word_list[i], hash_list)

    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than 
    # 0.2 * size of word_list

    size_m = int(0.2 * length)

    while (is_prime (size_m) != True):

        size_m += 1

    # populate the hash_memo with M blank strings

    hash_memo = ['' for i in range(0, size_m)]

    # create an empty list reducible_words

    reducible_words = []

    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    # as you recursively remove one letter at a time check
    # first if the sub-word exists in the hash_memo. if it does
    # then the word is reducible and you do not have to test
    # any further. add the word to the hash_memo.

    for i in range(0, length):

        if(is_reducible (word_list[i], hash_list, hash_memo)):

            reducible_words.append(word_list[i])

        else:

            continue

    # find the largest reducible words in reducible_words

    get_longest_words (reducible_words)

    # print the reducible words in alphabetical order
    # one word per line

    reducible_words.sort()

    for i in reducible_words:

        print(i)

if __name__ == "__main__":
  main()
