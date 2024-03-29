# класс вывода текста на экран
class DrawText:
    def create_text(self, 
                    screen = None, 
                    font = None, color = None, 
                    x = 0, 
                    y = 0, 
                    text = None):
        self.text = text if type(text) == str else str(text)

        self.text = font.render(self.text, True, color)
        screen.blit(self.text, (x, y))

