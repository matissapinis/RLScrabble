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
import bag
import board
import dictionary
import player
import rack
import window

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
    game_board = board.Board()
    game_board.draw_board(DISPLAY_SCRABBLE)

    game_bag = bag.Bag()
    game_dictionary = dictionary.Dictionary()

    game_racks = []
    for i in range(2):
        game_racks.append(rack.Rack(game_bag))
    user_rack = game_racks[0]
    user_rack.draw_rack(DISPLAY_SCRABBLE)

    game_players = []
    for i in range(2):
        game_players.append(player.Player(i, game_board, game_bag, game_racks[i]))

    game_running = True

    mouse_moved = False
    mouse_clicked = False

    tile_picked = None

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
                ###print(game_board)
                tile_picked = game_players[0].pick_tile(mouse_x_pos, mouse_y_pos, game_board) #, tile_picked) # game_players[0])
                redraw_game(game_board, user_rack)

        pg.display.update()

## Should include drawing player scores:
def redraw_game(game_board, user_rack):
    game_board.draw_board(DISPLAY_SCRABBLE)
    user_rack.draw_rack(DISPLAY_SCRABBLE)

RLScrabble()
pg.quit()
quit()