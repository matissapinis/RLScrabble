'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

rack.py:
Contains the class modelling the player-user and performing game moves.

Author:         Matīss Apinis (ma17058)
Date created:   2019/05/21
Date edited:    2019/05/21
'''

# Libraries:
import pygame as pg

# Local files:
import bag
import board
import rack
import tile

class Player:

    def __init__(self, game_board, game_bag, game_rack):
        self.rack = game_rack
        self.board = game_board
        self.bag = game_bag
        self.total_score = 0
        self.delta_score = 0

    def take_tiles(self):
        if not self.bag.is_bag_empty():
            count_missing_tiles = rack.Rack.DIMENSION_RACK - len(self.rack)

            for i in range(count_missing_tiles):
                pulled_tile = self.bag.pull_tile()

                if pulled_tile != None:
                    self.rack.append(pulled_tile)

        # If bag is empty and player rack is empty then the returned 'False' indicates the game has ended.
        elif len(self.tray) == 0:
            return False

        return True

    # def play_move(self):





