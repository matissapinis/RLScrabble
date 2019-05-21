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




