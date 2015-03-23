from Basic_Buttons import *

class Battle_Buttons:

    #Buttons for Battle 
    def __init__(self):
        self.menuButtons = [Basic_Buttons(rect = (515, 482, 122, 43), ID = 'Fight'), Basic_Buttons(rect = (667, 482, 122, 43), ID = 'Switch'), Basic_Buttons(rect = (595, 542, 122, 43), ID = 'forfeit')]
        self.pokeButtons = [Basic_Buttons(ID = 'Poke 1'), Basic_Buttons(ID = 'Poke 2'), Basic_Buttons(ID = 'Poke 3')]
        self.moveButtons = [Basic_Buttons(ID = 'Move 1'), Basic_Buttons(ID = 'Move 2'), Basic_Buttons(ID = 'Move 3'), Basic_Buttons(ID = 'Move 4')]
        self.forfeitButtons = [Basic_Buttons(ID = 'Yes'), Basic_Buttons(ID = 'No')]
        self.currentButton = 0 #used to determine what button you are on
        self.menustate = 0 #0: menu, 1: attack, 2: switch, 3: forfeit
        
    
    def eventHandler(self):

        for event in pygame.event.get():
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


        if self.menustate == 0 and self.currentButton == 0:
            # hovering moves

            if self.keys[1]: #down button
                self.currentButton = 2
            elif self.keys[3]: #right button
                self.currentButton = 1
            elif self.keys[4]: #enter button
                self.menustate = 1
                self.currentState = 0 
            

        elif self.menustate == 0 and self.currentButton == 1:
            # hovering switch
            if self.keys[1]: #down button
                self.currentButton = 2
            elif self.keys[2]: #left button
                self.currentButton = 0
            elif self.keys[4]: #enter button
                self.menustate = 2
                self.currentButton = 0
            
        elif self.menustate == 0 and self.currentButton == 2:
            # hovering forfeit
            if self.keys[0]: #up button
                self.currentButton = 0
            elif self.keys[2]: #left button
                self.currentButton = 1
            elif self.keys[3]: #right button
                self.currentButton = 0
            elif self.keys[4]: #enter button
                self.menustate = 2
                self.currentButton = 0

        elif self.menustate == 1 and self.currentButton == 0:
            # hovering move 1
            if self.keys[1]: #down button
                self.currentButton = 2
            elif self.keys[3]: #right button
                self.currentButton = 1

        elif self.menustate == 1 and self.currentButton == 1:
            # hovering move 2
            if self.keys[1]: #down button
                self.currentButton = 2
            elif self.keys[2]: #left button
                self.currentButton = 0
            
        elif self.menustate == 1 and self.currentButton == 2:
            #hovering move 3
            if self.keys[0]: #up button
                self.currentButton = 0
            elif self.keys[2]: #left button
                self.currentButton = 1
            elif self.keys[3]: #right button
                self.currentButton = 3

        elif self.menustate == 1 and self.currentButton == 3:
            #hovering move 4
            if self.keys[0]: #up button
                self.currentButton = 1
            elif self.keys[2]: #left button
                self.currentButton = 2

        elif self.menustate == 2 and self.currentButton == 0:
            #hovering poke 1
            if self.keys[3]: #right button
                self.currentButton = 1

        elif self.menustate == 2 and self.currentButton == 1:
            #hovering poke 2
            if self.keys[2]: #left button
                self.currentButton = 0
            elif self.keys[3]: #right button
                self.currentButton = 2

        elif self.menustate == 2 and self.currentButton == 2:
            #hovering poke 3
            if self.keys[2]: #left button
                self.currentButton = 1
                
        elif self.menustate == 3 and self.currentButton == 0:
            #hovering yes
            if self.keys[3]: #right button
                self.currentButton = 1

        elif self.menustate == 3 and self.currentButton == 1:
            #hovering no
            if self.keys[2]: #left button
                self.currentButton = 0


        if self.menustate == 1 or self.menustate == 2 or self.menustate == 3:
            if self.keys[5]: #escape button
                self.menustate = 0
                self.currentButton = 0
               
                    
    
        
        
