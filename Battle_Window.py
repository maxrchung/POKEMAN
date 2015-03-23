import pygame, sys
import Battle_Buttons
from pygame.locals import *
pygame.init()

GREEN = ( 0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
padx = 20
pady = 20

class Battle_Window:
    #Window that draws the battle as it takes place

    def __init__(self):

        self.myfont = pygame.font.Font("PKMN RBYGSC.ttf", 25) #creates a font from the pokemon ttf file
        self.overlay = pygame.image.load("Main_Overlay.png") # loads the overlay with the health bars, and menu UI
        self.overlayRect = self.overlay.get_rect() #gets the dimensions 800x600 in a tuple(int,int)

        #window dimensions
        self.screenwidth = 800
        self.screenheight = 600

        #variables for the player's health bar
        self.p1currentHealth = 100
        self.p1totalHealth = 100

        #variables for the enemy's health bar
        self.p2currentHealth = 100
        self.p2totalHealth = 100

        #creates the pygame window
        self.display = pygame.display.set_mode((self.screenwidth, self.screenheight), 0, 32)
        self.display.fill(WHITE)


        #draws the initial window
        self.draw()


    def draw(self):
        self.display.blit(self.overlay, self.overlayRect)
        self.poke1 = self.myfont.render("BULBASAUR", 1, BLACK)
        self.display.blit(self.poke1, (530, 260))
        pygame.draw.rect(self.display, GREEN, (111, 60, 239, 8))
        self.poke2 = self.myfont.render("CHARMANDER", 1, BLACK)
        self.display.blit(self.poke2, (padx + 80, pady))
        pygame.draw.rect(self.display, GREEN, (531, 297, 239, 8))



    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()


