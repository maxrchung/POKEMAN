import pygame
from pygame.locals import *

pygame.font.init()
BLACK     = (  0,   0,   0)
WHITE     = (255, 255, 255)
DARKGRAY  = ( 64,  64,  64)
GRAY      = (128, 128, 128)
LIGHTGRAY = (212, 208, 200)


class Basic_Buttons:

    def __init__(self, rect = None, caption = '', bgcolor = LIGHTGRAY, fgcolor = BLACK, normal = None, down= None, highlight = None):
        if rect is None:
            self.rect = pygame.Rect(0,0,30,60)
        else:
            self.rect = pygame.Rect(rect)

        self.caption = caption
        self.bgcolor = bgcolor
        self.fgcolor = fgcolor
        self.font = pygame.font.Font('PKMN RBYGSC.tff', 14)

        #tracking the state of the button
        self.buttonDown = False #is the key down
        self.keyOnButton = False # is the key currently on the button
        self.lastKeyOnButton = False # was the last keyPressed on the button

        self.visible = True
        self.customSurfaces = False

        if normal is None:
            #creates the surface with text
            self.surfaceNormal = pygame.Surface(self.rect.size)
            self.surfaceDown = pygame.Surface(self.rect.size)
            self.surfaceHighlight = pygame.Surface(self.rect.size)
            self.update()
        else:
            #create the surfaces for a custom image button
            self.setSurfaces(normal, down, highlight)


    def draw(self, surfaceObj):
        #Blit the current button's appearance to the surface object
        if self.visible:
            if self.buttonDown:
                surfaceObj.blit(self.surfaceDown, self.rect)
            elif self.keyOnButton:
                surfaceObj.blit(self.Highlight, self.rect)
            else:
                surfaceObj.blit(self.surfaceNormal, self.rect)

    def setSurfaces(self, normalSurface, downSurface=None, highlightSurface=None):
        # Drawing the button image...
        

        # Checks to see if button has downclick image and highlight image
        if downSurface is None: downSurface = normalSurface
        if highlightSurface is None: highlightSurface = normalSurface

        #checks to see if the surface is a string filepath
        if type(normalSurface) == str: self.origSurfaceNormal = pygame.image.load(normalSurface)
        if type(downSurface) == str: self.origSurfaceDown = pygame.image.load(downSurface)
        if type(highlightSurface) == str: self.origSurfaceHighlight = pygame.image.load(highlightSurface)

        #check the image sizes
        if self.origSurfaceNormal.get_size() != self.origSurfaceDown.get_size() != self.origSurfaceHighlight.get_size(): raise Exception('Error: item sizes do not match.')
        
        #set the surface images
        self.surfaceNormal = self.origSurfaceNormal
        self.surfaceDown = self.origSurfaceDown
        self.surfaceHighlight = self.origSurfaceHighlight
        self.customSurfaces = True
        self.rect = pygame.rect((self.rect.left, self.rect.top, self.surfaceNormal.get_width(), self.surfaceNormal.get_height()))




    def _update(self):
        #Redraw the button's Surface object. Call when the button is changed
        _w = self.rect.width
        _h = self.rect.height


        #if the button is an image, smoothscale transform the button
        if self.customSurfaces:
            self.surfaceNormal = pygame.transform.smoothscale(self.origSurfaceNormal, self.rect.size)
            self.surfaceDown = pygame.transform.smoothscale(self.origSurfaceDown, self.rect.size)
            self.surfaceHighlight = pygame.transform.smoothscale(self.origSurfaceHighlight, self.rect.size)
            return
        
        #fill background color for all buttons
        self.surfaceNormal.fill(self.bgcolor)
        self.surfaceDown.fill(self.bgcolor)
        self.surfaceHighlight.fill(self.bgcolor)
                             
        #draw caption text for all buttons
        captionSurf = self.font.render(self.caption, True, self.fgcolor, self.bgcolor)
        captionRect = captionSurf.get_rect()
        captionRect.center = int(w/2), int(h/2)
        self.surfaceNormal.blit(captionSurf, captionRect)
        self.surfaceDown.blit(captionSurf, captionRect)

        #draw border for normal button
        pygame.draw.rect(self.surfaceNormal, BLACK, pygame.Rect((0, 0, w, h)), 1) # Black border around everything
        pygame.draw.line(self.surfaceNormal, WHITE, (1, 1), (w-2, 1))
        pygame.draw.line(self.surfaceNormal, WHITE, (1, 1), (1, h-2))
        pygame.draw.line(self.surfaceNormal, DARKGRAY, (1, h-1), (w-1, h-1))
        pygame.draw.line(self.surfaceNormal, DARKGRAY, (w-1, 1), (w-1, h-1))
        pygame.draw.line(self.surfaceNormal, GRAY, (2, h-2), (w-2, h-2))
        pygame.draw.line(self.surfaceNormal, GRAY, (w-2, 2), (w-2, h-2))

        #draw border for down button
        pygame.draw.rect(self.surfaceDown, BLACK, pygame.Rect((0, 0, w, h)), 1) # Black border around everything
        pygame.draw.line(self.surfaceDown, WHITE, (1, 1), (w-2, 1))
        pygame.draw.line(self.surfaceDown, WHITE, (1, 1), (1, h-2))
        pygame.draw.line(self.surfaceDown, DARKGRAY, (1, h-1), (w-1, h-1))
        pygame.draw.line(self.surfaceDown, DARKGRAY, (w-1, 1), (w-1, h-1))
        pygame.draw.line(self.surfaceDown, GRAY, (2, h-2), (w-2, h-2))
        pygame.draw.line(self.surfaceDown, GRAY, (w-2, 2), (w-2, h-2))

        #draw border for highlight button
        self.surfaceHighlight = self.surfaceNormal

                             
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

    
