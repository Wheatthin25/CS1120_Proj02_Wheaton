#Project 2
#Abby Wheaton
#Boggleboard class

import random
import string
import copy
class BoggleBoard:
    #initalizing board
    def __init__(self):
        self.__board = []
        self.__row1 = []
        self.__row2 = []
        self.__row3 = []
        self.__row4 = []
        self.__word = ''

        self.__board = [self.__row1, self.__row2, self.__row3, self.__row4]



    #setting self.__word to the user's word
    def set_word(self, word):
        self.__word = word

    #fill the board with random capital letters using a nested for loop
    def fill_board (self):
        for rows in self.__board:
            for x in range(4):
                rows.append(random.choice(string.ascii_uppercase))


    #this is change the value of self.__board to the testing board after the word is found successfully
    def update_board(self, test_board):
       self.__board = test_board


    def print_board(self):
    #prints the board using a nested for loop
        for rows in self.__board:
            #staring with an empty string
            row_string = ''
            print("+---+ +---+ +---+ +---+")
            for letter in rows:
                #checking to see if there is an updated character
                #if there is, no spaces are added
                if '<' in letter:
                    row_string+= '|' + letter + '| '
                else:
                    row_string += "| "+ letter+ ' | '
            #printing concatenated string

            print(row_string)
            print("+---+ +---+ +---+ +---+")


    #added all indicies of the first letter of user word to a list
    def check_char(self, en_list, char):
        index_list = []
        for index_tuple in en_list:
            if index_tuple[1] == char:
                index_list.append(index_tuple[0])
        return index_list

    #makes a list of all indicies of the first letter of user's word
    def find_indices(self):
        char_list = []
        first_char = self.__word[0]
        #adding all the letters in the board to a list
        for x in range(4):
            for y in range(4):
                char_list.append(self.__board[x][y])
        #creating a list of tuples, which contain the index and the first character in user's word
        index_char_list = list(enumerate(char_list))
        index_list = self.check_char(index_char_list, first_char)
        return index_list


    #given the list of board letters, it will return the row and spot in the row of the first letter of the inputted word
    def board_spot(self, index_list_spot):
        if index_list_spot == 0:
            return 0, 0
        elif index_list_spot == 1:
            return 0, 1
        elif index_list_spot == 2:
            return 0, 2
        elif index_list_spot == 3:
            return 0, 3
        elif index_list_spot == 4:
            return 1, 0
        elif index_list_spot == 5:
            return 1, 1
        elif index_list_spot == 6:
            return 1, 2
        elif index_list_spot == 7:
            return 1, 3
        elif index_list_spot == 8:
            return 2, 0
        elif index_list_spot == 9:
            return 2, 1
        elif index_list_spot == 10:
            return 2, 2
        elif index_list_spot == 11:
            return 2, 3
        elif index_list_spot == 12:
            return 3, 0
        elif index_list_spot == 13:
            return 3, 1
        elif index_list_spot == 14:
            return 3, 2
        elif index_list_spot == 15:
            return 3, 3

    #checks the spot to the right of the current letter
    def check_right(self, test_board, row, letter_spot, index):
        try:
            #returns true if the spot to the right equals the next letter in the word
            if (test_board[row][letter_spot + 1] == self.__word[index +1]) and (letter_spot + 1 <= 3):
                return True
            else:
                return False
        except IndexError:
            return False

    #checks the spot to the left of the current letter
    def check_left(self, test_board, row, letter_spot, index):
        try:
            # returns true if the spot to the right equals the next letter in the word
            if (letter_spot - 1 >= 0) and (test_board[row][letter_spot - 1] == self.__word[index + 1]):
                return True
            else:
                return False
        except IndexError:
            return False

    #checks the spot above the current letter
    def check_up(self, test_board, row, letter_spot, index):
        try:
            # returns true if the spot to the right equals the next letter in the word
            if (row > 0) and (test_board[row - 1][letter_spot] == self.__word[index + 1]):
                return True
            else:
                return False
        except IndexError:
            return False

    # checks the spot below the current letter
    def check_down(self, test_board,  row, letter_spot, index):
        try:
            # returns true if the spot to the right equals the next letter in the word
            if (row < 3) and (test_board[row + 1][letter_spot] == self.__word[index +1]):
                return True
            else:
                return False
        except IndexError:
            return False


    def add_arrows(self, row, letter_spot, test_board):
        # puts the arrows around the found letters
        test_board[row][letter_spot] = '<' + test_board[row][letter_spot] + '>'



    #word validation on board
    def word_on_board(self):
        #make copy of board
        test_board = copy.deepcopy(self.__board)
        word_index = 0
        test_word = self.__word[0]
        #make a list of indices of the first letter of the user given word
        index_list = self.find_indices()
        #if there are no occurances of the letter, returns False
        if len(index_list) == 0:
            return False

        else:
            #finding the spot on the board given by the first index in the index list
            row, letter_spot = self.board_spot(index_list[0])

            #will iterate as long as the index list is not empty
            while len(index_list)!= 0:
                #adding the arrows to the first letter of the board
                self.add_arrows(row, letter_spot, test_board)

                #checks to see if the test string is equal to the user's word and returns True if it is
                if test_word == self.__word:
                    self.update_board(test_board)
                    return True

                #if the word is not equal to the test string, it will check to the right of the letter
                elif self.check_right(test_board, row, letter_spot, word_index):
                    #if it is to the right, then it changes the index to be the spot to the right
                    # moves on the next character of the user's word
                    # adds the found character to the testing string

                    letter_spot += 1
                    word_index += 1
                    test_word += test_board[row][letter_spot]

                # if the word is not equal to the test string, it will check to the left of the letter
                elif self.check_left(test_board, row, letter_spot, word_index):
                    # if it is to the left, then it changes the index to be the spot to the left
                    # moves on the next character of the user's word
                    # adds the found character to the testing string

                    letter_spot -= 1
                    word_index += 1
                    test_word += test_board[row][letter_spot]

                # if the word is not equal to the test string, it will check the spot above the letter
                elif self.check_up(test_board, row, letter_spot, word_index):
                    # if it is above, then it changes the index to be the spot above
                    # moves on the next character of the user's word
                    # adds the found character to the testing string

                    row -= 1
                    word_index += 1
                    test_word += test_board[row][letter_spot]

                # if the word is not equal to the test string, it will check the spot below the letter
                elif self.check_down(test_board, row, letter_spot, word_index):
                    # if it is below, then it changes the index to be the spot below
                    # moves on the next character of the user's word
                    # adds the found character to the testing string

                    row += 1
                    word_index += 1
                    test_word += test_board[row][letter_spot]


                #if the word is not equal to the test string, and the next character is not next to the current letter of the word
                #it will check to see if this was the last index to check in the index list
                elif len(index_list) ==1:
                    return False

                #if there are more indexes to check, it will reset the test string, the board, and the current charcter of the user's word
                #it then deletes the first index in the list of indexes and starts looking at the next index
                else:
                    test_word = self.__word[0]
                    test_board = copy.deepcopy(self.__board)
                    word_index = 0
                    del index_list[0]
                    row, letter_spot = self.board_spot(index_list[0])









