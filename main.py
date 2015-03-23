'''
Created on Mar 23, 2015

@author: Carl W Glahn
'''
import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Pokedeath Test")
    screen = pygame.display.set_mode((1024,612))
    running = True
    image1 = pygame.image.load("hobo.png")
    image2 = pygame.image.load("criminal.png")
    time= 0
    def draw(yourplayer, hisplayer, time):
        screen.fill((55,55,55))
        if time%10000000 == 0:
            yourplayer=death1(yourplayer)
            hisplayer=death2(hisplayer)
            screen.blit(image1,(yourplayer[0],yourplayer[1]))
            screen.blit(image2,(hisplayer[0],hisplayer[1]))
        else:
            screen.blit(image1,(yourplayer[0],yourplayer[1]))
            screen.blit(image2,(hisplayer[0],hisplayer[1]))
        time+=1
        pygame.display.flip()
    def death1(xy):
        if(xy[1]>=700):
            return xy
        xy[1]+= .8
        #print (xy)
        return xy
    def death2(xy):
        if(xy[1]<=-200):
            return xy
        xy[1]-= .8

        return xy
    def switch1(xy):
        #print(imagex)
        #print(imagey)
        if(xy[0]<=-150 or xy[1]>=700):
            return xy
        xy[0]-= 1
        xy[1]+= 1
        #print (xy)
        return xy
    def switch2(xy):
        #print(imagex)
        #print(imagey)
        if(xy[0]>=1150 or xy[1]<=-200):
            return xy
        xy[0]+= 1
        xy[1]-= 1
        #print (xy)
        return xy
    
    yourplayer=[200,300]
    hisplayer= [750, 100]
    while running:
        draw(yourplayer, hisplayer, time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
if __name__=="__main__":
    # call the main function
    main()