# класс подсчета раундов
class NumberRounds:
    def __init__(self):
        self.rounds = 0

    def change_rounds(self, round):
        self.rounds = round

    def decrease_rounds(self):
        if self.rounds > 0:
            self.rounds -= 1