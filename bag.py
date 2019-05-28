'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

bag.py:
Contains the class modelling the game bag of tiles.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/05/27
'''

'''
Represents the bag of tiles, contains all tiles which haven't been drawn yet.
Initialized with the exact distribution of tiles, grab() will choose one tile
from the bag at random. If none are available, it will return None
'''

# Libraries:
from random import shuffle

# Local files:
import tile

class Bag:
	# Dictionary of tiles by letter as key with 2-tuple as value containing its score value and copy count in bag:
	def __init__(self):
		self.tiles = []

		self.add('A', 1, 9)
		self.add('B', 3, 2)
		self.add('C', 3, 2)
		self.add('D', 2, 4)
		self.add('E', 1, 12)
		self.add('F', 4, 2)
		self.add('G', 2, 3)
		self.add('H', 4, 2)
		self.add('I', 1, 9)
		self.add('J', 8, 1)
		self.add('K', 5, 1)
		self.add('L', 1, 4)
		self.add('M', 3, 2)
		self.add('N', 1, 6)
		self.add('O', 1, 8)
		self.add('P', 3, 2)
		self.add('Q', 10, 1)
		self.add('R', 1, 6)
		self.add('S', 1, 4)
		self.add('T', 1, 6)
		self.add('U', 1, 4)
		self.add('V', 4, 2)
		self.add('W', 4, 2)
		self.add('X', 8, 1)
		self.add('Y', 4, 4)
		self.add('Z', 10, 1)
		self.add(' ', 0, 2)

		shuffle(self.tiles)

	'''
   	Pulls a new tile from the game bag if it’s not empty.
   	'''
	def pull_tile(self):
		if self.is_bag_empty():
			return None

		return self.tiles.pop()

	'''
	Checks whether the game bag is empty or not.
	'''
	def is_bag_empty(self):
		return len(self.tiles) == 0

	'''
	Randomizes the sequence in which tiles would be pulled out of the game bag.
	'''
	def shuffle(self):
		shuffle(self.tiles)

	def return_tile(self, tile):
		self.tiles.append(tile)

	'''
	Adds n copies of a newly created game tile to the game bag. 
	'''
	def add(self, letter, points, n):
		for i in range(n):
			self.tiles.append(tile.Tile(letter, points))
