'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

menu.py:
Contains the class implementing the game menu for choosing game mode.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/29
Date edited:    2019/05/20
'''

''' Removed since will only use HvA 1v1 mode:
# Libraries:
import pygame as pg

# Local files:
import board, tile, window

class Menu:
    DIMENSION_MENU = 3
    TYPE_BUTTON = ['HVH', 'HVA', 'AVA']

    COLOR_BUTTON_AREA = board.Board.COLOR_BACKGROUND

    SIZE_BUTTON_WIDTH = 1200 * 0.2
    SIZE_BUTTON_HEIGHT = board.Board.SIZE_SQUARE_AREA

    SIZE_DISPLAY_WIDTH = 1200
    SIZE_DISPLAY_HEIGHT = 900

    PROPORTION_LEFT = 0.3
    PROPORTION_TOP = 0.4

    DISTANCE_LEFT = SIZE_DISPLAY_WIDTH * PROPORTION_LEFT
    DISTANCE_TOP = SIZE_DISPLAY_HEIGHT * PROPORTION_TOP

    OFFSET_LEFT = 5
    OFFSET_TOP = 5

    def __init__(self):
        self.button_list = Menu.TYPE_BUTTON
        self.button_width = Menu.SIZE_BUTTON_WIDTH
        self.button_height = Menu.SIZE_BUTTON_HEIGHT
        self.button_color = tile.Tile.COLOR_TILE_AREA

    ## TBC:
    def draw_menu(self, DISPLAY_SCRABBLE):
        DISPLAY_SCRABBLE.fill(window.Window.COLOR_DISPLAY)

        x_position = Menu.DISTANCE_LEFT
        y_position = Menu.DISTANCE_TOP

        pg.draw.rect(DISPLAY_SCRABBLE, board.Board.COLOR_BACKGROUND,
                     (x_position - Menu.OFFSET_LEFT, y_position - Menu.OFFSET_TOP,
                      (1 - 2 * Menu.PROPORTION_LEFT) * Menu.SIZE_DISPLAY_WIDTH + 2 * Menu.OFFSET_LEFT,
                      (1 - 2 * Menu.PROPORTION_TOP) * Menu.SIZE_DISPLAY_HEIGHT + 2 * Menu.OFFSET_TOP))

        for y in range(Menu.DIMENSION_MENU):
            pg.draw.rect(DISPLAY_SCRABBLE, tile.Tile.COLOR_TILE_BORDER,
                         (x_position - 2, y_position - 2,
                          (1 - 2 * Menu.PROPORTION_LEFT) * Menu.SIZE_DISPLAY_WIDTH + 4,
                          (1 - 2 * Menu.PROPORTION_TOP) * Menu.SIZE_DISPLAY_HEIGHT + 4))

            pg.draw.rect(DISPLAY_SCRABBLE, tile.Tile.COLOR_TILE_AREA,
                         (x_position, y_position,
                          (1 - 2 * Menu.PROPORTION_LEFT) * Menu.SIZE_DISPLAY_WIDTH,
                          (1 - 2 * Menu.PROPORTION_TOP) * Menu.SIZE_DISPLAY_HEIGHT))

            y_position += Menu.SIZE_DISPLAY_HEIGHT + 4
        
        ###
        pg.draw.rect(DISPLAY_SCRABBLE, tile.Tile.COLOR_TILE_BORDER,
                     (x_position, y_position,
                      (1 - 2 * Menu.PROPORTION_LEFT) * Menu.SIZE_DISPLAY_WIDTH,
                      (1 - 2 * Menu.PROPORTION_TOP) * Menu.SIZE_DISPLAY_HEIGHT))

        pg.draw.rect(DISPLAY_SCRABBLE, tile.Tile.COLOR_TILE_BORDER, (Menu.DISTANCE_LEFT + 2, y_position + 10, Menu.SIZE_BUTTON_WIDTH * 1.55 - 3, Menu.SIZE_BUTTON_HEIGHT - 3))

        pg.draw.rect(DISPLAY_SCRABBLE, tile.Tile.COLOR_TILE_AREA, (Menu.DISTANCE_LEFT + 3, y_position + 11, Menu.SIZE_BUTTON_WIDTH * 1.55 - 5, Menu.SIZE_BUTTON_HEIGHT - 5))
        ###

    ## TBC:
    def click_button(self, mouse_x_pos, mouse_y_pos):
        return None
'''