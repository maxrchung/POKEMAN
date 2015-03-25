import pygame
from TextScroll import *

pygame.init()
pygame.font.init()

font25 = pygame.font.Font("PKMN RBYGSC.ttf", 25)

pygame.display.set_caption("TEST")
screen = pygame.display.set_mode((800, 600))

overlay = pygame.image.load("Main_Overlay.png")

textScroll = TextScroll(screen=screen)
s = "HELP I'M BEING REPRESSED BY THE EVIL KAPPA EMPEROR. I AM IN DANGER AND I AM GOING TO DIE OF BEING TOO COOL. OH MY GOD I AM GONNA REALLY TRY AND FINISH THIS TEXT INPUT"
s2 = "1234567890123456789012345678901234567890"
s3 = "nigger faggot[] is my maxawetgiwejiweji wax chug da gwad epeen"

text1 = font25.render(s3, 0, (0,0,0))
offset = 10
midHeight = text1.get_rect().height/2

textScroll.load(s3)

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass

    screen.blit(overlay, (0, 0))
    '''
    screen.blit(text1, (18+offset, 483-midHeight))
    screen.blit(text1, (18+offset, 522-midHeight))
    screen.blit(text1, (18+offset, 562-midHeight))
    '''

    render = font25.render(textScroll.text, 0, (0, 0, 0))
    screen.blit(render, (18+offset, 483-midHeight))

    textScroll.update()
    textScroll.draw()

    pygame.display.flip()
