#Project 2
#Abby Wheaton
#Main program

import random
from BoggleBoard import BoggleBoard

#checks to see if the word given is a palindrome
#it will call the function over and over again with the argument of the string without the first character
#it will then add that first character onto the end
#this reverses the string
#the function will return the reversed string once the string is just one character
def is_palindrome(string):
    if len(string)<= 1:
        return string
    else:
        return is_palindrome(string[1:]) + string[0]

#setting the random seed
seed = int(input("Enter seed: "))
random.seed(seed)

#creating an instance of the board and then filling and printing it
board1 = BoggleBoard()
board1.fill_board()
board1.print_board()

#user will input their word, and it will be sent to the palindrome function
#if the string returned by the palindrome function is the same as the user's string,
#the variable palindrome_flag is set to True, else set to False
word = input("Enter word (in UPPERcase): ")
reverse_string = is_palindrome(word)
if reverse_string == word:
    palindrome_flag =True
else:
    palindrome_flag = False

#This will check to see if the word is on the board
board1.set_word(word)
word_flag =board1.word_on_board()

#outputting the results of checking if the word was on the board and if the word was a palindrome
if word_flag:
    print("Nice job!")
    if palindrome_flag:
        print(f"The word {word} is a palindrome.")
    else:
        print(f"The word {word} is not a palindrome.")
    board1.print_board()
else:
    print("I don't see that word.")
    if palindrome_flag:
        print(f"The word {word} is a palindrome.")
    else:
        print(f"The word {word} is not a palindrome.")
        print("Are we looking at the same board?")




