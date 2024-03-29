# функция оформления начального экрана
# импорт стартовой кнопки, объектов игрок, компьютера, окна игры и логического флага старта игры
from initialization import btn_start, player, computer, screen, startGame_flag


def startScreen():
    # выводим кнопку старт
    btn_start.draw(screen.win)
    # задаем начальный жест кулаков на старте игры для компа и игрока и выводим их на экрен
    player.change_gesture(player.gesture_dict['start'], width = 144, height = 183, x = 100, y = screen.height / 2)
    player.blit_image(player.gesture, player.gesture_rect)
    computer.change_gesture(computer.gesture_dict['start'], width = 144, height = 183, x = screen.width - 100, y = screen.height / 2, vertical = True)
    computer.blit_image(computer.gesture, computer.gesture_rect)

    # если кнопка старт нажата, то изменяем флаг старта игры и завершаем функцию
    if btn_start.is_clicked:
        btn_start.is_clicked = False
        startGame_flag.change_start()