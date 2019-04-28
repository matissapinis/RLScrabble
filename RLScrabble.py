'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

RLScrabble.py:
Contains the main part of the application that initiates the "Scrabble" game.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/04/28
'''

# Libraries:
import pygame

# Local files:
import board

pygame.init()

SIZE_DISPLAY_WIDTH = 1200
SIZE_DISPLAY_HEIGHT = 900

DISPLAY_SCRABBLE = pygame.display.set_mode((SIZE_DISPLAY_WIDTH,SIZE_DISPLAY_HEIGHT))
pygame.display.set_caption("RLScrabble")
DISPLAY_SCRABBLE.fill(board.Board.COLOR_WHITE)

def RLScrabble():
    game_running = True
    run_game()
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYUP:
                game_running = False
        pygame.display.update()

def run_game():
    game_board = board.Board()
    game_board.draw_board(DISPLAY_SCRABBLE)

RLScrabble()
pygame.quit()
quit()