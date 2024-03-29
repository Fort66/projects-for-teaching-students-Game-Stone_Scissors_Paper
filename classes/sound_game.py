# класс вывода фонового звука и звука событий в игре
import pygame as pg
pg.init()

class SoundGame:
    def __init__(self):
        self.background = None
        self.music = None

    def play_background(self, background = None):
        if background:
            self.background = pg.mixer.music.load(background)
            pg.mixer.music.set_volume(0.2)
            pg.mixer.music.play(-1)

    def play_game(self, music_file = None):
        if music_file:
            self.music = pg.mixer.Sound(music_file)
            pg.mixer.Sound.set_volume(self.music, 0.4)
            self.music.play()



