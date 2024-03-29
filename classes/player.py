# класс игроков

import pygame as pg
# для случайного выбооа компьютером используем модуль random, метод randint
from random import randint


class Player:

    def __init__(
        self,
        name = None,
        auto_game = False,
        screen = None,
        # список жестов в этой игре
        gesture_dict = {}
    ):
        #имя игрока
        self.name = name
        # флаг, что игрок компьютер
        self.auto_game = auto_game
        # выбор жеста для раунда (1, 2, 3)
        self.choice = None
        # флаг ротации, перемещения кулака на экране
        self.rotation = False
        # экран, на котором играет игрок
        self.screen = screen
        # список возможных жестов, словарь
        self.gesture_dict = gesture_dict

    # изображение жеста. Задаем нужный жест на каждом цикле игры
    def change_gesture(self,
                       image_file = None,
                       width = 0,
                       height = 0,
                       x = 0,
                       y = 0,
                       # для отображения (переворота) по горизонтали, либо вертикали
                       vertical = False,
                       horizontal = False):
        
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.vertical = vertical
        self.horizontal = horizontal
        # изображение жеста и его размеры и координаты на экране
        self.gesture = pg.transform.scale(pg.image.load(image_file),
                                          (width, height))
        # для отображения (переворота) по горизонтали, либо вертикали
        if self.vertical or self.horizontal:
            self.gesture = pg.transform.flip(self.gesture, self.vertical,
                                             self.horizontal)
        # координаты жеста на экране
        self.gesture_rect = self.gesture.get_rect(center = (x, y))
        # изображение жеста и его размеры и координаты на экране, для ротации
        self.gesture_rotate = pg.transform.scale(pg.image.load(image_file),
                                                 (width, height))
    
    # вывод на экран
    def blit_image(self, name_image, name_rect):
        self.screen.blit(name_image, name_rect)

    # выбор жеста для раунда (1, 2, 3)
    def set_choice(self, value = 0):
        self.choice = value if self.auto_game == False else randint(1, 3)

    # ротация жеста (перемещение кулака на экране)
    def change_rotation(self, rot):
        if self.rotation == False:
            self.rotation = True
            self.gesture_rotate = pg.transform.rotate(self.gesture, rot)
        else:
            self.rotation = False
            self.gesture_rotate = self.gesture

    # отображение выбранного жеста на экране по окончании раунда
    def view_choice(self):
        if self.choice == 1:
            self.change_gesture(self.gesture_dict['stone'], width = self.width, height = self.height, x = self.x, y = self.y, vertical = self.vertical, horizontal = self.horizontal)
            self.blit_image(self.gesture, self.gesture_rect)
        elif self.choice == 2:
            self.change_gesture(self.gesture_dict['scissors'], width = self.width, height = self.height, x = self.x, y = self.y, vertical = self.vertical, horizontal = self.horizontal)
            self.blit_image(self.gesture, self.gesture_rect)
        elif self.choice == 3:
            self.change_gesture(self.gesture_dict['paper'], width = self.width, height = self.height, x = self.x, y = self.y, vertical = self.vertical, horizontal = self.horizontal)
            self.blit_image(self.gesture, self.gesture_rect)
