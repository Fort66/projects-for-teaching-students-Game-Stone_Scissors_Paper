# класс подсчета очков
class Scores:
    def __init__(self):
        self.pl_score = 0
        self.comp_score = 0

    def change_scores(self, player_score = 0, computer_score = 0):
        self.pl_score += player_score
        self.comp_score += computer_score    
