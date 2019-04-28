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

SIZE_DISPLAY = (800, 600)

ScrabbleDisplay = pygame.display.set_mode(SIZE_DISPLAY)
pygame.display.set_caption("RLScrabble")

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        print(event)
    pygame.display.update()

pygame.quit()
quit()
