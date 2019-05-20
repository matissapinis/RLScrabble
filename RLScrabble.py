'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

RLScrabble.py:
Contains the main part of the application that initiates the "Scrabble" game.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/05/20
'''

'''
To-do for RLScrabble.py:
-- 1) Make drawing positions dependent on window size from new window.py.
2) Highlight clicked rack tiles.
3) Make window and consequently tile size dependent on resolution / monitor size.
'''

# Libraries:
import pygame as pg

# Local files:
import bag, board, dictionary, rack, window

pg.init()
pg.font.init()

'''
DISPLAY_SCRABBLE = pg.display.set_mode((window.Window.SIZE_DISPLAY_WIDTH, window.Window.SIZE_DISPLAY_HEIGHT))
pg.display.set_caption("RLScrabble")
DISPLAY_SCRABBLE.fill(window.Window.COLOR_DISPLAY)
'''

## SIZE_DISPLAY_WINDOW = pg.display.Info()
SIZE_DISPLAY_WIDTH = 1200 # 1200 / 800 / SIZE_DISPLAY_WINDOW.current_w
SIZE_DISPLAY_HEIGHT = 900 # 900 / 600 / SIZE_DISPLAY_WINDOW.current_h

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
    ''' Removed since will only use HvA 1v1 mode:
    game_menu = menu.Menu()
    game_menu.draw_menu(DISPLAY_SCRABBLE)
    '''

    game_board = board.Board()
    game_board.draw_board(DISPLAY_SCRABBLE)

    p1_rack = rack.Rack()
    p1_rack.draw_rack(DISPLAY_SCRABBLE)

    game_bag = bag.Bag()

    game_dictionary = dictionary.Dictionary()

RLScrabble()
pg.quit()
quit()