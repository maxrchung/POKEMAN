from Game import *
from LetterSelector import *
from BlinkCursor import *

class TextInput:
    def __init__(self, game):
        self.game = game

        # The given input so far
        self.input = ''
        
        # We use the index to know what letter we're on
        self.index = 0

        # We have 30 inputs in total, represented by 5 rows of 6 letters
        self.rows = 5
        self.cols = 6
        self.letters = ['A','B','C','D','E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','SPC','DEL','CLR','ENT']
        
        self.choose = self.game.font32.render("CHOOSE A NAME: ", 0, (0, 0, 0))

        self.blinkCursor = BlinkCursor(self)
        self.letterSelector = LetterSelector(self)

        # Clock for the cursor/blink display
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.display = 1

    def update(self):
        self.timer += self.clock.tick()
        if self.timer > 500:
            self.display *= -1
            self.timer = 0

        if self.game.eventManager.left:
            if self.index > 0:
                self.index -= 1
        elif self.game.eventManager.up:
            if self.index > 5:
                self.index -= 6
        elif self.game.eventManager.right:
            if self.index < 29:
                self.index += 1
        elif self.game.eventManager.down:
            if self.index < 24:
                self.index += 6
        elif self.game.eventManager.enter:
            if self.letters[self.index] == 'SPC':
                if len(self.input) < 10:
                    self.input += ' '
            elif self.letters[self.index] == 'DEL':
                if len(self.input) > 0:
                    self.input = self.input[:-1]
            elif self.letters[self.index] == 'CLR':
                self.input = ''
            elif self.letters[self.index] == 'ENT':
                self.game.p1name = self.input
                content = ['Login', self.input]
                self.game.networkManager.sendPacket(content)
                self.state = "Draft" # Switch to draft state after
                print()
                print("Switched to Draft")
                self.input = ''
            else:
                if len(self.input) < 10:
                    self.input += self.letters[self.index]
        elif self.game.eventManager.cancel:
            if len(self.input) > 0:
                self.input = self.input[:-1]

        self.blinkCursor.update()
        self.letterSelector.update()

    def draw(self):
        self.game.screen.blit(self.choose, (400 - self.choose.get_rect().width/2, 32))

        name = self.game.font32.render(self.input, 0, (0,0,0))
        self.game.screen.blit(name, (400 - name.get_rect().width/2, 140))
        self.blinkCursor.pos[0] = 400 + name.get_rect().width/2

        for i in range(len(self.letters)):
            letter = self.game.font32.render(self.letters[i], 0, (0,0,0))
            row = int(i / 6)
            col = int(i % 6)
            self.game.screen.blit(letter, (16 + (col * 128) + 64 - letter.get_rect().width/2, 280 + (row * 64) + 32 - letter.get_rect().height/2))

        self.blinkCursor.draw()
        self.letterSelector.draw()

    def reset(self):
        self.input = ""
        self.index = 0
