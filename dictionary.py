'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

bag.py:
Contains the class modelling the game dictionary being used.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/05/20
'''

class Dictionary:
    file_name = "dictionary_SOWPODS.txt"

    def __init__(self):
        self.words = []

        dictionary_file = open(self.file_name, 'r')
        for line in dictionary_file:
            word = line.rstrip()
            self.words.append(word)



