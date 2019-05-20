'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

rack.py:
Contains the class modelling player tile racks.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/04/29
'''

'''
To-do for rack.py:
1) Shuffle k <= 7 tiles.
2) Tidy up and explain long drawing parameters.
3) Make drawing positions dependent on window size from new window.py.
'''

# Libraries:
import pygame as pg

# Local files:
import bag
import board
import tile

class Rack:
    DIMENSION_RACK = 7

    DISTANCE_TOP = 270 - 2
    DISTANCE_LEFT = 840

    def __init__(self, game_bag):
        self.rack = []
        for i in range(Rack.DIMENSION_RACK):
            self.rack.append(game_bag.pull_tile())

    def is_rack_empty(self):
        return len(self.rack) == 0

    def is_rack_full(self):
        return len(self.rack) == Rack.DIMENSION_RACK

    def draw_rack(self, DISPLAY_SCRABBLE):
        pg.draw.rect(DISPLAY_SCRABBLE, board.Board.COLOR_BACKGROUND,
                     (Rack.DISTANCE_TOP - 5, Rack.DISTANCE_LEFT - 5,
                      (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + 4) * Rack.DIMENSION_RACK + 7,
                      (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + 4) * 1 + 7))

        for i in range(Rack.DIMENSION_RACK):
            x_position = Rack.DISTANCE_TOP + i * (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + board.Board.SIZE_SQUARE_GAP)
            tile.Tile.draw_tile(self.rack[i], DISPLAY_SCRABBLE, x_position, Rack.DISTANCE_LEFT)
            '''
            x_position = Rack.DISTANCE_TOP + i * (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + board.Board.SIZE_SQUARE_GAP)

            pg.draw.rect(DISPLAY_SCRABBLE, tile.Tile.COLOR_TILE_BORDER,
                         (x_position + 2, Rack.DISTANCE_LEFT + 2, board.Board.SIZE_SQUARE_AREA - 3, board.Board.SIZE_SQUARE_AREA - 3))

            pg.draw.rect(DISPLAY_SCRABBLE, tile.Tile.COLOR_TILE_AREA,
                         (x_position + 3, Rack.DISTANCE_LEFT + 3, board.Board.SIZE_SQUARE_AREA - 5, board.Board.SIZE_SQUARE_AREA - 5))

            '''


