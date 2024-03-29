# функция получения результата раунда, чтобы потом вывести на экран

from initialization import player, scores, computer

def getResult():

    if player.choice == computer.choice:
        scores.change_scores(1, 1)
    elif player.choice == 1 and computer.choice == 2:
        scores.change_scores(1, 0)
    elif player.choice == 2 and computer.choice == 3:
        scores.change_scores(1, 0)
    elif player.choice == 3 and computer.choice == 1:
        scores.change_scores(1, 0)
    else:
        scores.change_scores(0, 1)