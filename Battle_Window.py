import pygame, sys
    
from pygame.locals import *
pygame.init()


GREEN = ( 0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)



myfont = pygame.font.Font("PKMN RBYGSC.ttf", 25)
overlay = pygame.image.load("Main_Overlay.png")
overlayRect = overlay.get_rect()


padx = 20
pady = 20
screenwidth = 800
screenheight = 600

currentHealth = 100
totalHealth = 100
        
display = pygame.display.set_mode((screenwidth, screenheight), 0, 32)
display.fill(WHITE)

display.blit(overlay, overlayRect)
poke1 = myfont.render("BULBASAUR", 1, BLACK)
display.blit(poke1, (530, 260))
pygame.draw.rect(display, GREEN, (111, 60, 239, 8))
poke2 = myfont.render("CHARMANDER", 1, BLACK)
display.blit(poke2, (padx + 80, pady))
pygame.draw.rect(display, GREEN, (531, 297, 239, 8))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
