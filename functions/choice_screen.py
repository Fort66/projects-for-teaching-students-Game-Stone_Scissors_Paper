# экран выбора пользователем одного  из трех жестов

from initialization import btn_stone, btn_scissors, btn_paper, screen, player, computer, userChoice_flag

def choiceScreen():
    # рисуем кнопки камень, ножницы, бумага
    btn_stone.draw(screen.win)
    btn_scissors.draw(screen.win)
    btn_paper.draw(screen.win)
    player.blit_image(player.gesture, player.gesture_rect)
    computer.blit_image(computer.gesture, computer.gesture_rect)

    # обрабатываем нажатия кнопок камень, ножницы, бумага
    if btn_stone.is_clicked:
        player.set_choice(1)

    if btn_scissors.is_clicked:
        player.set_choice(2)

    if btn_paper.is_clicked:
        player.set_choice(3)
    # обнуляем флаги кнопок камень, ножницы, бумага, если они нажаты и взводим флаги выбора юзера и компьютера
    if btn_stone.is_clicked or btn_scissors.is_clicked or btn_paper.is_clicked:
        btn_stone.is_clicked = False
        btn_scissors.is_clicked = False
        btn_paper.is_clicked = False
        computer.set_choice()
        userChoice_flag.change_choice()
        
        
            