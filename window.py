'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

window.py:
Contains the parameters for game window size and looks.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/29
Date edited:    2019/04/29
'''

# Libraries:

class Window:
    ## SIZE_DISPLAY_WINDOW = pg.display.Info()
    SIZE_DISPLAY_WIDTH = 1200 # 1200 / 800 / SIZE_DISPLAY_WINDOW.current_w
    SIZE_DISPLAY_HEIGHT = 900 # 900 / 600 / SIZE_DISPLAY_WINDOW.current_h

    COLOR_DISPLAY = (255, 255, 255)

    def __init__(self):
        self.window_width = Window.SIZE_DISPLAY_WIDTH
        self.window_height = Window.SIZE_DISPLAY_HEIGHT

    def window_size(self):
        return (Window.SIZE_DISPLAY_WIDTH, Window.SIZE_DISPLAY_HEIGHT)