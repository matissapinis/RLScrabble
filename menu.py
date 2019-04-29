'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

menu.py:
Contains the class modelling the game menu for choosing game mode.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/29
Date edited:    2019/04/29
'''

# Libraries:
import pygame as pg

# Local files:
import tile

class Menu:
    DIMENSION_MENU = 3
    TYPE_BUTTON = ['HVH', 'HVA', 'AVA']
    SIZE_BUTTON = (0, 0, 0, 0)

    def __init__(self):
        self.button_list = Menu.TYPE_BUTTON
        self.button_area = Menu.SIZE_BUTTON
        self.button_color = tile.Tile.COLOR_TILE_AREA

    ## TBC:
    def draw_menu(self, DISPLAY_SCRABBLE):
        '''
        pg.draw.rect(DISPLAY_SCRABBLE, board.Board.COLOR_BACKGROUND,
                     (Rack.DISTANCE_TOP - 5, Rack.DISTANCE_LEFT - 5,
                      (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + 4) * Rack.DIMENSION_RACK + 7,
                      (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + 4) * 1 + 7))

        for x in range(Rack.DIMENSION_RACK):
            x_position = Rack.DISTANCE_TOP + x * (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + board.Board.SIZE_SQUARE_GAP)

            pg.draw.rect(DISPLAY_SCRABBLE, tile.Tile.COLOR_TILE_BORDER,
                         (x_position + 2, Rack.DISTANCE_LEFT + 2, board.Board.SIZE_SQUARE_AREA - 3, board.Board.SIZE_SQUARE_AREA - 3))

            pg.draw.rect(DISPLAY_SCRABBLE, tile.Tile.COLOR_TILE_AREA,
                         (x_position + 3, Rack.DISTANCE_LEFT + 3, board.Board.SIZE_SQUARE_AREA - 5, board.Board.SIZE_SQUARE_AREA - 5))
        '''
        return None

    ## TBC:
    def click_button(self, mouse_x_pos, mouse_y_pos):
        return None