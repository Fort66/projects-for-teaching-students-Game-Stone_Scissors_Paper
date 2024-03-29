# функция, которая выводит каждый конкретный текст в заданном месте экрана (слово, или строку) на основании класса draw_text (экземпляр класса)

from initialization import player, computer, draw_text, screen, scores, number_rounds, colors, fonts


def view_text():

    draw_text.create_text(
            screen = screen.win,
            font = fonts.roboto,
            color = colors.white,
            x = 30,
            y = 50,
            text = player.name
        )
    draw_text.create_text(
            screen = screen.win,
            font = fonts.roboto,
            color = colors.white,
            x = screen.width - 200,
            y = 50,
            text = computer.name
        )
    draw_text.create_text(
            screen = screen.win,
            font = fonts.roboto,
            color = colors.white,
            x = screen.width /2 - 40,
            y = screen.height - 100,
            text = 'Счет'
        )
    draw_text.create_text(
            screen = screen.win,
            font = fonts.arial,
            color = colors.yellow,
            x = 80,
            y = screen.height - 50,
            text = scores.pl_score
        )
    draw_text.create_text(
            screen = screen.win,
            font = fonts.arial,
            color = colors.yellow,
            x = screen.width - 100,
            y = screen.height - 50,
            text = scores.comp_score
        )

    draw_text.create_text(
            screen = screen.win,
            font = fonts.arial,
            color = colors.yellow,
            x = screen.width / 2 - 150,
            y = 50,
            text = 'Осталось раундов'
        )
    draw_text.create_text(
            screen = screen.win,
            font = fonts.arial,
            color = colors.yellow,
            x = screen.width / 2 - 20,
            y = screen.height - 500,
            text = number_rounds.rounds
        )