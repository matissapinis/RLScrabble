'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

RLScrabble.py:
Contains the main part of the application that initiates the "Scrabble" game.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/04/29
'''

'''
To-do for RLScrabble.py:
1) Make drawing positions dependent on window size from new window.py.
2) Highlight clicked rack tiles.
'''

# Libraries:
import pygame as pg

# Local files:
import board, rack

pg.init()
pg.font.init()

SIZE_DISPLAY_WIDTH = 1200
SIZE_DISPLAY_HEIGHT = 900

COLOR_DISPLAY = (255, 255, 255)

DISPLAY_SCRABBLE = pg.display.set_mode((SIZE_DISPLAY_WIDTH, SIZE_DISPLAY_HEIGHT))
pg.display.set_caption("RLScrabble")
DISPLAY_SCRABBLE.fill(COLOR_DISPLAY)

def RLScrabble():
    game_running = True

    mouse_moved = False
    mouse_clicked = False

    run_game()
    while game_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False
            elif event.type == pg.MOUSEMOTION:
                mouse_x_pos, mouse_y_pos = event.pos
                mouse_moved = True
            elif event.type == pg.MOUSEBUTTONUP:
                mouse_x_pos, mouse_y_pos = event.pos
                mouse_clicked = True
                print(event.pos) ##

            if mouse_clicked:
                ## TBC: Highlight clicked rack tile.
                assert("## TBC:")

        pg.display.update()

def run_game():
    game_board = board.Board()
    game_board.draw_board(DISPLAY_SCRABBLE)

    p1_rack = rack.Rack()
    p1_rack.draw_rack(DISPLAY_SCRABBLE)

RLScrabble()
pg.quit()
quit()