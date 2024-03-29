# экран ротации, т.е. тот экран на которм имитируется махание руки игроками

from initialization import player, computer

def rotationScreen():
    # передаем в классы изменения ротации игрока и компьютера, т.е. угол поворота руки игрока и компьютера, и рисуем это на экране
    player.change_rotation(-45)
    computer.change_rotation(45)
    player.blit_image(player.gesture_rotate, player.gesture_rect)
    computer.blit_image(computer.gesture_rotate, computer.gesture_rect)
    