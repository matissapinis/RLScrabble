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
import pygame as pg

# Local files:
import board, rack

pg.init()

SIZE_DISPLAY_WIDTH = 1200
SIZE_DISPLAY_HEIGHT = 900

DISPLAY_SCRABBLE = pg.display.set_mode((SIZE_DISPLAY_WIDTH, SIZE_DISPLAY_HEIGHT))
pg.display.set_caption("RLScrabble")
DISPLAY_SCRABBLE.fill((255, 255, 255))

def RLScrabble():
    game_running = True
    run_game()
    while game_running:
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYUP:
                game_running = False
        pg.display.update()

def run_game():
    game_board = board.Board()
    game_board.draw_board(DISPLAY_SCRABBLE)

    p1_rack = rack.Rack()
    p1_rack.draw_rack(DISPLAY_SCRABBLE)

RLScrabble()
pg.quit()
quit()