'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

rack.py:
Contains the class modelling the player-user and performing game moves.

Author:         Matīss Apinis (ma17058)
Date created:   2019/05/21
Date edited:    2019/05/22
'''

'''
TO-DO:
1) Instances of tile_current get confusing -- remove them for straight returns and assignments etc.
'''

# Libraries:
import pygame as pg

# Local files:
import bag
import board
import rack
import tile

class Player:
    player_types = ['User', 'Computer']

    def __init__(self, type, game_board, game_bag, game_rack):
        self.type = self.player_types[type] ###
        self.rack = game_rack
        self.board = game_board
        self.bag = game_bag
        self.total_score = 0
        self.delta_score = 0
        self.hand = None


    ''' Attempts a temporary move before playing it: '''
    def temporary_move(self, x_position, y_position, tile_current):
        (board_x, board_y) = self.board.get_board_position(x_position, y_position)

        if board_x >= 0 and board_y >= 0:
            tile_previous = self.board.square[board_x][board_y][0]

            if tile_previous == None:
                self.square[board_x][board_y][0] = tile_current

                if tile_current.is_tile_blank():
                    return ("INPUT_LETTER", tile_current) ##

                return (True, tile_current)

        return (False, tile_current)

    ### TypeError: pick_tile() missing 1 required positional argument: 'game_board' :: =None awkward fix.
    def pick_tile(self, x_position, y_position, game_board):  # , tile_picked):
    #def pick_tile(self, x_position=None, y_position=None, game_board=None): #, tile_picked):
        if self.hand == None:
            tile_current = self.lift_board_tile(x_position, y_position)

            if tile_current != None:
                if tile_current.is_tile_blank():
                    tile_current.letter = ''
                self.rack.append(tile_current)
                return None
            else:
                tile_current = self.lift_rack_tile(x_position, y_position)
                if tile_current != None:
                    return tile_current
                else:
                    return None
        else:
            (move_success, move_tile) = self.temporary_move(x_position, y_position, self.hand)

            if move_success:
                if move_success == "INPUT_LETTER":
                    self.choose_letter(move_tile, DISPLAY_SCRABBLE)
                self.temporary_move()
                return None
            else:
                tile_current = self.lift_rack_tile(x_position, y_position)
                return tile_current


    def lift_board_tile(self, x_position, y_position):
        (board_x, board_y) = self.board.get_board_position(x_position, y_position)

        if board_x >= 0 and board_y >= 0:
            tile_current = self.board.square[board_x][board_y][0]

            if tile_current != None:
                self.board.square[board_x][board_y][0] = None
                return tile_current

        return None


    def lift_rack_tile(self, x_position, y_position):
        index_rack = self.rack.get_rack_position(x_position, y_position)

        if index_rack != -1 and index_rack < len(self.rack):
            if self.hand == None:
                self.hand = index_rack
                return self.rack[index_rack]
            else:
                (self.rack[index_rack], self.rack[self.hand]) = (self.rack[self.hand], self.rack[index_rack])

        self.hand = None
        return None

    def take_tiles(self):
        if not self.bag.is_bag_empty():
            count_missing_tiles = rack.Rack.DIMENSION_RACK - len(self.rack)

            for i in range(count_missing_tiles):
                pulled_tile = self.bag.pull_tile()

                if pulled_tile != None:
                    self.rack.append(pulled_tile)

        # If bag is empty and player rack is empty then the returned 'False' indicates the game has ended.
        elif len(self.rack) == 0:
            return False

        return True

    def choose_letter(self, tile_current):
        while tile_current.letter == '':
            for event in pg.event.get():
                if event.type == pg.KEYUP:
                    if event.key == pg.K_a:
                        tile_current.letter = 'A'
                    elif event.key == pg.K_b:
                        tile_current.letter = 'B'
                    elif event.key == pg.K_c:
                        tile_current.letter = 'C'
                    elif event.key == pg.K_d:
                        tile_current.letter = 'D'
                    elif event.key == pg.K_e:
                        tile_current.letter = 'E'
                    elif event.key == pg.K_f:
                        tile_current.letter = 'F'
                    elif event.key == pg.K_g:
                        tile_current.letter = 'G'
                    elif event.key == pg.K_h:
                        tile_current.letter = 'H'
                    elif event.key == pg.K_i:
                        tile_current.letter = 'I'
                    elif event.key == pg.K_j:
                        tile_current.letter = 'J'
                    elif event.key == pg.K_k:
                        tile_current.letter = 'K'
                    elif event.key == pg.K_l:
                        tile_current.letter = 'L'
                    elif event.key == pg.K_m:
                        tile_current.letter = 'M'
                    elif event.key == pg.K_n:
                        tile_current.letter = 'N'
                    elif event.key == pg.K_o:
                        tile_current.letter = 'O'
                    elif event.key == pg.K_p:
                        tile_current.letter = 'P'
                    elif event.key == pg.K_q:
                        tile_current.letter = 'Q'
                    elif event.key == pg.K_r:
                        tile_current.letter = 'R'
                    elif event.key == pg.K_s:
                        tile_current.letter = 'S'
                    elif event.key == pg.K_t:
                        tile_current.letter = 'T'
                    elif event.key == pg.K_u:
                        tile_current.letter = 'U'
                    elif event.key == pg.K_v:
                        tile_current.letter = 'V'
                    elif event.key == pg.K_w:
                        tile_current.letter = 'W'
                    elif event.key == pg.K_x:
                        tile_current.letter = 'X'
                    elif event.key == pg.K_y:
                        tile_current.letter = 'Y'
                    elif event.key == pg.K_z:
                        tile_current.letter = 'Z'

            pg.display.update()

    # def play_move(self):



