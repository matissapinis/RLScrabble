'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

rack.py:
Contains the class modelling player tile racks.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/05/20
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
                     (Rack.DISTANCE_TOP - 5 - 3 * board.Board.SIZE_SQUARE_GAP, Rack.DISTANCE_LEFT - 5 + 4 * board.Board.SIZE_SQUARE_GAP, ### Last terms in both arguments are hotfixes.
                      (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + 4) * Rack.DIMENSION_RACK + 7,
                      (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + 4) * 1 + 7))

        for i in range(Rack.DIMENSION_RACK):
            x_position = Rack.DISTANCE_TOP + i * (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + board.Board.SIZE_SQUARE_GAP) - 3 * board.Board.SIZE_SQUARE_GAP ### Last term is hotfix.
            tile.Tile.draw_tile(self.rack[i], DISPLAY_SCRABBLE, x_position, Rack.DISTANCE_LEFT) # + 4 * board.Board.SIZE_SQUARE_GAP) ### Last term of last argument is hotfix.
            '''
            x_position = Rack.DISTANCE_TOP + i * (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + board.Board.SIZE_SQUARE_GAP)

            pg.draw.rect(DISPLAY_SCRABBLE, tile.Tile.COLOR_TILE_BORDER,
                         (x_position + 2, Rack.DISTANCE_LEFT + 2, board.Board.SIZE_SQUARE_AREA - 3, board.Board.SIZE_SQUARE_AREA - 3))

            pg.draw.rect(DISPLAY_SCRABBLE, tile.Tile.COLOR_TILE_AREA,
                         (x_position + 3, Rack.DISTANCE_LEFT + 3, board.Board.SIZE_SQUARE_AREA - 5, board.Board.SIZE_SQUARE_AREA - 5))
            '''

    ### AttributeError: 'Rack' object has no attribute 'get_rack_index'
    def get_rack_position(self, x_position, y_position):
        x_position -= Rack.DISTANCE_LEFT + board.Board.SIZE_SQUARE_BORDER + board.Board.SIZE_SQUARE_GAP ### Not sure about last term.
        y_position -= Rack.DISTANCE_TOP + board.Board.SIZE_SQUARE_BORDER + board.Board.SIZE_SQUARE_GAP ### Not sure about last term.

        if x_position >= 0 and y_position >= 0 and y_position <= (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + board.Board.SIZE_SQUARE_GAP):
            if (x_position % (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + board.Board.SIZE_SQUARE_GAP) <
                    (board.Board.SIZE_SQUARE_AREA - board.Board.SIZE_SQUARE_BORDER - board.Board.SIZE_SQUARE_GAP) and
                    y_position % (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + board.Board.SIZE_SQUARE_GAP) <
                    (board.Board.SIZE_SQUARE_AREA - board.Board.SIZE_SQUARE_BORDER - board.Board.SIZE_SQUARE_GAP)):
                rack_pos = (int)(x_position / (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + board.Board.SIZE_SQUARE_GAP))

                if rack_pos < len(self.rack):
                    return rack_pos

        return -1


