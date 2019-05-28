'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

menu.py:
Contains the class modelling the game menu.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/05/28
'''

# Libraries:
import pygame as pg

# Local files:
import board
import tile

class Menu():
	PLAY_MOVE = "PLAY MOVE"
	SWAP_TILES = "SWAP TILES"

	def __init__(self, DISPLAY_SCRABBLE):
		self.buttons = {}
		self.rect = (0, 0, 800, 600)
		self.background = (255, 255, 255)

		self.rect = (855, 300, 200, 350) # 570, ..., 200, 300
		self.buttons[self.PLAY_MOVE] = Button(self.PLAY_MOVE, (855, 300, 200, 38)) # 570, ..., 200, 30
		self.buttons[self.SWAP_TILES] = Button(self.SWAP_TILES, (855, 340, 200, 38)) # 570, ..., 200, 30
		DISPLAY_SCRABBLE.fill((255, 255, 255))

	'''
	Goes through all buttons and returns the name of the button, if it was clicked.
	'''
	def get_button_name(self, mouse_x_position, mouse_y_position):
		if self.get_button_mouseover(mouse_x_position, mouse_y_position):
			pressed_button = None
			for button in self.buttons.keys():
				if self.buttons[button].get_button_mouseover(mouse_x_position, mouse_y_position):
					pressed_button = button
			return pressed_button
	
	'''
	Goes through and updates all buttons, redrawing them if they are hovered.
	'''
	def set_button_highlight(self, DISPLAY_SCRABBLE, mouse_x_position, mouse_y_position):
		for button in self.buttons.values():
			button.set_button_highlight(DISPLAY_SCRABBLE, mouse_x_position, mouse_y_position)
			
	def get_button_mouseover(self, mouse_x_position, mouse_y_position):
		(left, top, width, height) = self.rect
		return mouse_x_position >= left and mouse_x_position <= left+width and mouse_y_position >= top and mouse_y_position <= top+height

	def draw_buttons(self, DISPLAY_SCRABBLE):
		pg.draw.rect(DISPLAY_SCRABBLE, self.background, self.rect)
		for button in self.buttons.values():
			button.draw_button(DISPLAY_SCRABBLE)

class Button():
	ON = "on"
	OFF = "off"
	
	initialized = False

	@staticmethod
	def initialize():
		pg.font.init()
		Button.FONT = pg.font.SysFont('bahnschrift', 28)
		Button.initialized = True
	
	def __init__(self, name, rect, color = None, backColor = None):
		# Make sure the fonts are set up:
		if not Button.initialized:
			Button.initialize()
			
		if color == None:
			color = board.Board.COLOR_DEFAULT
		if backColor == None:
			backColor = board.Board.COLOR_BACKGROUND
		
		self.name = name
		self.rect = rect
		self.last_drawn = Button.OFF
		self.color = color
		self.backColor = backColor

	def set_button_highlight(self, DISPLAY_SCRABBLE, mouse_x_position, mouse_y_position):
		if self.get_button_mouseover(mouse_x_position, mouse_y_position):
			self.draw(DISPLAY_SCRABBLE, self.color)
			self.last_drawn = Button.ON
		else:
			self.draw(DISPLAY_SCRABBLE, self.backColor)
			self.last_drawn = Button.OFF
			
	def get_button_mouseover(self, mouse_x_position, mouse_y_position):
		(left, top, width, height) = self.rect
		return mouse_x_position >= left and mouse_x_position <= left + width and mouse_y_position >= top and mouse_y_position <= top + height

	def draw(self, DISPLAY_SCRABBLE, backColor):
		pg.draw.rect(DISPLAY_SCRABBLE, backColor, self.rect)
		(left, top, width, height) = self.rect	
		text = Button.FONT.render(self.name, True, tile.Tile.COLOR_TILE_AREA, backColor)
		rect = text.get_rect()
		rect.center = (left + width / 2, top + height / 2)
		DISPLAY_SCRABBLE.blit(text, rect)

	def draw_button(self, DISPLAY_SCRABBLE):
		if self.last_drawn == Button.ON:
			self.draw(DISPLAY_SCRABBLE, self.color)
		elif self.last_drawn == Button.OFF:
			self.draw(DISPLAY_SCRABBLE, self.backColor)
			