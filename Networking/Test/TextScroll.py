import pygame

class TextScroll:
    def __init__(self, game=None, screen=None):
        self.text = ""
        self.game = game
        self.screen = screen

        # Take this eventually from game
        self.font25 = pygame.font.Font("PKMN RBYGSC.ttf", 25)

        # Scroll speed
        self.scrollClock = pygame.time.Clock()
        self.scrollTimer = 0
        self.scroll = 0

        # Blinking cursor
        self.blinkClock = pygame.time.Clock()
        self.blinkTimer = 0
        self.blink = False
        self.displayBlink = False
        self.scroll = 0 # index for where to scroll

        self.displayTexts = ['','','']

        self.cursor = pygame.image.load('select.png')

    def load(self, text):
        self.texts = self.textWrap(text)
        self.scroll = 0
        self.displayBlink = False

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
                        if text[j] == " ":
                            print(text[:j])
                            textWrapped.append(text[:j])
                            text = text[j+1:]
                            i = 0
                            break
                        j -= 1
                i += 1
            textWrapped.append(text)
        return textWrapped

    def update(self):
        if not self.displayBlink:
            self.scrollTimer += self.scrollClock.tick()
            if self.scrollTimer > 30:
                self.scrollTimer = 0
                tempScroll = self.scroll
                for index in range(len(self.texts)):
                    if tempScroll < len(self.texts[index]):
                        self.displayTexts[index] = self.texts[index][:tempScroll]
                        break
                    else:
                        self.displayTexts[index] = self.texts[index]
                        tempScroll -= len(self.texts[index])

                self.scroll += 1
                maxLength = 0
                for text in self.texts:
                    maxLength += len(text)
                if self.scroll > maxLength:
                    self.displayBlink = True

        elif self.displayBlink:
            self.blinkTimer += self.blinkClock.tick()
            if self.blinkTimer > 500:
                self.blinkTimer = 0
                if self.blink:
                    self.blink = False
                elif not self.blink:
                    self.blink = True


    def draw(self):
        for i in range(len(self.displayTexts)):
            render = self.font25.render(self.displayTexts[i], 0, (0,0,0))
            self.screen.blit(render, (18+10, 483-render.get_rect().height/2 + 40*i))

        if self.blink:
            self.screen.blit(self.cursor, (486 - 30, 582 - 30))
