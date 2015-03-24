from Game import *

class EventManager:
    def __init__(self, game):
        self.game = game

        #Sets variables for keys
        self.left = False
        self.up = False
        self.right = False
        self.down = False
        self.cancel = False # Basically the B button
        self.enter = False # Basically the A button

    def run(self):
        self.update()

    def update(self):
        # Reset input every loop
        self.left = False
        self.up = False
        self.right = False
        self.down = False
        self.cancel = False
        self.enter = False
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    self.left = True
                elif event.key==pygame.K_UP:
                    self.up = True
                elif event.key==pygame.K_RIGHT:
                    self.right = True
                elif event.key==pygame.K_DOWN:
                    self.down = True
                elif event.key==pygame.K_ESCAPE:
                    self.cancel = True
                elif event.key==pygame.K_RETURN:
                    self.enter = True
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                self.game.disconnect()
