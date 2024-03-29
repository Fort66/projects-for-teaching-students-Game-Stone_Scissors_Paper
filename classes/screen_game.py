# класс создания экрана игры

import pygame as pg

class ScreenGame:
    def change_screen(self, 
                # размеры по умоляанию
                 width = 800, 
                 height = 600, 
                 # частота кадров в секунду по умолчанию
                 FPS = 60, 
                 # цвет фона по умолчанию
                 fill_color = (0, 76, 153),
                 # заголовок окна по умолчанию
                 caption = '',
                 # иконка окна по умолчанию
                 icon = ''):
        
        self.display = pg.display
        self.width = width
        self.height = height
        self.color = fill_color
        self.win = self.display.set_mode((self.width, self.height))
        self.display.set_caption(caption)
        self.display.set_icon(pg.image.load(icon))
        self.caption = caption
        self.FPS = FPS