from TextInput import *
import pygame

class LetterSelector:
    def __init__(self, textInput):
        self.textInput = textInput
        self.pos = [69666, -69666]
        
    def update(self):
        row = int(self.textInput.index / 6)
        col = int(self.textInput.index % 6)
        self.pos[0] = 16 + col * 128 - 2
        self.pos[1] = 280 + 8 + row * 64

    def draw(self):
        rect = pygame.Rect(self.pos, (128, 48))
        pygame.draw.rect(self.textInput.game.screen, (0, 0, 0), rect, 5)
