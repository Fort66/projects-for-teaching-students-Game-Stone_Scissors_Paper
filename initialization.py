# испортируемвсе написанные классы из всех файлов, из папки classes.
from classes.screen_game import ScreenGame
from classes.player import Player
from classes.button import Button
from classes.sound_game import SoundGame
from classes.draw_text import DrawText
from classes.number_rounds import NumberRounds
from classes.scores import Scores
from classes.user_choice_flag import UserChoiceFlag
from classes.start_game_flag import StartGameFlag
from classes.colors import Colors
from classes.fonts import Fonts




# создаем экземпляр класса окна игры, передаем в него размеры, заголовок, иконку
screen = ScreenGame()
screen.change_screen(width = 800, height = 600, caption = 'Камень Ножницы Бумага', icon = 'images/scissors.png')

# создаем экземпляр класса игрока player, computer. В инит класса сразу передаем словарь со всеми жестами для этой игры
player = Player(name = 'Игрок', 
                screen = screen.win, 
                gesture_dict = {
                    'stone': 'images/stone.png',
                    'scissors': 'images/scissors.png',
                    'paper': 'images/paper.png',
                    'start': 'images/start.png',
                })
computer = Player(name='Компьютер', 
                  auto_game = True, 
                  screen = screen.win,
                  gesture_dict = {
                        'stone': 'images/stone.png',
                        'scissors': 'images/scissors.png',
                        'paper': 'images/paper.png',
                        'start': 'images/start.png',
                  })

# создаем разные кнопки (экземпляры класса button)
btn_start = Button(x = screen.width / 2 - 100, y = screen.height / 2, width = 200, height = 50, text = 'Старт')
btn_stone = Button(x = screen.width / 2 - 175, y = screen.height / 2 + 100, width = 100, height = 50, text = 'Камень')
btn_scissors = Button(x = screen.width / 2 - 50, y = screen.height / 2 + 100, width = 100, height = 50, text = 'Ножницы')
btn_paper = Button(x = screen.width / 2 + 75, y = screen.height / 2 + 100, width = 100, height = 50, text = 'Бумага')

# создаем экземпляр класса звуков игры (экземпляр класса sound_game)
sound_game = SoundGame()

# создаем экземпляр класса для рисования текста (экземпляр класса draw_text)
draw_text = DrawText()

# создаем экземпляр класса для работы с количеством раундов (экземпляр класса)
number_rounds = NumberRounds()

# создаем экземпляр класса для работы с очками (экземпляр класса)
scores = Scores()

# создаем экземпляр класса для работы с флагами (экземпляр класса) выбора пользователя
userChoice_flag = UserChoiceFlag()

# создаем экземпляр класса для работы с флагами (экземпляр класса) старт игры, нажатие кнопки старт
startGame_flag = StartGameFlag()

# создаем экземпляр класса для работы с цветами (экземпляр класса)
colors = Colors()

# создаем экземпляр класса для работы с шрифтами (экземпляр класса)
fonts = Fonts()