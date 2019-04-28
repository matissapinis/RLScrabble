'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

rack.py:
Contains the class modelling player tile racks.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/04/28
'''

'''
To-do for rack.py:
1) Shuffle k <= 7 tiles.
2) Move COLOR_TILE to a new tile.py.
3) Tidy up and explain long drawing parameters.
4) Make drawing positions dependent on window size from new window.py.
'''

import pygame as pg

import board

class Rack:
    DIMENSION_RACK = 7

    COLOR_TILE = (230, 230, 230)

    DISTANCE_TOP = 270 - 2
    DISTANCE_LEFT = 840

    def __init__(self):
        self.rack = []
        for x in range(Rack.DIMENSION_RACK):
            self.rack.append(None)

    def is_empty_rack(self):
        return len(self.rack) == 0

    def is_full_rack(self):
        return len(self.rack) == Rack.DIMENSION_RACK

    def draw_rack(self, DISPLAY_SCRABBLE):
        pg.draw.rect(DISPLAY_SCRABBLE, board.Board.COLOR_BACKGROUND,
                     (Rack.DISTANCE_TOP - 5, Rack.DISTANCE_LEFT - 5,
                      (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + 4) * Rack.DIMENSION_RACK + 7,
                      (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + 4) * 1 + 7))

        for x in range(Rack.DIMENSION_RACK):
            x_position = Rack.DISTANCE_TOP + x * (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + board.Board.SIZE_SQUARE_GAP)

            pg.draw.rect(DISPLAY_SCRABBLE, board.Board.COLOR_TILE_BORDER,
                         (x_position + 2, Rack.DISTANCE_LEFT + 2, board.Board.SIZE_SQUARE_AREA - 3, board.Board.SIZE_SQUARE_AREA - 3))

            pg.draw.rect(DISPLAY_SCRABBLE, Rack.COLOR_TILE,
                         (x_position + 3, Rack.DISTANCE_LEFT + 3, board.Board.SIZE_SQUARE_AREA - 5, board.Board.SIZE_SQUARE_AREA - 5))

