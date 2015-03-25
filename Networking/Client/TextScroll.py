import pygame
from Game import *
from collections import deque

class TextScroll:
    def __init__(self, game):
        self.text = ""
        self.game = game

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
        self.texts = []

        self.cursor = pygame.image.load('select.png')
        self.display = False

        self.store = deque()

    def load(self, text):
        textWrapped = self.textWrap(text)
        print("Loaded into store:",textWrapped)
        print('TextScroll Load running!')
        while len(textWrapped) > 3:
            self.store.append(textWrapped)
            textWrapped = textWrapped[3:]

        self.display = True
        self.texts = self.store.popleft()

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
            print(text)
        return textWrapped

    def update(self):
        if not self.display:
            return

        if not self.displayBlink:
            self.scrollTimer += self.scrollClock.tick()
            if self.scrollTimer > 30:
                if self.game.eventManager.enter:
                    for index in range(len(self.texts)):
                        self.displayTexts[index] = self.texts[index]
                        self.displayBlink = True
                else:
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
            if self.game.eventManager.enter:
                if self.store: # If there are more messages
                    print('Going to next store...')
                    self.texts = self.store.popleft()
                    self.displayTexts = ['','','']
                    print(self.texts)
                    self.scroll = 0
                    self.displayBlink = False
                else:
                    print('TextScroll finished displaying')
                    self.scroll = 0
                    self.displayBlink = False
                    self.texts = []
                    self.displayTexts = ['','','']
                    self.display = False

    def draw(self):
        if self.display:
            for i in range(len(self.displayTexts)):
                render = self.font25.render(self.displayTexts[i], 0, (0,0,0))
                self.game.screen.blit(render, (18+10, 483-render.get_rect().height/2 + 40*i))

            if self.blink:
                self.game.screen.blit(self.cursor, (486 - 30, 582 - 30))
