# File: Project2.py
# Student: Michel Gonzalez
# UT EID: Mag9989
# Course Name: CS303E
# 
# Date Created: 04-10-2021
# Date Last Modified: 04-11-2021
# Description of Program: The purpose of this program is to encrypt
# a given message and decrypt a given encrypted message. The program
# has five different commands that are given in the input message


import random

lcletters = "abcdefghijklmnopqrstuvwxyz"

def isLegalKey(key):                    # Checks if a key is legal or not

    if(len(key) == 26):

        for ch in key:

            if(ch in lcletters):

                return True
            
            else:

                return False  
    else:

        return False
    
def makeRandomKey():                    # Creates a random key

    lst = list(lcletters)

    random.shuffle(lst)

    return "".join(lst)
    
class SubstitutionCipher:               

    def __init__(self, key = makeRandomKey()):      # Defines the class object

        if(isLegalKey(key) == True):

            self.__key = key
        
        else:

            print("Key entered is not legal")

            return

    def getKey(self):                               # Returns the current key in the program

        return self.__key

    def setKey(self, newKey):                       # This sets the key 

        self.__key = newKey

        if(isLegalKey(self.__key) == True):

            return self.__key

        elif(newKey == "random"):

            self.__key = makeRandomKey()

            return self.__key
        
        else:

            return "Key entered is not legal"
        
    def encryptText(self, plaintext):               # This encrypts a given decrypted message

        self.__plaintext = list(plaintext)

        for i in range(0, len(self.__plaintext)):

            if(self.__plaintext[i].isupper() == True):  # Checks for any uppercase letters

                if(ord(self.__plaintext[i]) < 65 or ord(self.__plaintext[i]) > 90):

                    continue
                
                else:

                    textLetter = self.__plaintext[i]    # Gets the ith letter in the message

                    lclettersCap = lcletters.upper()    # Capitalizes the aplhpabet letters int

                    self.__keyCap = self.__key.upper()  # Capitalizes the key

                    lclettersPosition = lclettersCap.find(textLetter)       # Finds the index position of a
                                                                            # specific letter in the aplphabet
                    self.__plaintext[i] = self.__keyCap[lclettersPosition]  # Replaces the specific letter with the
                                                                            # correct letter in the key 
            else:

                if(ord(self.__plaintext[i]) < 97 or ord(self.__plaintext[i]) > 122):

                    continue

                else:

                    textLetter = self.__plaintext[i]                # Same process except for lower cases letters

                    lclettersPosition = lcletters.find(textLetter)

                    self.__plaintext[i] = self.__key[lclettersPosition]

        return "".join(self.__plaintext)

            
               
    def decryptText(self, ciphertext):          # this behaves the same however it takes in an
                                                # encrypted message and decrypts it
        self.__ciphertext = list(ciphertext)

        for i in range(0, len(self.__ciphertext)):

            if(self.__ciphertext[i].isupper() == True):

                if(ord(self.__ciphertext[i]) < 65 or ord(self.__ciphertext[i]) > 90):

                    continue
                
                else:

                    textLetter = self.__ciphertext[i]

                    lclettersCap = lcletters.upper()

                    self.__keyCap = self.__key.upper()

                    keyPosition = self.__keyCap.find(textLetter)

                    self.__ciphertext[i] = lclettersCap[keyPosition]

            else:

                if(ord(self.__ciphertext[i]) < 97 or ord(self.__ciphertext[i]) > 122):

                    continue

                else:

                    textLetter = self.__ciphertext[i]

                    keyPosition = self.__key.find(textLetter)

                    self.__ciphertext[i] = lcletters[keyPosition]

        return "".join(self.__ciphertext)

def main():                                         # Main function that creates both the prompt and command lines
                                                    # that allows a user to input and create messages to encrypt or
                                                    # decrypt them. A quit function is in place to end the program.
   cipher = SubstitutionCipher()

   command = input("Enter a command (getKey, changeKey, encrypt, decrypt, quit): ")

   while (command != "quit"):

       command = command.lower()

       if("k" in command):

           command = command.replace("k", "K")

       if (command == "getKey"):

           k = cipher.getKey()

           print("  Current cipher key: ", k)
           
           command = input("Enter a command (getKey, changeKey, encrypt, decrypt, quit): ")

       elif (command == "changeKey"):

            newKey = input("  Enter valid cipher key, 'random' for a random key, or 'quit' to quit: ")

            while(newKey != "quit"):

                if (newKey == "random"):

                    newKey = cipher.setKey(newKey)

                    print("    New cipher key: ", newKey)

                    break

                if(isLegalKey(newKey) != True):

                    while(isLegalKey(newKey) != True):

                        print("    Illegal key entered. Try again!")

                        newKey = input("  Enter valid cipher key, 'random' for a random key, or 'quit' to quit: ")

                        if(newKey == "quit"):

                            break
                        
                        else:

                            continue

                elif (isLegalKey(newKey) == True):

                    print("    New cipher key: ", newKey)

                    break
                
            if(newKey == "quit"):

                command = input("Enter a command (getKey, changeKey, encrypt, decrypt, quit): ")
                        
       elif (command == "encrypt"):

            text = input("  Enter a text to encrypt: ")

            text2 = cipher.encryptText(text)

            print("    The encrypted test is: ", text2)

            command = input("Enter a command (getKey, changeKey, encrypt, decrypt, quit): ")

       elif (command == "decrypt"):

            text = input("  Enter a text to decrypt: ")

            text2 = cipher.decryptText(text)

            print("    The decrypted text is: ", text2)

            command = input("Enter a command (getKey, changeKey, encrypt, decrypt, quit): ")

       elif (command != "getKey" or command != "changeKey" or command != "encrypt" or command != " decrypt"):

            print("  Command not recognized. Try again!")

            command = input("Enter a command (getKey, changeKey, encrypt, decrypt, quit): ")

   if (command == "quit"):

        print("Thanks for visiting!")

        return

main()
                    

        

    

        
                                        

        

    
