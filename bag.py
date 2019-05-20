'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

bag.py:
Contains the class modelling the game bag of tiles.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/05/20
'''

# Libraries:
import pygame as pg
from random import shuffle

# Local files:
import tile

class Bag:
    # Dictionary of tiles by letter as key with 2-tuple as value containing its score value and copy count in bag:
    tile_set = {
        'A': (1, 11),
        'Ā': (2, 4),
        'B': (5, 1),
        'C': (5, 1),
        'Č': (10, 1),
        'D': (3, 3),
        'E': (1, 6),
        'Ē': (4, 2),
        'F': (10, 1),
        'G': (5, 1),
        'Ģ': (10, 1),
        'H': (10, 1),
        'I': (1, 9),
        'Ī': (4, 2),
        'J': (4, 2),
        'K': (2, 4),
        'Ķ': (10, 1),
        'L': (2, 3),
        'Ļ': (8, 1),
        'M': (2, 4),
        'N': (2, 4),
        'Ņ': (6, 1),
        'O': (3, 3),
        'P': (2, 3),
        'R': (1, 5),
        'S': (1, 8),
        'Š': (6, 1),
        'T': (1, 6),
        'U': (1, 5),
        'Ū': (6, 1),
        'V': (3, 3),
        'Z': (3, 2),
        'Ž': (8, 1),
        '':  (None, 2),
    }

    def __init__(self):
        self.tiles = []

        for letter, tuple in self.tile_set.items():
            value = tuple[0]
            count = tuple[1]

            for i in range(count):
                self.tiles.append(tile.Tile(letter, value))

        shuffle(self.tiles)