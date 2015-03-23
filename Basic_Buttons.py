import pygame
from pygame.locals import *

pygame.font.init()
BLACK     = (  0,   0,   0)
WHITE     = (255, 255, 255)
DARKGRAY  = ( 64,  64,  64)
GRAY      = (128, 128, 128)
LIGHTGRAY = (212, 208, 200)


class Basic_Buttons:

    def __init__(self, rect = None, bgcolor = LIGHTGRAY, fgcolor = BLACK, normal = None, ID = ''):

        #List of Keys
        self.keys = [False, False, False, False, False, False] #key[0] = UP, key[1] = DOWN, key[2] = LEFT, key[3] = RIGHT, key[4] = g, key[5] = h
        
        #Button's ID (I.E 'Attack', 'Switch', 'Forfeit')
        self.ID = ID

        #Button Rectangle
        if rect is None:
            self.rect = pygame.Rect(0,0,30,60)
        else:
            self.rect = pygame.Rect(rect)

        #Button text/font
        self.caption = ID
        self.font = pygame.font.Font('PKMN RBYGSC.tff', 14)
        
        #Button foreground/background color
        self.bgcolor = bgcolor
        self.fgcolor = fgcolor

        #is the button visible/is the button an image
        self.visible = True
        self.customSurfaces = False

        if normal is None:
            #creates the surface with text
            self.surfaceNormal = pygame.Surface(self.rect.size)
            self._update()
        else:
            #create the surfaces for a custom image button
            self.setSurfaces(normal)


    def draw(self, surfaceObj):
        #Blit the current button's appearance to the surface object
        if self.visible:
            surfaceObj.blit(self.surfaceNormal, self.rect)

    def setSurfaces(self, normalSurface):
        # Drawing the button image...

        #checks to see if the surface is a string filepath
        if type(normalSurface) == str: self.origSurfaceNormal = pygame.image.load(normalSurface)
        
        #set the surface images
        self.surfaceNormal = self.origSurfaceNormal
        self.customSurfaces = True
        self.rect = pygame.rect((self.rect.left, self.rect.top, self.surfaceNormal.get_width(), self.surfaceNormal.get_height()))

    def _update(self):
        
        #Redraw the button's Surface object. Call when the button is changed
        _w = self.rect.width
        _h = self.rect.height


        #if the button is an image, smoothscale transform the button
        if self.customSurfaces:
            self.surfaceNormal = pygame.transform.smoothscale(self.origSurfaceNormal, self.rect.size)
            return
        
        #fill background color for button
        self.surfaceNormal.fill(self.bgcolor)
                             
        #draw caption text for all buttons
        captionSurf = self.font.render(self.caption, True, self.fgcolor, self.bgcolor)
        captionRect = captionSurf.get_rect()
        captionRect.center = int(w/2), int(h/2)
        self.surfaceNormal.blit(captionSurf, captionRect)

        #draw border for button
        pygame.draw.rect(self.surfaceNormal, BLACK, pygame.Rect((0, 0, w, h)), 1) # Black border around everything
        pygame.draw.line(self.surfaceNormal, WHITE, (1, 1), (w-2, 1))
        pygame.draw.line(self.surfaceNormal, WHITE, (1, 1), (1, h-2))
        pygame.draw.line(self.surfaceNormal, DARKGRAY, (1, h-1), (w-1, h-1))
        pygame.draw.line(self.surfaceNormal, DARKGRAY, (w-1, 1), (w-1, h-1))
        pygame.draw.line(self.surfaceNormal, GRAY, (2, h-2), (w-2, h-2))
        pygame.draw.line(self.surfaceNormal, GRAY, (w-2, 2), (w-2, h-2))

                             
    def getCaption(self): return caption
    def getRect(self): return rect
    def getVisible(self): return visible
    def getFgcolor(self): return fgcolor
    def getBgcolor(self): return bgcolor

    def setCaption(self, i): caption = i
    def setRect(self, i): rect = i
    def setVisible(self, i): visible = i
    def setFgcolor(self): fgcolor = i
    def setBgcolor(self): bgcolor = i

    
