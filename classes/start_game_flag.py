# класс взвода флага старта игры, нажатие на кнопку старт
class StartGameFlag:
    def __init__(self):
        self.flag = False

    def change_start(self):
        self.flag = True if self.flag == False else False

