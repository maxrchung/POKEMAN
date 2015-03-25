import pygame

class TextScroll:
    def __init__(self, game=None, screen=None):
        self.text = ""
        self.game = game
        self.screen = screen

        # Take this eventually from game
        self.font25 = pygame.font.Font("PKMN RBYGSC.ttf", 25)

    def load(self, text):
        self.texts = self.textWrap(text)

    def textWrap(self, text):
        test = text
        textWrapped = []
        testRender = self.font25.render(test, 0, (0,0,0))
        if testRender.get_rect().width > 448:
            check = ""
            i = 0
            while i < len(text):
                check = text[:i+1]
                checkRender = self.font25.render(check, 0, (0,0,0))
                if checkRender.get_rect().width > 448:
                    j = i
                    while j != 0:
                        print(j)
                        if text[j] == " ":
                            print(text[:j])
                            textWrapped.append(self.font25.render(text[:j], 0, (0,0,0)))
                            text = text[j+1:]
                            i = 0
                            break
                        j -= 1
                i += 1
            textWrapped.append(self.font25.render(text, 0, (0,0,0)))
            print(text)
        return textWrapped

    def update(self):
        pass

    def draw(self):
        for i in range(len(self.texts)):
            self.screen.blit(self.texts[i], (18+10, 483-self.texts[i].get_rect().height/2 + 40*i))
