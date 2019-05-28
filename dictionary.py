'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

menu.py:
Contains the class modelling the game dictionary.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/05/28
'''

class Dictionary:
	'''
	Loads the list of valid words. 
	'''
	def __init__(self, file_name):
		self.words = {}
		dictionary_file = open(file_name, 'r')
		for line in dictionary_file:
			line = line.rstrip()
			tokens = line.split()
			if len(tokens) == 1:
				count = -1
			elif len(tokens) == 2:
				count = int(tokens[1])
				
			self.words[tokens[0]] = count
			
	'''
	Checks if the word is in the dictionary.
	'''
	def is_word_valid(self, word):
		# True if the word was in the dictionary.
		if word in self.words:
			return True