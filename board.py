'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

board.py:
Contains the class modelling the basic game board.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/05/28
'''

# Libraries:
import pygame as pg

# Local files:
import dictionary
import player
import tile

class Board:
	DIMENSION_BOARD = 15
	POSITION_FIRST = (7, 7)

	PREMIUM_LETTER_2X = 'L2'
	PREMIUM_LETTER_3X = 'L3'
	PREMIUM_WORD_2X = 'W2'
	PREMIUM_WORD_3X = 'W3'

	POSITIONS_LETTER_2X = [(0, 3), (0, 11),
						   (2, 6), (2, 8),
						   (3, 0), (3, 7), (3, 14),
						   (6, 2), (6, 6), (6, 8), (6, 12),
						   (7, 3), (7, 11),
						   (8, 2), (8, 6), (8, 8), (8, 12),
						   (11, 0), (11, 7), (11, 14),
						   (12, 6), (12, 8),
						   (14, 3), (14, 11)]

	POSITIONS_LETTER_3X = [(1, 5), (1, 9),
						   (5, 1), (5, 5), (5, 9), (5, 13),
						   (9, 1), (9, 5), (9, 9), (9, 13),
						   (13, 5), (13, 9)]

	POSITIONS_WORD_2X = [(1, 1), (1, 13),
						 (2, 2), (2, 12),
						 (3, 3), (3, 11),
						 (4, 4), (4, 10),
						 (7, 7),
						 (10, 4), (10, 10),
						 (11, 3), (11, 11),
						 (12, 2), (12, 12),
						 (13, 1), (13, 13)]

	POSITIONS_WORD_3X = [(0, 0), (0, 7), (0, 14),
						 (7, 0), (7, 14),
						 (14, 0), (14, 7), (14, 14)]

	DICTIONARY_FILE = 'media/scrabblewords.txt'

	SQUARE_SIZE = tile.Tile.SQUARE_SIZE
	SQUARE_BORDER = tile.Tile.SQUARE_BORDER
	BOARD_TOP = 0
	BOARD_LEFT = 0

	PROMPT_LEFT = 830 # 145
	PROMPT_TOP = 180 # 200
	PROMPT_WIDTH = 250
	PROMPT_HEIGHT = 75
	PROMPT_FONT = None

	COLOR_BACKGROUND = (15, 75, 0)
	COLOR_DEFAULT = (30, 150, 0)
	COLOR_LETTER_2X = (100, 200, 255)
	COLOR_LETTER_3X = (0, 100, 255)
	COLOR_WORD_2X = (255, 100, 0)
	COLOR_WORD_3X = (255, 0, 0)

	MASK_COLOR = (0, 0, 0, 100)

	'''
	Initialize the board, create the square matrix and mark all the special square.
	'''
	def __init__(self):
		self.square = []
		for x in range(Board.DIMENSION_BOARD):
			self.square.append([])
			for y in range(Board.DIMENSION_BOARD):
				self.square[x].append((None, None))

		for (x, y) in self.POSITIONS_LETTER_2X:
			self.square[x][y] = (None, Board.PREMIUM_LETTER_2X)

		for (x, y) in self.POSITIONS_LETTER_3X:
			self.square[x][y] = (None, Board.PREMIUM_LETTER_3X)

		for (x, y) in self.POSITIONS_WORD_2X:
			self.square[x][y] = (None, Board.PREMIUM_WORD_2X)

		for (x, y) in self.POSITIONS_WORD_3X:
			self.square[x][y] = (None, Board.PREMIUM_WORD_3X)

		# These locks control which row/column can be played upon to force play in a straight line.
		self.column_lock = -1
		self.row_lock = -1

		# Load the dictionary.
		self.dictionary = dictionary.Dictionary(Board.DICTIONARY_FILE)

		# Load font.
		Board.PROMPT_FONT = pg.font.SysFont('bahnschrift', 28)


	'''
	Locates a board position and tries to put a tile there:
	
	Returns false if any of these apply:
		The square is occupied.
		The position is outside the bounds of the board.
		The play has already been constrained in a particular direction.
	'''
	def temporary_move(self, x_position, y_position, tile_current):
		(board_x, board_y) = self.get_board_position(x_position, y_position)

		if self.check_locks(board_x, board_y):
			if board_x >= 0 and board_y >= 0 and board_x < Board.DIMENSION_BOARD and board_y < Board.DIMENSION_BOARD:
				previousTile = self.square[board_x][board_y][0]
				if previousTile == None:
					self.square[board_x][board_y] = (tile_current, self.square[board_x][board_y][1])
					if tile_current.is_tile_blank():
						return ("CHOOSE_LETTER", tile_current)
					self.set_locks()
					return (True, tile_current)
		return (False, tile_current)

	'''
	Returns true if the position is playable based on the lock combinations.
	'''
	def check_locks(self, board_x, board_y):
		if (self.row_lock >= 0 and self.column_lock >= 0) and (board_x == self.column_lock or board_y == self.row_lock):
			locks_correct = True
		elif self.column_lock >= 0 and board_x == self.column_lock:
			locks_correct = True
		elif self.row_lock >= 0 and board_y == self.row_lock:
			locks_correct = True
		elif self.row_lock < 0 and self.column_lock < 0:
			locks_correct = True
		else:
			locks_correct = False
		return locks_correct

	'''
	Scans the board:
		If there is one unlocked tile, set both a row/column lock.
		If there are two, set only the lock for that row/column.
		If there are none, remove all locks.
	'''
	def set_locks(self):
		temporary_tiles = []
		for x in range(Board.DIMENSION_BOARD):
			for y in range(Board.DIMENSION_BOARD):
				if self.square[x][y][0] != None and not self.square[x][y][0].locked:
					temporary_tiles.append((x, y))
		# Case 1: No temporary tiles.
		if len(temporary_tiles) == 0:
			self.column_lock = -1
			self.row_lock = -1
		# Case 2: One temporary tile, allow play on row and column.
		elif len(temporary_tiles) == 1:
			self.column_lock = temporary_tiles[0][0]
			self.row_lock = temporary_tiles[0][1]
		# Case 3: More than one temporary tile, disable play outside of line.
		else:	
			col = temporary_tiles[0][0]
			row = temporary_tiles[0][1]
			in_one_column = True
			in_one_row = True
			for t in temporary_tiles:
				if(t[0] != col):
					in_one_column = False
				if(t[1] != row):
					in_one_row = False
			
			if in_one_column:
				self.column_lock = col
				self.row_lock = -1
			elif in_one_row:
				self.column_lock = -1
				self.row_lock = row	
					
	
	'''
	Attempts to remove the tile from the given square:
		Returns the tile if it was removed successfully, otherwise returns None.
		If the coordinates were out of range, the square didn't have a tile or if the tile was locked.
	'''	
	def lift_board_tile(self, x_position, y_position):
		(board_x, board_y) = self.get_board_position(x_position, y_position)

		if board_x >= 0 and board_y >= 0:
			tile_current = self.square[board_x][board_y][0]

			if tile_current != None and not tile_current.locked:
				self.square[board_x][board_y] = (None, self.square[board_x][board_y][1])
				self.set_locks()
				return tile_current

		return None
			
	'''
	Returns the (board_x, board_y) tuple of the coordinates on the board based on screen coordinates.
	'''
	def get_board_position(self, x_position, y_position):
		x_position -= Board.BOARD_LEFT + Board.SQUARE_BORDER
		y_position -= Board.BOARD_TOP + Board.SQUARE_BORDER
		
		# Make sure coordinates are in the tile area:
		if x_position >= 0 and y_position >= 0:
			# Don't count clicks in the gaps between tiles:
			if (x_position % (Board.SQUARE_SIZE + Board.SQUARE_BORDER) < Board.SQUARE_SIZE - Board.SQUARE_BORDER and
			   y_position % (Board.SQUARE_SIZE + Board.SQUARE_BORDER) < Board.SQUARE_SIZE - Board.SQUARE_BORDER):
				board_x = (int)(x_position / (Board.SQUARE_SIZE + Board.SQUARE_BORDER))
				board_y = (int)(y_position / (Board.SQUARE_SIZE + Board.SQUARE_BORDER))
				# Make sure coordinates aren't off the board:
				if board_x < Board.DIMENSION_BOARD and board_y < Board.DIMENSION_BOARD:
					return (board_x, board_y)
		return (-1, -1)
		
	
	'''
	Puts a tile on the board.
	'''	
	def place_tile(self, coordinates, tile):
		x = coordinates[0]
		y = coordinates[1]
		self.square[x][y] = (tile, self.square[x][y][1])
		
	'''
	Goes through all temporary tiles on the board, validating the move and processing the play.
		Upon success, the tiles are locked.
		Upon failure, the tiles are removed entirely.
	
	Validation rules:
		1) At least one tile must be temporary.
		2) All temporary tiles must lie on one line.
		3) On the first turn, one tile must be located on the central square.
		4) The linear word must be unbroken (including locked tiles).
		5) At least one crossword must be formed.
		6) All words formed must be inside the dictionary.
	
	'''	
	def play_move(self, move_first=True):
		# Collect all temporary tiles.
		temporary_tiles = []
		for x in range(Board.DIMENSION_BOARD):
			for y in range(Board.DIMENSION_BOARD):
				if self.square[x][y][0] != None and not self.square[x][y][0].locked:
					temporary_tiles.append((x, y))
		
		# There must be at least one tile played.
		if len(temporary_tiles) <= 0:
			#fail
			return ([], -1)			
			
		# Tiles must be played on a straight line.
		col = temporary_tiles[0][0]
		row = temporary_tiles[0][1]
		in_one_column = True
		in_one_row = True
		for (x, y) in temporary_tiles:
			if(x != col):
				in_one_column = False
			if(y != row):
				in_one_row = False
		
		if not in_one_row and not in_one_column:
			# Fail, remove tiles and return.
			return (self.discard_move(), -1)
		
		# If move_first, then one tile must be on POSITION_FIRST
		if not Board.POSITION_FIRST in temporary_tiles and move_first:
			return(self.discard_move(), -1)
		
		# Word created is unbroken.
		unbroken = True
		left = col
		right = col
		top = row
		bottom = row
		
		# Determine the span of the word in either up/down or left/right directions.
		for (x, y) in temporary_tiles:
			if x < left:
				left = x
			elif x > right:
				right = x
			if y < top:
				top = y
			elif y > bottom:
				bottom = y
				
		# Confirm that the span is unbroken.
		if in_one_column:
			for y in range(top, bottom+1):
				if self.square[col][y][0] == None:
					unbroken = False
		elif in_one_row:
			for x in range(left, right+1):
				if self.square[x][row][0] == None:
					unbroken = False
					
		if not unbroken:
			return(self.discard_move(), -1)

		(total_score, spellings, seed_ratio) = self.validate_words(move_first, temporary_tiles=temporary_tiles)
		
		if total_score < 0:
			return(self.discard_move(), -1)
			

		# Lock tiles played.
		for (x, y) in temporary_tiles:
			self.square[x][y][0].locked = True			
			
		# Remove the locks on the board.
		self.column_lock = -1
		self.row_lock = -1	
			
		return (None, total_score)

	'''
	Searches through the conflicted word space,
	trying all options to see which assignment of word score bonuses yields the highest points.
	'''
	def find_highest_scorer(self, conflicts, scores, bonuses_applied = []):
		if len(conflicts) == 0:
			total_score = 0
			for (bonus, word) in bonuses_applied:
				total_score += scores[word] * bonus
				return (total_score, bonuses_applied)
		# Check both possible bonus applications:
		else:
			# Apply bonus to first crossword:
			bonuses_applied1 = bonuses_applied[:]
			bonuses_applied1.append((conflicts[0][0], conflicts[0][1][0]))
			score1 = self.find_highest_scorer(conflicts[1:], scores, bonuses_applied1)

			# Apply bonus to second crossword:
			bonuses_applied2 = bonuses_applied[:]
			bonuses_applied2.append((conflicts[0][0], conflicts[0][1][1]))
			score2 = self.find_highest_scorer(conflicts[1:], scores, bonuses_applied2)

			if score1 > score2:
				best_score = score1
				best_bonus = bonuses_applied1
			else:
				best_score = score2
				best_bonus = bonuses_applied2

			return (best_score, best_bonus)
		
	'''
	Checks if all the words played are valid.
	'''
	def validate_words(self, move_first, tiles_played=None, temporary_tiles=None):
		# A list containing lists of ((x, y), tile).
		words_built = []

		if tiles_played != None:
			temporary_tiles = []
			for pos, tile in tiles_played:
				self.place_tile(pos,tile)
				temporary_tiles.append(pos)

		seed_ratio = self.calculate_seed_ratio()

	
		# Ensure a crossword is formed and keep a list of words built:
		'''
		Find all the crosswords by going through all the rows
		and columns which contain temporary tiles (potential words).
		
		Start with a temporary tile on that row/column and expand outward in both directions
		until hitting a blank on both ends (the created word).
		
		Go through the words and confirm that a previously played tile was used.
		'''
	
		# First build a list of possible word rows and columns.
		rows_to_check = []
		columns_to_check = []
		row_set = []
		column_set = []
		for (x, y) in temporary_tiles:
			if not x in column_set:
				column_set.append(x)
				columns_to_check.append((x, y))
			if not y in row_set:
				row_set.append(y)
				rows_to_check.append((x, y))
		
		# Build words along rows:
		for (col, row) in rows_to_check:
			
			# Build left:
			left = col
			while left - 1 >= 0 and self.square[left - 1][row][0] != None:
				left -= 1
			
			# Build right:
			right = col
			while right + 1 < Board.DIMENSION_BOARD and self.square[right + 1][row][0] != None:
				right += 1
			
			# Add the word built if it has at least 2 letters:
			if left != right:
				words_built.append([((x, row), self.square[x][row][0]) for x in range(left, right + 1)])

		# Build words along columns:
		for (col, row) in columns_to_check:

			# Build up:
			up = row
			while up - 1 >= 0 and self.square[col][up - 1][0] != None:
				up -= 1

			# Build down:
			down = row
			while down + 1 < Board.DIMENSION_BOARD and self.square[col][down + 1][0] != None:
				down += 1

			# Add the word built.
			if up != down:
				words_built.append([((col, y), self.square[col][y][0]) for y in range(up, down + 1)])
				
		crossword_made = False
		for word in words_built:
			for ((x, y), tile_current) in word:
				if tile_current.locked:
					crossword_made = True
					
		if not crossword_made and not move_first:
			# Fails if word is unattached.
			self.remove_tiles_fast(tiles_played)			
			return (-1, None, seed_ratio)
					

		# Ensure all words in words_built are in the dictionary.
		spellings = []
		for word in words_built:
			spelling = ""
			for (position, tile_current) in word:
				spelling += tile_current.letter
			spellings.append(spelling)	
			if not self.dictionary.is_word_valid(spelling):
				# Fails if word isn't a valid dictionary word.
				self.remove_tiles_fast(tiles_played)
				return (-1, None, seed_ratio)
		
		# Calculate score:
		total_score = 0
		
		# 50 point bonus for using all tiles:
		if len(temporary_tiles) == player.Player.RACK_SIZE:
			total_score += 50

		# Contains word-point value for each word.
		word_scores = {}
		# Stores words where word bonuses are conflicted.
		words_conflicting = []
		i = 0
		# We can only get bonuses for one word, so only apply corner bonuses once.
		marks = []
		for word in words_built:
			word_scores[i] = 0
			word_bonus = 1
			for (x, y), tile_current in word:
				letter_score = tile_current.value
				# Can't get bonuses for previously played tiles.
				if self.square[x][y][0].locked == False:
					crosswords = self.shared((x, y), words_built)
					bonus = self.square[x][y][1]
					if bonus == Board.PREMIUM_LETTER_2X and not (x, y) in marks:
						letter_score *= 2
						marks.append((x, y))
					elif bonus == Board.PREMIUM_LETTER_3X and not (x, y) in marks:
						letter_score *= 3
						marks.append((x, y))
					elif bonus == Board.PREMIUM_WORD_2X:
						if len(crosswords) <= 1:
							word_bonus *= 2
						else:
							if not (2, crosswords) in words_conflicting:
								words_conflicting.append((2, crosswords))
					elif bonus == Board.PREMIUM_WORD_3X:
						if len(crosswords) <= 1:
							word_bonus *= 3
						else:
							if not (3, crosswords) in words_conflicting:
								words_conflicting.append((3, crosswords))
				word_scores[i] += letter_score
			word_scores[i] *= word_bonus
			i += 1
			
		# If are conflicts, then go through all permutations to retrieve the highest possible score.
		if len(words_conflicting) > 0:
			(best, best_word_scores) = self.find_highest_scorer(words_conflicting, word_scores)
			for (bonus, word) in best_word_scores:
				word_scores[word] *= bonus	
		
		# Now add up all the words to make the total score.
		for score in word_scores.values():
			total_score += score
			
		# Pull the tiles if we put them on in this call.
		self.remove_tiles_fast(tiles_played)

		return (total_score, spellings, seed_ratio)

	'''
	Removes tiles if we already know where they are.
	'''			
	def remove_tiles_fast(self, tiles_played):
		if tiles_played != None:
			for (x, y), tile in tiles_played:
				assert self.square[x][y][0] != None
				assert self.square[x][y][0].locked == False
				if self.square[x][y][0].is_blank:
					self.square[x][y][0].letter = ' '
				self.square[x][y] = (None, self.square[x][y][1])
					
	'''
	Returns a list of all word indices using the given tile.
	'''	
	def shared(self, pos, words):
		wordsUsingPos = []
		i = 0
		for word in words:
			for (coords, tile) in word:
				if pos == coords:
					wordsUsingPos.append(i)
			i+=1
					
		return wordsUsingPos
			
	'''
	Removes the temporary tiles on the board and returns them as a list.
	'''
	def discard_move(self):
		temporary_tiles = []
		for x in range(Board.DIMENSION_BOARD):
			for y in range(Board.DIMENSION_BOARD):
				if self.square[x][y][0] != None and not self.square[x][y][0].locked:
					temporary_tiles.append(self.square[x][y][0])
					self.square[x][y] = (None, self.square[x][y][1])
		
		# Remove the locks the player can play again.
		self.column_lock = -1
		self.row_lock = -1
		
		return temporary_tiles
		
	'''
	Calculates the number of seeds and number of tiles and returns them as a tuple.
	'''
	def calculate_seed_ratio(self):
		seed_count = 0
		tile_count = 0
		for x in range(Board.DIMENSION_BOARD):
			for y in range(Board.DIMENSION_BOARD):
				if self.square[x][y][0] != None:
					tile_count += 1
				elif ((x > 0 and self.square[x-1][y][0] != None) or
					  (x < Board.DIMENSION_BOARD-1 and self.square[x+1][y][0] != None) or
					  (y > 0 and self.square[x][y-1][0] != None) or
					  (y < Board.DIMENSION_BOARD-1 and self.square[x][y+1][0] != None)):
					seed_count += 1

		if seed_count == 0:
			seed_count = 1
			
		return (seed_count, tile_count)

	'''
	Prompts player to set a letter for the blank tile.
	'''	
	def choose_letter(self, tile_blank, DISPLAY_SCRABBLE, DISPLAY_OVERLAY):

		letter = None
		self.draw_prompt(DISPLAY_SCRABBLE, DISPLAY_OVERLAY)
		while letter == None:
			for event in pg.event.get():
				if event.type == pg.KEYUP:
					if event.key == pg.K_a:
						letter = 'A'
					elif event.key == pg.K_b:
						letter = 'B'
					elif event.key == pg.K_c:
						letter = 'C'
					elif event.key == pg.K_d:
						letter = 'D'
					elif event.key == pg.K_e:
						letter = 'E'
					elif event.key == pg.K_f:
						letter = 'F'
					elif event.key == pg.K_g:
						letter = 'G'
					elif event.key == pg.K_h:
						letter = 'H'
					elif event.key == pg.K_i:
						letter = 'I'
					elif event.key == pg.K_j:
						letter = 'J'
					elif event.key == pg.K_k:
						letter = 'K'
					elif event.key == pg.K_l:
						letter = 'L'
					elif event.key == pg.K_m:
						letter = 'M'
					elif event.key == pg.K_n:
						letter = 'N'
					elif event.key == pg.K_o:
						letter = 'O'
					elif event.key == pg.K_p:
						letter = 'P'
					elif event.key == pg.K_q:
						letter = 'Q'
					elif event.key == pg.K_r:
						letter = 'R'
					elif event.key == pg.K_s:
						letter = 'S'
					elif event.key == pg.K_t:
						letter = 'T'
					elif event.key == pg.K_u:
						letter = 'U'
					elif event.key == pg.K_v:
						letter = 'V'
					elif event.key == pg.K_w:
						letter = 'W'
					elif event.key == pg.K_x:
						letter = 'X'
					elif event.key == pg.K_y:
						letter = 'Y'
					elif event.key == pg.K_z:
						letter = 'Z'
			pg.display.update()
		
		# Set the letter.
		tile_blank.letter = letter

	'''
	Draws a letter prompt to ask for the blank letter.
	'''												
	def draw_prompt(self, DISPLAY_SCRABBLE, DISPLAY_OVERLAY):
		
		# Draw prompt shadow.
		DISPLAY_OVERLAY.fill((0,0,0,0))
		pg.draw.rect(DISPLAY_OVERLAY, Board.MASK_COLOR, (Board.PROMPT_LEFT, Board.PROMPT_TOP, Board.PROMPT_WIDTH+4, Board.PROMPT_HEIGHT+4))
		
		# Draw text.
		promptText = Board.PROMPT_FONT.render("CHOOSE LETTER!", True, (0,0,0,200), (255,255,255,200))
		promptRect = promptText.get_rect()
		promptRect.center = (Board.PROMPT_LEFT+Board.PROMPT_WIDTH/2, Board.PROMPT_TOP+Board.PROMPT_HEIGHT/2)
		DISPLAY_SCRABBLE.blit(promptText, promptRect)
		
	'''
	Redraws only tiles which are animating.
	'''	
	def draw_animated(self, DISPLAY_SCRABBLE, DISPLAY_OVERLAY):
		for x in range(Board.DIMENSION_BOARD):
			for y in range(Board.DIMENSION_BOARD):
				#draw position
				(tile, bonus) = self.square[x][y]
				if tile != None:
					left = x * (Board.SQUARE_SIZE + Board.SQUARE_BORDER) + Board.SQUARE_BORDER + Board.BOARD_LEFT
					top = y * (Board.SQUARE_SIZE + Board.SQUARE_BORDER) + Board.SQUARE_BORDER + Board.BOARD_TOP
					tile.draw_animated(left, top, DISPLAY_SCRABBLE, (not tile.locked))
																																				
			
	'''
	Draw the board and any placed tiles.
	'''			
	def draw_board(self, DISPLAY_SCRABBLE, DISPLAY_OVERLAY):
		pg.draw.rect(DISPLAY_SCRABBLE, Board.COLOR_BACKGROUND,
					 (0,0, 15*(Board.SQUARE_SIZE + Board.SQUARE_BORDER) + Board.SQUARE_BORDER + Board.BOARD_LEFT,15*(Board.SQUARE_SIZE + Board.SQUARE_BORDER) + Board.SQUARE_BORDER + Board.BOARD_LEFT))

		#draw each square
		for x in range(Board.DIMENSION_BOARD):
			for y in range(Board.DIMENSION_BOARD):
				#draw position
				x_position = x * (Board.SQUARE_SIZE + Board.SQUARE_BORDER) + Board.SQUARE_BORDER + Board.BOARD_LEFT
				y_position = y * (Board.SQUARE_SIZE + Board.SQUARE_BORDER) + Board.SQUARE_BORDER + Board.BOARD_TOP

				(tile_current, bonus) = self.square[x][y]
				if self.square[x][y][1] == Board.PREMIUM_LETTER_2X:
					square_color = Board.COLOR_LETTER_2X
				elif self.square[x][y][1] == Board.PREMIUM_LETTER_3X:
					square_color = Board.COLOR_LETTER_3X
				elif self.square[x][y][1] == Board.PREMIUM_WORD_2X:
					square_color = Board.COLOR_WORD_2X
				elif self.square[x][y][1] == Board.PREMIUM_WORD_3X:
					square_color = Board.COLOR_WORD_3X
				else:
					square_color = Board.COLOR_DEFAULT

				pg.draw.rect(DISPLAY_SCRABBLE, square_color, (x_position, y_position, Board.SQUARE_SIZE, Board.SQUARE_SIZE))
				
				if tile_current != None:
					if tile_current.locked:
						highlight = False
					else:
						highlight = True
					tile_current.draw_tile(x_position, y_position, DISPLAY_SCRABBLE, highlight)
		
		# Draw lock overlay:
		DISPLAY_OVERLAY.fill((0, 0, 0, 0))
		top = Board.BOARD_TOP
		left = Board.BOARD_LEFT
		right = Board.DIMENSION_BOARD*(Board.SQUARE_BORDER + Board.SQUARE_SIZE) + Board.SQUARE_BORDER
		bottom = Board.DIMENSION_BOARD*(Board.SQUARE_BORDER + Board.SQUARE_SIZE) + Board.SQUARE_BORDER
		x1 = self.column_lock * (Board.SQUARE_SIZE + Board.SQUARE_BORDER) + Board.BOARD_LEFT
		x2 = x1 + (Board.SQUARE_SIZE + Board.SQUARE_BORDER) + Board.SQUARE_BORDER
		y1 = self.row_lock * (Board.SQUARE_SIZE + Board.SQUARE_BORDER) + Board.BOARD_LEFT
		y2 = y1 + (Board.SQUARE_SIZE + Board.SQUARE_BORDER) + Board.SQUARE_BORDER				
		if self.row_lock >= 0 and self.column_lock >= 0:
			pg.draw.rect(DISPLAY_OVERLAY, Board.MASK_COLOR, (left, top, x1-left, y1-top))
			pg.draw.rect(DISPLAY_OVERLAY, Board.MASK_COLOR, (left, y2, x1-left, bottom-y2))
			pg.draw.rect(DISPLAY_OVERLAY, Board.MASK_COLOR, (x2, top, right-x2, y1-top))
			pg.draw.rect(DISPLAY_OVERLAY, Board.MASK_COLOR, (x2, y2, right-x2, bottom-y2))
		elif self.row_lock >= 0:
			pg.draw.rect(DISPLAY_OVERLAY, Board.MASK_COLOR, (left, top, right-left, y1-top))
			pg.draw.rect(DISPLAY_OVERLAY, Board.MASK_COLOR, (left, y2, right-left, bottom-y2))
		elif self.column_lock >= 0:
			pg.draw.rect(DISPLAY_OVERLAY, Board.MASK_COLOR, (left, top, x1-left, bottom-top))
			pg.draw.rect(DISPLAY_OVERLAY, Board.MASK_COLOR, (x2, top, right-x2, bottom-top))
			
		DISPLAY_SCRABBLE.blit(DISPLAY_OVERLAY, (0, 0))
