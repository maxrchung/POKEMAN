from Basic_Buttons import *

class Battle_Buttons:

    #Buttons for Battle 
    def __init__(self):
        self.menuButtons = {"Fight" : Basic_Buttons(ID = 'Fight'), "Switch": Basic_Buttons(ID = 'Switch'), "Forfeit" : Basic_Buttons(ID = 'forfeit'))
        

    
    def eventHandler(self):
        self._clock = pygame.time.Clock()
        
        self.number_count = 0

        for event in pygame.event.get():
            if(self.number_count > 4000):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.keys[0] = True
                    elif event.key == pygame.K_DOWN:
                        self.keys[1] = True
                    elif event.key == pygame.K_LEFT:  
                        self.keys[2] = True
                    elif event.key == pygame.K_RIGHT:
                        self.keys[3] = True
                    elif event.key == pygame.K_g:
                        self.keys[4] = True
                    elif event.key == pygame.K_h:
                        self.keys[5] = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.keys[0] = False
                    elif event.key == pygame.K_DOWN:
                        self.keys[1] = False
                    elif event.key == pygame.K_LEFT:
                        self.keys[2] = False
                    elif event.key == pygame.K_RIGHT:
                        self.keys[3] = False
                    elif event.key == pygame.K_g:
                        self.keys[4] = False
                    elif event.key == pygame.K_h:
                        self.keys[5] = False


            if self.keys[0]:

            elif self.keys[1]:

            elif self.keys[2]:

            elif self.keys[3]:

            elif self.keys[4]:

            elif self.keys[5]:

                    
        self.number_count += self._clock.tick()
    


    def move_cursor(self, direction):
        #
