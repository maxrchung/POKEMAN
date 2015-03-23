from TextInput import *
import pygame

class BlinkCursor:
    def __init__(self, textInput):
        self.textInput = textInput
        self.pos = [-66669, 142]
        
    def update(self):
        pass

    def draw(self):
        if self.textInput.display == 1:
            if not len(self.textInput.input) == 10 and not len(self.textInput.input) == 0:
                surface = pygame.Surface((30, 32))
                self.textInput.game.screen.blit(surface, self.pos)
