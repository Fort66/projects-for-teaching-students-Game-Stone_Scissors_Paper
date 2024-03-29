# класс флага выбора игроков
class UserChoiceFlag:
    def __init__(self):
        self.flag = False

    def change_choice(self):
        self.flag = True if self.flag == False else False

