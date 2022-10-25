#  File: Cipher.py

#  Description: The purpose of this program is to take a given string
#               and ecnrypting it or decrypting it by creating a square
#               matrix using a 2-D list, and then rotating the stirng
#               90 degrees clockwise or 90 degrees counter clockwise
#               respectably

#  Student Name: Michel Gonzalez

#  Student UT EID: MAG9989

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 06/16/2021

#  Date Last Modified: 06/16/2021

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string

def encrypt ( strng ):                                                                  

    if(1 <= len(strng) <= 100):                                                         # This portion of the program encrypts a given string 
                                                                                        # by creating a square matrix made from a 2-D list and
        import math                                                                     # rotates the elements of the square matrix clockwise
                                                                                        # by 90 degrees
        l_len = len(strng)

        m_len = l_len

        while(math.sqrt(m_len) % 1 != 0):                                               # Gets the closest square value from the length of the
                                                                                        # given string and uses the diffenrece of M and L
            m_len += 1                                                                  # to attach asteriks at the end of the string
            
        num_astrix = (m_len - l_len)

        strng = strng + ('*' * num_astrix)

        dimension = int(math.sqrt(m_len))                                               # Gets the dimensions of the matrix

        string_list = [[0 for i in range(0, dimension)] for j in range(0, dimension)]   # Creates the matrix

        for i in range(dimension - 1, -1, -1):                                          # Assignes the 2-D list a 90 degree rotated version of 
                                                                                        # the given string (Astrikes are also rotated)
            for j in range(0, dimension):

                string_list[j][i] = strng[j]

            strng = strng[dimension:]                                                   # Shortens the string by the value of the dimension
                                                                                        
        string_list = [''.join(i) for i in string_list]                                 # Creates the new encrypted string and removes any astrixs
                                                                                        # in the string
        string_list = ''.join(string_list)

        string_list = string_list.replace('*', '')

        return string_list
    
    else:

        return 0

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string

def decrypt ( strng ):

    if(1 <= len(strng) <= 100):                                                         # This portion of the program decrypts a given string by
                                                                                        # applying similar functions as the encryption portion
        import math                                                                     # except it rotates the matrix counterclock-wise by 90 degrees
        
        l_len = len(strng)

        m_len = l_len

        while(math.sqrt(m_len) % 1 != 0):                                               # Same as method to get the nearest square from the length

            m_len += 1

        strng = strng + ('*' *(m_len - l_len))

        dimension = int(math.sqrt(m_len))

        strng_copy = strng                                                              # Creates a copy of the original string since both will be needed

        string_list = [[0 for i in range(0, dimension)] for j in range(0, dimension)]   # Creates a non-rotated matrix with each element filled with
                                                                                        # characters from the given string
        for i in range(0, dimension):                                                    

            for j in range(0, dimension):

                string_list[i][j] = strng_copy[j]

            strng_copy = strng_copy[dimension:]                                         # Modifies the copy of the string for the non-rotated matrix
                                                                                        
        for i in range(0, dimension):                                                   # This portion rotates the non-rotated matrix counterclock-wise
                                                                                        # by 90 degrees, however it does not rotate any asteriks
            k = 0                                                                       # Variable k is used to keep track of the position in the string
                                                                                        # that the previous colounm left off on
            for j in range(dimension - 1, -1 , -1):

                if(string_list[j][i] != '*'):                                           # Checks for an astrix and skips it if there is one

                    if(strng[k] == '*'):                                                # Used to check if all characters in the string have been palced
                                                                                        # in the matrix since the ending values may be astrix if the
                        break                                                           # original length was not a square value

                    else:

                        string_list[j][i] = strng[k]

                        k += 1                                                     

                else:

                    continue

            strng = strng[k: ]                                                          # Takes off the letters that have been already assgined

        string_list = [''.join(i) for i in string_list]                                 # Creates the decrypted string and returns it

        string_list = ''.join(string_list)

        string_list = string_list.replace('*', '')

        return string_list                                                              # Note* both the matrices in the encryption and decryption fucntions 
                                                                                        # were created column by column rather than row by row, since the
    else:                                                                               # horizontal strings were turned into a verticle postion

        return 0
def main():

    import sys

    in_file = sys.stdin.readlines()                                                     # Acces the file and assignes each string in the file
                                                                                        # to the correct function that the string needs to go through
    str_p = in_file[0]                                                                  # Also, gets rid of extra characters in each string

    str_p = str_p.replace('\n', '') 

    str_p = str_p.strip()

    str_q = in_file[1]

    str_q = str_q.replace('\n', '')

    str_q = str_q.strip()

    encrypted_p = encrypt(str_p)

    print(encrypted_p)                                                                  # Prints the encrypted message and the decrypted message

    decrypted_q = decrypt(str_q)

    print(decrypted_q)

if __name__ == "__main__":
  main()
