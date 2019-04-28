'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

RLScrabble.py:
Contains the main part of the application that initiates the "Scrabble" game.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/04/28
'''

import pygame
pygame.init()

SIZE_DISPLAY_WIDTH = 800
SIZE_DISPLAY_HEIGHT = 600
DISPLAY_SCRABBLE = pygame.display
DISPLAY_SCRABBLE.set_mode((SIZE_DISPLAY_WIDTH,SIZE_DISPLAY_HEIGHT))
DISPLAY_SCRABBLE.set_caption("RLScrabble")

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)

IMAGE_TILE = pygame.image.load("Tile.png")

def RLScrabble():
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        pygame.display.update()

RLScrabble()