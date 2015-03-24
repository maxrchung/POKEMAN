import pygame, sys



from Battle_Buttons import *
from pygame.locals import *
from Color_Globals import *
sys.path.insert(0, 'C:\\Users\\Victor\\Desktop\\Game Jam Spring 2015\\POKEMAN\\Networking\\Client')
from Game import *
pygame.init()


padx = 20
pady = 20

class Battle_Window:
                #Window that draws the battle as it takes place

    def __init__(self, game):
        #initializes the game to Battle_Window
        self.game = game

        #pokemon received from the server
        self.receivedPokeList = game.pokemans#(40, 225)
        self.receivedPokeIndex = game.activePoke
        self.receivedEnemyPoke = game.oppPoke #(535, 65)
        
        #pokemon images

        #player 1
        self.p1coord       = (40, 225)
        self.p1rapperimg   = pygame.image.load("nerd.png")
        self.p1delinqimg   = pygame.image.load("delinqB.png")
        self.p1nerdimg     = pygame.image.load("nerd.png")
        self.p1criminalimg = pygame.image.load("criminal.png")
        self.p1homelessimg = pygame.image.load("hobo.png")
    
        #player 2
        self.p2coord       = (535, 60)
        self.p2rapperimg   = pygame.image.load("nerd.png")
        self.p2delinqimg   = pygame.image.load("delinq.png")
        self.p2nerdimg     = pygame.image.load("nerd.png")
        self.p2criminalimg = pygame.image.load("criminal.png")
        self.p2homelessimg = pygame.image.load("hobo.png")
        
    
        self.myfont = pygame.font.Font("PKMN RBYGSC.ttf", 25) #creates a font from the pokemon ttf file
        self.smallfont = pygame.font.Font("PKMN RBYGSC.ttf", 12)
        self.overlay = pygame.image.load("Main_Overlay.png") # loads the overlay with the health bars, and menu UI
        self.overlayRect = self.overlay.get_rect() #gets the dimensions 800x600 in a tuple(int,int)

        #window dimensions
        self.screenwidth = 800
        self.screenheight = 600

        #variables for the player's health bar
        self.p1healthPercentage = 100
        self.p1totalHealth = 100
        self.p1currentHealth = 325
        self.p1healthMax = 325

        #variables for the enemy's health bar
        self.p2healthPercentage = 100
        self.p2totalHealth = 100
        self.p2currentHealth = 325
        self.p2healthMax = 325


        #creates the pygame window
        self.display = pygame.display.set_mode((self.screenwidth, self.screenheight), 0, 32)
        self.display.fill(WHITE)

        #pokemon names
        self.poke1Name = self.receivedPokeList[self.receivedPokeIndex].name.upper()
        self.poke2Name = self.receivedPokeList[self.receivedPokeIndex].name.upper()

        #initialize the Battle Buttons
        self.theButtons = Battle_Buttons()
        self.fightButton = self.myfont.render(self.theButtons.getMenu(0).upper(), 1, BLACK)
        self.switchButton = self.myfont.render(self.theButtons.getMenu(1).upper(), 1, BLACK)
        self.forfeitButton = self.myfont.render(self.theButtons.getMenu(2).upper(), 1, BLACK)
        #"Fight" Button:          (515, 482, 122, 43)
        #"Switch" Button:         (667, 482, 122, 43)
        #"Forfeit" Button:        (595, 542, 122, 43)


        #initialize the Move Buttons
        self.move1 = self.smallfont.render(self.receivedPokeList[self.receivedPokeIndex].moveset[0].name, 1, BLACK)
        self.move2 = self.smallfont.render(self.receivedPokeList[self.receivedPokeIndex].moveset[1].name, 1, BLACK)
        self.move3 = self.smallfont.render(self.receivedPokeList[self.receivedPokeIndex].moveset[2].name, 1, BLACK)
        self.move4 = self.smallfont.render(self.receivedPokeList[self.receivedPokeIndex].moveset[3].name, 1, BLACK)

        #initialize the Switch Buttons
        self.switch1 = self.myfont.render(self.receivedPokeList[0].name.upper(), 1, BLACK)
        self.switch2 = self.myfont.render(self.receivedPokeList[1].name.upper(), 1, BLACK)
        self.switch3 = self.myfont.render(self.receivedPokeList[2].name.upper(), 1, BLACK)

        #initialize the forfeit Buttons
        self.forfeit1 = self.myfont.render("YES", 1, BLACK)
        self.forfeit2 = self.myfont.render("NO", 1, BLACK)


        #visible bools for inner windows
        self.moveVisible = False
        self.pokeVisible = False
        self.switchVisible = False
        self.forfeitVisible = False




        #draws the initial window
        self.draw()




    def draw(self):
        self.display.fill(WHITE)
        #creates the health text
        self.p1healthtext = "%d / %d" % (self.p1currentHealth, self.p1healthMax)

        
        #draws the elements onto the screen
        self.display.blit(self.overlay, self.overlayRect)
        self.poke1 = self.myfont.render(self.poke1Name, 1, BLACK)
        self.display.blit(self.poke1, (530, 260))                         
        self.poke2 = self.myfont.render(self.poke2Name, 1, BLACK)
        self.display.blit(self.poke2, (padx + 80, pady))

        #conditionals to check the color of the hp bars

        assert 0 <= self.p1healthPercentage <= 100, "Player 1 health is not in correct bounds: %r" % self.p1healthPercentage
        assert 0 <= self.p2healthPercentage <= 100, "Player 2 Health is not in Correct Bounds: %r" % self.p2healthPercentage

        #filling in the health bars        
        if (self.p1healthPercentage <= 15):          #<----Health is below 15%
            pygame.draw.rect(self.display, RED, (531, 297, 239*(self.p1healthPercentage / 100), 8)) #player 1 Health Bar
        elif(self.p1healthPercentage <= 50):         #<----Health is below 50%
            pygame.draw.rect(self.display, YELLOW, (531, 297, 239*(self.p1healthPercentage / 100), 8))
        else:                                        #<----Health is above 50%
            pygame.draw.rect(self.display, GREEN, (531, 297, 239*(self.p1healthPercentage / 100), 8))
        if (self.p2healthPercentage <= 15):
            pygame.draw.rect(self.display, RED, (111, 60, 239*(self.p2healthPercentage / 100), 8)) #player 2 Health Bar
        elif (self.p2healthPercentage <= 50):
            pygame.draw.rect(self.display, YELLOW, (111, 60, 239*(self.p2healthPercentage / 100), 8))
        else:
            pygame.draw.rect(self.display, GREEN, (111, 60, 239*(self.p2healthPercentage / 100), 8))

        #draws the health number below the health bar
        self.healthtextRender = self.myfont.render(self.p1healthtext, 1, BLACK)
        self.display.blit(self.healthtextRender, (550, 320))


        #draws the menu buttons
        self.display.blit(self.fightButton, (520, 502))
        self.display.blit(self.switchButton, (657, 502))
        self.display.blit(self.forfeitButton, (565, 562))

        #load in the cursor
        self.cursorimg = pygame.image.load("Menu_Cursor.png")
        self.cursorimgrect = self.cursorimg.get_rect()

        #if the gamestate is in menu
        if self.theButtons.getMenustate() == 0:
        #then match the blit to the current button
            #button on FIGHT
            if self.theButtons.getCurrentbutton() == 0:
                self.display.blit(self.cursorimg, (500, 502))
            #button on SWITCH
            elif self.theButtons.getCurrentbutton() == 1:
                self.display.blit(self.cursorimg, (637, 502))
            #button on FORFEIT
            elif self.theButtons.getCurrentbutton() == 2:
                self.display.blit(self.cursorimg, (545, 562))


        #if the menustate is on moves
        if self.theButtons.getMenustate() == 1:
            #button on move 1
            if self.theButtons.getCurrentbutton() == 0:
                self.display.blit (self.cursorimg, (103, 504))
            #button on move 2
            elif self.theButtons.getCurrentbutton() == 1:
                self.display.blit (self.cursorimg, (226, 504))
            #button on move 3
            elif self.theButtons.getCurrentbutton() == 2:
                self.display.blit (self.cursorimg, (103, 536))
            #button on move 4
            elif self.theButtons.getCurrentbutton() == 3:
                self.display.blit (self.cursorimg, (226, 536))


        #if the menustate is on switch
        if self.theButtons.getMenustate() ==2:
            #button on pokemon 1
            if self.theButtons.getCurrentbutton() == 0:
                self.display.blit (self.cursorimg, (79, 516))
            #button on pokemon 2
            elif self.theButtons.getCurrentbutton() == 1:
                self.display.blit (self.cursorimg, (178, 516))
            #button on pokemon 3
            elif self.theButtons.getCurrentbutton() == 2:
                self.display.blit (self.cursorimg, (267, 516))

        #if the menustate is on forfeit
        if self.theButtons.getMenustate() == 3:
            #button on yes
            if self.theButtons.getCurrentbutton() == 0:
                self.display.blit (self.cursorimg, (145, 516))
            #button on no
            elif self.theButtons.getCurrentbutton() == 1:
                self.display.blit (self.cursorimg, (310, 516))



        #if the gamestate is in the moves
        if self.moveVisible == True:
            self.display.blit(self.move1, (123, 504))
            self.display.blit(self.move2, (246, 504))
            self.display.blit(self.move3, (123, 536))
            self.display.blit(self.move4, (246, 536))
        #if the gamestate is in switch
        elif self.pokeVisible == True:
            self.display.blit(self.poke1, (99, 516))
            self.display.blit(self.poke2, (198, 516))
            self.display.blit(self.poke3, (287, 516))
        #if the gamestate is in quit
        elif self.forfeitVisible == True:
            self.display.blit(self.forfeit1, (165, 516))
            self.display.blit(self.forfeit2, (330, 516))

        #draw the pokemon for the player
        if self.receivedPokeList[self.receivedPokeIndex].type == 0:  #rapper
            self.display.blit(self.p1rapperimg, self.p1coord)
        elif self.receivedPokeList[self.receivedPokeIndex].type == 1: #delinquent child
            self.display.blit(self.p1delinqimg, self.p1coord)
        elif self.receivedPokeList[self.receivedPokeIndex].type == 2: #Nerds
            self.display.blit(self.p1nerdimg, self.p1coord)
        elif self.receivedPokeList[self.receivedPokeIndex].type == 3: #Criminals
            self.display.blit(self.p1criminalimg, self.p1coord)
        elif self.receivedPokeList[self.receivedPokeIndex].type == 4: #Homeless
            self.display.blit(self.p1homelessimg, self.p1coord)
        #draw the pokemon for the enemy
        if self.receivedEnemyPoke.type == 0: #rapper
            self.display.blit(self.p2rapperimg, self.p2coord)
        elif self.receivedEnemyPoke.type == 1: #delinquent child
            self.display.blit(self.p2delinqimg, self.p2coord)
        elif self.receivedEnemyPoke.type == 2: #nerd
            self.display.blit(self.p2nerdimg, self.p2coord)
        elif self.receivedEnemyPoke.type == 3: #criminal
            self.display.blit(self.p2criminalimg, self.p2coord)
        elif self.receivedEnemyPoke.type == 4: #homeless
            self.display.blit(self.p2homelessimg, self.p2coord)
    def update(self):
        content = ["Battle"]
                        #state changes
        if self.theButtons.getMenustate() == 0 and self.theButtons.getCurrentbutton() == 0:
                        # hovering moves

            if self.game.eventManager.down: #down button
                self.theButtons.setCurrentbutton(2)
            elif self.game.eventManager.right: #right button
                self.theButtons.setCurrentbutton(1)
            elif self.game.eventManager.enter: #enter button
                self.theButtons.setMenustate(1)
                self.theButtons.setCurrentbutton(0)
                        

        elif self.theButtons.getMenustate() == 0 and self.theButtons.getCurrentbutton() == 1:
                        # hovering switch
            if self.game.eventManager.down: #down button
                self.theButtons.setCurrentbutton(2)
            elif self.game.eventManager.left: #left button
                self.theButtons.setCurrentbutton(0)
            elif self.game.eventManager.enter: #enter button
                self.theButtons.setMenustate(2)
                self.theButtons.setCurrentbutton(0)
                        
        elif self.theButtons.getMenustate() == 0 and self.theButtons.getCurrentbutton() == 2:
                        # hovering forfeit
            if self.game.eventManager.up: #up button
                self.theButtons.setCurrentbutton(0)
            elif self.game.eventManager.left: #left button
                self.theButtons.setCurrentbutton(1)
            elif self.game.eventManager.right: #right button
                self.theButtons.setCurrentbutton(0)
            elif self.game.eventManager.enter: #enter button
                self.theButtons.setMenustate(2)
                self.theButtons.setCurrentbutton(0)

        elif self.theButtons.getMenustate() == 1 and self.theButtons.getCurrentbutton() == 0:
                        # hovering move 1
            if self.game.eventManager.down: #down button
                self.theButtons.setCurrentbutton(2)
            elif self.game.eventManager.right: #right button
                self.theButtons.setCurrentbutton(1)
            elif self.game.eventManager.enter:#sends moves[0]
                content.append(0)
                content.append(0)
                self.game.networkManager.sendPacket(content)

        elif self.theButtons.getMenustate() == 1 and self.theButtons.getCurrentbutton() == 1:
                        # hovering move 2
            if self.game.eventManager.down: #down button
                self.theButtons.setCurrentbutton(2)
            elif self.game.eventManager.left: #left button
                self.theButtons.setCurrentbutton(0)
            elif self.game.eventManager.enter:#sends moves[1]
                content.append(0)
                content.append(1)
                self.game.networkManager.sendPacket(content)
                        
        elif self.theButtons.getMenustate() == 1 and self.theButtons.getCurrentbutton() == 2:
                        #hovering move 3
            if self.game.eventManager.up: #up button
                self.theButtons.setCurrentbutton(0)
            elif self.game.eventManager.left: #left button
                self.theButtons.setCurrentbutton(1)
            elif self.game.eventManager.right: #right button
                self.theButtons.setCurrentbutton(3)
            elif self.game.eventManager.enter:#sends moves[2]
                content.append(0)
                content.append(2)
                self.game.networkManager.sendPacket(content)

        elif self.theButtons.getMenustate() == 1 and self.theButtons.getCurrentbutton() == 3:
                        #hovering move 4
            if self.game.eventManager.up: #up button
                self.theButtons.setCurrentbutton(1)
            elif self.game.eventManager.left: #left button
                self.theButtons.setCurrentbutton(2)
            elif self.game.eventManager.enter:#sends moves[3]
                content.append(0)
                content.append(3)
                self.game.networkManager.sendPacket(content)

        elif self.theButtons.getMenustate() == 2 and self.theButtons.getCurrentbutton() == 0:
                        #hovering poke 1
            if self.game.eventManager.right: #right button
                self.theButtons.setCurrentbutton(1)
            elif self.game.eventManager.enter:#sends swap[0]
                content.append(1)
                content.append(0)
                if(self.receivedPokeIndex!=0):#checking to see if it's current pokemon
                    self.game.networkManager.sendPacket(content)

        elif self.theButtons.getMenustate() == 2 and self.theButtons.getCurrentbutton() == 1:
                        #hovering poke 2
            if self.game.eventManager.left: #left button
                self.theButtons.setCurrentbutton(0)
            elif self.game.eventManager.right: #right button
                self.theButtons.setCurrentbutton(2)
            elif self.game.eventManager.enter:#sends swap[1]
                content.append(1)
                content.append(1)
                if(self.receivedPokeIndex!=1):#checking to see if it's current pokemon
                    self.game.networkManager.sendPacket(content)

        elif self.theButtons.getMenustate() == 2 and self.theButtons.getCurrentbutton() == 2:
                        #hovering poke 3
            if self.game.eventManager.left: #left button
                self.theButtons.setCurrentbutton(1)
            elif self.game.eventManager.enter:#sends swap[2]
                content.append(1)
                content.append(2)
                if(self.receivedPokeIndex!=2):#checking to see if it's current pokemon
                    self.game.networkManager.sendPacket(content)
                
        elif self.theButtons.getMenustate() == 3 and self.theButtons.getCurrentbutton() == 0:
                        #hovering yes
            if self.game.eventManager.right: #right button
                self.theButtons.setCurrentbutton(1)
            elif self.game.eventManager.enter:#sends ff
                content.append(2)
                content.append(0)
                self.game.networkManager.sendPacket(content)

        elif self.theButtons.getMenustate() == 3 and self.theButtons.getCurrentbutton() == 1:
                        #hovering no
            if self.game.eventManager.left: #left button
                self.theButtons.setCurrentbutton(0)
            elif self.game.eventManager.enter:
                self.theButtons.setMenustate(0)
                self.theButtons.setCurrentbutton(0)


        if self.theButtons.getMenustate() == 1 or self.theButtons.getMenustate() == 2 or self.theButtons.getMenustate() == 3:
            if self.game.eventManager.cancel: #escape button
                self.theButtons.setMenustate(0)
                self.theButtons.setCurrentbutton(0)
                self.moveVisible =False
                self.pokeVisible = False
                self.forfeitVisible = False


        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                pygame.display.update()




                
