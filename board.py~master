'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

board.py:
Contains the class modelling the basic game board.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/04/28
'''

# Libraries:
import pygame

# Local files:
# import RLScrabble

class Board:
    DIMENSION_BOARD = 15
    POSITION_INITIAL = (7, 7)

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

    COLOR_BACKGROUND = (15, 75, 0)
    COLOR_TILE_BORDER = (100, 100, 100)

    COLOR_DEFAULT = (30, 150, 0)
    COLOR_LETTER_2X = (100, 200, 255)
    COLOR_LETTER_3X = (0, 100, 255)
    COLOR_WORD_2X = (255, 100, 0)
    COLOR_WORD_3X = (255, 0, 0)

    SIZE_SQUARE_AREA = 48
    SIZE_SQUARE_BORDER = 0
    SIZE_SQUARE_GAP = 4

    # DISTANCE_TOP = RLScrabble.SIZE_DISPLAY_HEIGHT * 0.05
    # DISTANCE_LEFT = RLScrabble.SIZE_DISPLAY_WIDTH * 0.05

    DISTANCE_TOP = 1200 * 0.05
    DISTANCE_LEFT = 900 * 0.05

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

    def draw_board(self, DISPLAY_SCRABBLE):
        pygame.draw.rect(DISPLAY_SCRABBLE, Board.COLOR_BACKGROUND,
                         (Board.DISTANCE_TOP - 5, Board.DISTANCE_LEFT - 5,
                          (Board.SIZE_SQUARE_AREA + Board.SIZE_SQUARE_BORDER + 4) * Board.DIMENSION_BOARD + 8,
                          (Board.SIZE_SQUARE_AREA + Board.SIZE_SQUARE_BORDER + 4) * Board.DIMENSION_BOARD + 8))

        for x in range(Board.DIMENSION_BOARD):
            for y in range(Board.DIMENSION_BOARD):
                x_position = Board.DISTANCE_TOP + x * (Board.SIZE_SQUARE_AREA + Board.SIZE_SQUARE_BORDER + Board.SIZE_SQUARE_GAP)
                y_position = Board.DISTANCE_LEFT + y * (Board.SIZE_SQUARE_AREA + Board.SIZE_SQUARE_BORDER + Board.SIZE_SQUARE_GAP)

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

                pygame.draw.rect(DISPLAY_SCRABBLE, Board.COLOR_TILE_BORDER,
                                 (x_position + 2, y_position + 2, Board.SIZE_SQUARE_AREA - 3, Board.SIZE_SQUARE_AREA - 3))

                pygame.draw.rect(DISPLAY_SCRABBLE, square_color,
                                 (x_position + 3, y_position + 3, Board.SIZE_SQUARE_AREA - 5, Board.SIZE_SQUARE_AREA - 5))