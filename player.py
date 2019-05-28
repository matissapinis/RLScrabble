'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

tile.py:
Contains the class modelling game player.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/05/28
'''

# Libraries:
import pygame

# Local files:
import board
import tile
import bag

class Player:
	FONT_COLOR = (55, 46, 40)
	BACKGROUND_COLOR = (255, 255, 255)
	
	RACK_SIZE = 7
	
	initialized = False

	RACK_COLOR = (110, 92, 80)
	RACK_LEFT = 183 # 100
	RACK_TOP = 800 # 550
	RACK_FIRST_LEFT = RACK_LEFT + tile.Tile.SQUARE_BORDER + tile.Tile.SQUARE_SIZE * .5
	RACK_FIRST_TOP = RACK_TOP + tile.Tile.SQUARE_BORDER
	
	@staticmethod
	def initialize():
		Player.FONT = pygame.font.Font('freesansbold.ttf', 18)
		Player.initialized = True
	
	'''
	Initialize a new player with a rack and score
	'''
	def __init__(self, game_board, game_bag):
		if not Player.initialized:
			Player.initialize()
		
		self.rack = []
		self.total_score = 0
		self.game_board = game_board
		self.game_bag = game_bag
		self.delta_score = 0

		self.hand = -1

		# Start with a full set of tiles:
		self.fill_rack()

	'''
	Try to grab a tile from the rack. If no tile is picked, return None, otherwise return the tile
	grabbed and put the tile in-hand. If there is a tile in-hand, swap it with the tile chosen
	'''
	def lift_rack_tile(self, x_position, y_position):
		index_rack = self.get_rack_position(x_position, y_position)

		if index_rack != -1 and index_rack < len(self.rack):
			if self.hand == -1:
				# Pick up the tile:
				self.hand = index_rack
				return self.rack[index_rack]
			else:
				# Swap the tiles:
				self.rack[index_rack], self.rack[self.hand] = self.rack[self.hand], self.rack[index_rack]

		# If swapped or tried to lift something else, remove it from hand:
		self.hand = -1
		return None

	'''
	Removes the in-hand piece from the rack.
	'''
	def temporary_move(self):
		if self.hand != -1:
			del self.rack[self.hand]
			self.hand = -1

	'''
	Finds the rack index selected based on screen coordinates provided (returns None if out of range).
	'''
	def get_rack_position(self, x_position, y_position):

		x_position -= Player.RACK_FIRST_LEFT
		y_position -= Player.RACK_FIRST_TOP

		# Make sure coordinates are in the tile area.
		if x_position >= 0 and y_position >= 0 and y_position <= tile.Tile.SQUARE_SIZE:
			# Don't count clicks in the gaps between tiles.
			if x_position % (tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER) < tile.Tile.SQUARE_SIZE - tile.Tile.SQUARE_BORDER:
				index_rack = (int)(x_position / (tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER))
				# Make sure coordinates are in the rack.
				if index_rack < len(self.rack):
					return index_rack
		return -1

	'''
	Draws the rack at the bottom of the screen.
	'''
	def draw_rack(self, DISPLAYSURF):

		# Draw a basic rack:
		pygame.draw.rect(DISPLAYSURF, board.Board.COLOR_BACKGROUND, (Player.RACK_LEFT, Player.RACK_TOP,
														 (tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER) * 8,
														 tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER * 2))

		# Draw each tile:
		i = 0
		for tile_iterated in self.rack:
			top = Player.RACK_FIRST_TOP
			left = (Player.RACK_FIRST_LEFT + (i * (tile.Tile.SQUARE_SIZE + tile.Tile.SQUARE_BORDER)))

			if i == self.hand:
				highlight = True
			else:
				highlight = False

			tile_iterated.draw_tile(left, top, DISPLAYSURF, highlight)
			i += 1

	'''
	Returns False if the player tries to draw new tiles and none exist in the bag.
	Returns True if either tiles were successfully removed, or the rack isn't empty. 
	'''
	def fill_rack(self):
		if not self.game_bag.is_bag_empty():
			
			# Attempt to withdraw the needed number of tiles.
			tile_number = Player.RACK_SIZE - len(self.rack)
			for i in range(tile_number):
				new_tile = self.game_bag.pull_tile()
				if new_tile != None:
					self.rack.append(new_tile)
			
		# If the bag was empty and our rack is empty, signal that game is over.
		elif len(self.rack) == 0:
			return False
			
		return True
		
	'''
	This function assumes the word was placed on the board by some mechanism as
	temporary tiles. The board then plays the temporary tiles, locking them if
	they work, returning them as a list if they don't. In the latter case, put
	the words back on the rack, in the former add the points and grab new tiles
	
	Returns True if the move was executed successfully (thus ending our turn) and
	False if it wasn't, forcing us to try again
	'''	
	def play_move(self, move_first):
		
		(tiles, points) = self.game_board.play_move(move_first)
		
		# The play was successful, add the points to our score and grab new tiles
		if tiles == None and points >= 0:
			self.total_score += points
			self.delta_score = points
			game_continues = self.fill_rack()
			if game_continues:
				return True
			else:
				return "GAME_OVER"
			
		# Play didn't work, put the tiles back on rack.
		elif tiles != None:
			for tile_current in tiles:
				'''
				Takes a tile previously held, should only be called for returning temporary tiles to the rack.
				'''
				if tile_current.is_tile_blank():
					tile_current.letter = ' '
				self.rack.append(tile_current)
				
			return False
		
		# No temporary tiles we're played:
		else:
			return False
			
	'''
	Puts the rack tiles back in the bag, shuffles the bag and withdraws new tiles.
	'''		
	def shuffle(self):
		for tile_current in self.rack:
			self.game_bag.return_tile(tile_current)
		
		self.rack = []
		self.game_bag.shuffle()
		self.fill_rack()

	'''
	Returns the value of the players rack in points.
	'''
	def rack_value(self):
		value = 0
		for tile_current in self.rack:
			value += tile_current.value
		return value
		
	'''
	Gives the points to the player.
	'''
	def increase_score(self, delta_score):
		self.total_score += delta_score
