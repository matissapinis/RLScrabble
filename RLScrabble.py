'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

RLScrabble.py:
Contains the main part of the application that initiates the "Scrabble" game.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/05/27
'''

# Libraries:
import pygame as pg

# Local files:
import bag
import board
import player
import menu
import tile

pg.init()
pg.font.init()

SIZE_DISPLAY_WIDTH = 1200
SIZE_DISPLAY_HEIGHT = 900

COLOR_DISPLAY = (255, 255, 255)

pg.display.set_caption("RLScrabble")
DISPLAY_SCRABBLE = pg.display.set_mode((SIZE_DISPLAY_WIDTH, SIZE_DISPLAY_HEIGHT))
DISPLAY_OVERLAY = DISPLAY_SCRABBLE.convert_alpha()
DISPLAY_SCRABBLE.fill(COLOR_DISPLAY)

tile.Tile.initialize() #N#

SCORE_LEFT = 865
SCORE_TOP = 100
SCORE_FONT = pg.font.SysFont('bahnschrift', 28)
SCORE_COLOR = (0, 0, 0)

BACKGROUND_COLOR = (255, 255, 255)

### The main function of the application which initiates and terminates running the software code.
'''
Initializes the Python libraries and other local Python files used for running the application.
Initializes constants for the application's GUI features.
Calls functions for initializing the game window, game board, game bag, game player and visually representing these objects as GUI elements.
Runs the pygame environment this system is implemented in continuously registering mouse motions and mouse clicks made in the environment: 
•	If a mouse motion moves the cursor to a user-interactable GUI element, then it is highlighted.
•	If a mouse click is executed on a user-interactable GUI element, then its respective functions are called.
'''
def RLScrabble():
	game_window = menu.Menu(DISPLAY_SCRABBLE)
	game_board = board.Board()
	game_bag = bag.Bag()
	game_player = player.Player(game_board, game_bag)

	game_running = True
	game_over = False

	first_move = True

	tile_picked = None

	draw_game(game_board, game_player, game_over, game_window)

	while game_running:
		mouse_moved = False
		mouse_clicked = False

		pressed_play = False
		pressed_swap = False

		for event in pg.event.get():
			if event.type == pg.QUIT:
				game_running = False
			elif event.type == pg.MOUSEMOTION:
				move_x_position, move_y_position = event.pos
				mouse_moved = True
			elif event.type == pg.MOUSEBUTTONUP:
				click_x_position, click_y_position = event.pos
				mouse_clicked = True

		if mouse_moved:
			game_window.set_button_highlight(DISPLAY_SCRABBLE, move_x_position, move_y_position)

		if mouse_clicked:
			pressed_button = game_window.get_button_name(click_x_position, click_y_position)

			if pressed_button == menu.Menu.PLAY_MOVE:
				pressed_play = True
			elif pressed_button == menu.Menu.SWAP_TILES:
				pressed_swap = True

		if pressed_play and not game_over:
			move_success = game_player.play_move(first_move)
			if move_success == "GAME_OVER":
				game_over = True
				game_finalize(game_player)
			elif move_success:
				first_move = False

			draw_game(game_board, game_player, game_over, game_window)

		if pressed_swap and not game_over:
			game_board.discard_move()
			game_player.shuffle()

			draw_game(game_board, game_player, game_over, game_window)

		if mouse_clicked and not game_over:
			tile_picked = pick_tile(click_x_position, click_y_position, tile_picked, game_board, game_player)
			draw_game(game_board, game_player, game_over, game_window)

		if game_over:
			game_running = False

		draw_parts(game_board, game_player, game_over)
		pg.display.update()

'''
Player attempts to pick up a tile:
a) The player has a tile in hand:
	If it's on the board, attempt to place the tile there:
		If it doesn't work, do nothing.
		If it does work, empty the hand and update the board.
	If it's on the rack, swap positions and set the hand to none.
b) The player doesn't have a tile in hand:
	If it's on the board and the tile is not locked, return it to the end of the rack.
	If it's on the rack, highlight that tile and put it in hand.
'''
def pick_tile(x_position, y_position, tile_picked, game_board, game_player):
	if tile_picked == None:
		# Try to remove a tile from the board.
		tile_current = game_board.lift_board_tile(x_position, y_position)

		if tile_current != None:
			if tile_current.is_tile_blank():
				tile_current.letter = ' '
			game_player.rack.append(tile_current)
			# If it worked, put it back on rack.
			return None
		else:
			# If it didn't, try to remove from the rack.
			tile_current = game_player.lift_rack_tile(x_position, y_position)
			if tile_current != None:
				# If it worked, remember the held tile.
				return tile_current
			else:
				# Hand stays empty.
				return None

	else:
		# Try to place the tile on the board.
		(move_success, tile_blank) = game_board.temporary_move(x_position, y_position, tile_picked)

		if move_success != False:
			if move_success == "CHOOSE_LETTER":
				game_board.choose_letter(tile_blank, DISPLAY_SCRABBLE, DISPLAY_OVERLAY)
			# If move is sucessful place a temporary tile.
			game_player.temporary_move()
			# Empty the hand.
			return None
		else:
			# Else try to swap the tiles on the rack:
			tile_current = game_player.lift_rack_tile(x_position, y_position)
			return tile_current
			

'''
Composite function which redraws everything.
'''	
def draw_game(game_board, game_player, game_over, game_window):
	DISPLAY_SCRABBLE.fill(BACKGROUND_COLOR)
	game_board.draw_board(DISPLAY_SCRABBLE, DISPLAY_OVERLAY)
	game_player.draw_rack(DISPLAY_SCRABBLE)
	draw_score(game_player, game_over)
	game_window.draw_buttons(DISPLAY_SCRABBLE)
	
'''
Function which redraws only animated elements.
'''
def draw_parts(board, game_player, game_over):
	board.draw_animated(DISPLAY_SCRABBLE, DISPLAY_OVERLAY)
	draw_score(game_player, game_over)
		
'''
Draws the score
'''
def draw_score(game_player, game_over):
	x_position = SCORE_LEFT
	y_position = SCORE_TOP

	score_text = SCORE_FONT.render("SCORE: " + str(game_player.total_score), True, SCORE_COLOR, BACKGROUND_COLOR)
	score_area = score_text.get_rect()
	score_area.left = x_position
	score_area.top = y_position
	DISPLAY_SCRABBLE.blit(score_text, score_area)

	pulse_text = SCORE_FONT.render("(+" + str(game_player.delta_score) + ')', True, (0,0,0), BACKGROUND_COLOR)
	pulse_area = pulse_text.get_rect()
	pulse_area.left = score_area.right + 10
	pulse_area.top = y_position
	DISPLAY_SCRABBLE.blit(pulse_text, pulse_area)

	if game_over:
		score_text = SCORE_FONT.render("GAME FINISHED!", True, SCORE_COLOR, BACKGROUND_COLOR)
		score_area = score_text.get_rect()
		score_area.left = x_position
		score_area.top = SCORE_TOP
		DISPLAY_SCRABBLE.blit(score_text, score_area)

'''
Ends the game, taking the rack value from all unfinished players, subtracting the value from their score.
'''
def game_finalize(game_player):
	penalty = game_player.rack_value()
	game_player.increase_score(-penalty)

RLScrabble()
pg.quit()
quit()