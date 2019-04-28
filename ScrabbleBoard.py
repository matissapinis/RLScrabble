'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

ScrabbleBoard.py:
Contains the class modelling the basic "Scrabble" game board.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/04/28
'''

import pygame
pygame.init()

SIZE_DISPLAY_WIDTH = 800
SIZE_DISPLAY_HEIGHT = 600

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)

IMAGE_TILE = pygame.image.load("Tile.png")

ScrabbleDisplay = pygame.display.set_mode((SIZE_DISPLAY_WIDTH,SIZE_DISPLAY_HEIGHT))
ScrabbleDisplay.fill(COLOR_WHITE)
pygame.display.set_caption("RLScrabble")

pixelArray = pygame.PixelArray(ScrabbleDisplay)

game_running = True

class ScrabbleBoard:
    DIMENSION_BOARD = 15
    POSITION_INITIAL = (7, 7)

    SIZE_SQUARE_AREA = 32
    SIZE_SQUARE_BORDER = 4
    SIZE_SQUARE_GAP = 4

    def __init__(self):
        '''
        Create an empty 2D array as the basis of the board:
        '''
        self.square = []
        for x in range(self.DIMENSION_BOARD):
            self.square.append([])
            for y in range(self.DIMENSION_BOARD):
                self.square[x].append((None, None))

    def draw_board(self):
        for row in range(self.DIMENSION_BOARD):
            for column in range(self.DIMENSION_BOARD):
                x = row * (self.SIZE_SQUARE_AREA + self.SIZE_SQUARE_BORDER) + self.SIZE_SQUARE_GAP
                y = column * (self.SIZE_SQUARE_AREA + self.SIZE_SQUARE_BORDER) + self.SIZE_SQUARE_GAP

                pygame.draw.rect(ScrabbleDisplay, COLOR_BLUE, (x_position, y_position, (self.SIZE_SQUARE_AREA + self.SIZE_SQUARE_BORDER), (self.SIZE_SQUARE_AREA + self.SIZE_SQUARE_BORDER)))

                # ScrabbleDisplay.blit(IMAGE_TILE, (x_position,y_position))

    def game_loop():
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                # print(event)
            board = ScrabbleBoard()
            ScrabbleDisplay.fill(COLOR_WHITE)
            board.draw_board()

            pygame.display.update()

game = ScrabbleBoard()
game.game_loop()

pygame.quit()
quit()
