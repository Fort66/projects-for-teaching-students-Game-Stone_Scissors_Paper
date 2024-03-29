# rkfcc wbrkf buhs

import pygame as pg
from pygame.locals import *
from initialization import player, computer, btn_start, btn_stone, btn_paper, btn_scissors, sound_game, screen, number_rounds, userChoice_flag, startGame_flag, scores

from functions.view_text import view_text
from functions.start_screen import startScreen
from functions.choice_screen import choiceScreen
from functions.rotation_screen import rotationScreen
from functions.get_result import getResult

# инициализация Pygame
pg.init()

# инициализация таймера для фпс
clock = pg.time.Clock()

class Game:
    def __init__(self):
        # количество перемещений руки вверх и вниз, каждый жест это 1, всего 6 для ротации
        self.counter_rotation = 0
        # флаг для запуска игры
        self.running = True

    # обработка событий игры, кнопки закрытия окна, кнопки запуска игры, кнопки выбора
    def event_game(self):
        for event in pg.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
            elif event.type == QUIT:
                self.running = False

            btn_start.handle_event(event)
            btn_stone.handle_event(event)
            btn_paper.handle_event(event)
            btn_scissors.handle_event(event)

    # запуск игры, основной цикл игры, обновление экрана, запуск таймера для фпс,
    def run_game(self):
        number_rounds.change_rounds(5)
        sound_game.play_background('music/background_music.mp3')

        while self.running:
            clock.tick(screen.FPS)
            screen.win.fill(screen.color)

            self.event_game()
            view_text()

            if not startGame_flag.flag and not userChoice_flag.flag:
                startScreen()

            elif startGame_flag.flag and not userChoice_flag.flag:
                self.counter_rotation = 6
                choiceScreen()

                
            elif startGame_flag.flag and userChoice_flag.flag:
                if self.counter_rotation > 0:
                    self.counter_rotation -= 1
                    rotationScreen()
                    if self.counter_rotation % 2 != 0: 
                        sound_game.play_game('music/counting_down.mp3')

                    pg.display.update()
                    pg.time.delay(500)

                else:
                    getResult()

                    sound_game.play_game('music/victory.mp3')
                    screen.win.fill(screen.color)
                    player.view_choice()
                    computer.view_choice()
                    startGame_flag.change_start()
                    userChoice_flag.change_choice()
                    number_rounds.decrease_rounds()
                    view_text()


                    pg.display.update()
                    pg.time.delay(3000)


            if number_rounds.rounds == 0:
                number_rounds.change_rounds(5)
                scores.pl_score = 0
                scores.comp_score = 0

            pg.display.update()

        pg.quit()