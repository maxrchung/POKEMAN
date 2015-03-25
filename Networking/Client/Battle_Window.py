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
        self.p1coord       = (72, 189)
        self.p1rapperimg   = pygame.image.load("NAKEDMAN2BACK.png")
        self.p1delinqimg   = pygame.image.load("NAKEDMAN4BACK.png")
        self.p1nerdimg     = pygame.image.load("NAKEDMAN5BACK.png")
        self.p1criminalimg = pygame.image.load("NAKEDMAN3BACK.png")
        self.p1homelessimg = pygame.image.load("NAKEDMANBACK.png")
    
        #player 2
        self.p2coord       = (536, 86)
        self.p2rapperimg   = pygame.image.load("NAKEDMAN2.png")
        self.p2delinqimg   = pygame.image.load("NAKEDMAN4.png")
        self.p2nerdimg     = pygame.image.load("NAKEDMAN5.png")
        self.p2criminalimg = pygame.image.load("NAKEDMAN3.png")
        self.p2homelessimg = pygame.image.load("NAKEDMAN.png")
        
    
        self.myfont = pygame.font.Font("PKMN RBYGSC.ttf", 25) #creates a font from the pokemon ttf file
        self.smallfont = pygame.font.Font("PKMN RBYGSC.ttf", 16)
        self.overlay = pygame.image.load("Main_Overlay.png") # loads the overlay with the health bars, and menu UI
        self.overlayRect = self.overlay.get_rect() #gets the dimensions 800x600 in a tuple(int,int)

        #window dimensions
        self.screenwidth = 800
        self.screenheight = 600

        #variables for the player's health bar
        self.p1healthPercentage = 100
        self.p1healthMax = game.pokemans[game.activePoke].stats[5]
        self.p1currentHealth = game.pokemans[game.activePoke].current

        #variables for the enemy's health bar
        self.p2healthPercentage = 100
        self.p2healthMax = game.oppPoke.stats[5]
        self.p2currentHealth = game.oppPoke.current


        #creates the pygame window
        self.display = pygame.display.set_mode((self.screenwidth, self.screenheight), 0, 32)
        self.display.fill(WHITE)

        #pokemon names
        self.poke1Name = self.receivedPokeList[self.receivedPokeIndex].name.upper()
        self.poke2Name = self.receivedEnemyPoke.name.upper()

        #initialize the Battle Buttons
        self.theButtons = Battle_Buttons()
        self.fightButton = self.myfont.render(self.theButtons.getMenu(0).upper(), 0, BLACK)
        self.switchButton = self.myfont.render(self.theButtons.getMenu(1).upper(), 0, BLACK)
        self.forfeitButton = self.myfont.render(self.theButtons.getMenu(2).upper(), 0, BLACK)
        #"Fight" Button:          (515, 482, 122, 43)
        #"Switch" Button:         (667, 482, 122, 43)
        #"Forfeit" Button:        (595, 542, 122, 43)


        #initialize the Move Buttons
        self.move1 = self.myfont.render(self.receivedPokeList[self.receivedPokeIndex].moveset[0].moveName, 0, BLACK)
        self.move2 = self.myfont.render(self.receivedPokeList[self.receivedPokeIndex].moveset[1].moveName, 0, BLACK)
        self.move3 = self.myfont.render(self.receivedPokeList[self.receivedPokeIndex].moveset[2].moveName, 0, BLACK)
        self.move4 = self.myfont.render(self.receivedPokeList[self.receivedPokeIndex].moveset[3].moveName, 0, BLACK)

        #initialize the Switch Buttons
        self.switch1 = self.myfont.render(self.receivedPokeList[0].name.upper(), 0, BLACK)
        self.switch2 = self.myfont.render(self.receivedPokeList[1].name.upper(), 0, BLACK)
        self.switch3 = self.myfont.render(self.receivedPokeList[2].name.upper(), 0, BLACK)

        #initialize the forfeit Buttons
        self.forfeit1 = self.myfont.render("YES", 0, BLACK)
        self.forfeit2 = self.myfont.render("NO", 0, BLACK)


        #visible bools for inner windows
        self.moveVisible = False
        self.switchVisible = False
        self.forfeitVisible = False

        self.battling = False

        self.blinkClock = pygame.time.Clock()
        self.blinkTimer = 0
        self.blink = True

        #draws the initial window
        self.draw()




    def draw(self):
        self.display.fill(WHITE)
        #creates the health text
        self.p1healthtext = "%d / %d" % (self.p1currentHealth, self.p1healthMax)

        
        #draws the elements onto the screen
        self.display.blit(self.overlay, self.overlayRect)
        self.poke1 = self.myfont.render(self.poke1Name, 1, BLACK)
        self.display.blit(self.poke1, (511  , 259))                         
        self.poke2 = self.myfont.render(self.poke2Name, 1, BLACK)
        self.display.blit(self.poke2, (112, 20))
 
        #conditionals to check the color of the hp bars

        #filling in the health bars        
        if (self.p1healthPercentage <= 15):          #<----Health is below 15%
            pygame.draw.rect(self.display, RED, (515 + 240*((100 - self.p1healthPercentage) / 100), 298, 241*(self.p1healthPercentage / 100), 9)) #player 1 Health Bar
        elif(self.p1healthPercentage <= 50):         #<----Health is below 50%
            pygame.draw.rect(self.display, YELLOW, (515 + 240*((100 - self.p1healthPercentage) / 100), 298, 241*(self.p1healthPercentage / 100), 9))
        else:                                        #<----Health is above 50%
            pygame.draw.rect(self.display, GREEN, (515 + 240*((100 - self.p1healthPercentage) / 100), 298, 241*(self.p1healthPercentage / 100), 9))
        if (self.p2healthPercentage <= 15):
            pygame.draw.rect(self.display, RED, (116, 59, 240*(self.p2healthPercentage / 100), 9)) #player 2 Health Bar
        elif (self.p2healthPercentage <= 50):
            pygame.draw.rect(self.display, YELLOW, (116, 59, 240*(self.p2healthPercentage / 100), 9))
        else:
            pygame.draw.rect(self.display, GREEN, (116, 59, 240 *(self.p2healthPercentage / 100), 9))

        #draws the health number below the health bar
        self.healthtextRender = self.myfont.render(self.p1healthtext, 0, BLACK)
        self.display.blit(self.healthtextRender, (550, 317))
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
        if self.game.wait == True:
            text = self.myfont.render("Waiting for opponent",0,BLACK)
            self.display.blit(text,(100,600))
            return
        #draws the menu buttons
        self.display.blit(self.fightButton, (575+13-self.fightButton.get_rect().width/2, 483+13-self.fightButton.get_rect().height/2))
        self.display.blit(self.switchButton, (725-13-self.switchButton.get_rect().width/2, 483+13-self.switchButton.get_rect().height/2))
        self.display.blit(self.forfeitButton, (725-13-self .forfeitButton.get_rect().width/2, 565-13-self.forfeitButton.get_rect().height/2))

        self.blinkTimer += self.blinkClock.tick()
        if self.blinkTimer > 500:
            self.blinkTimer = 0
            if self.blink:
                self.blink = False
            else:
                self.blink = True

        if self.blink:
            self.cursorimg = pygame.image.load("Menu_Cursor.png")
        else:
            self.cursorimg = pygame.image.load("blank.png")            
            
        self.cursorimgrect = self.cursorimg.get_rect()

        #if the gamestate is in menu
        if self.theButtons.getMenustate() == 0:
        #then match the blit to the current button
            #button on FIGHT
            if self.theButtons.getCurrentbutton() == 0:
                self.display.blit(self.cursorimg, (575+13-self.fightButton.get_rect().width/2-28, 483+13-self.fightButton.get_rect().height/2))
            #button on SWITCH
            elif self.theButtons.getCurrentbutton() == 1:
                self.display.blit(self.cursorimg, (725-13-self.switchButton.get_rect().width/2-28, 483+13-self.switchButton.get_rect().height/2))
            #button on FORFEIT
            elif self.theButtons.getCurrentbutton() == 2:
                self.display.blit(self.cursorimg, (725-13-self.forfeitButton.get_rect().width/2-28, 565-13-self.forfeitButton.get_rect().height/2))


        #if the menustate is on moves
        if self.theButtons.getMenustate() == 1:
            #button on move 1
            if self.theButtons.getCurrentbutton() == 0:
                self.display.blit (self.cursorimg, (134-self.move1.get_rect().width/2-28, 496-self.move1.get_rect().height/2))
            #button on move 2
            elif self.theButtons.getCurrentbutton() == 1:
                self.display.blit (self.cursorimg, (368-self.move2.get_rect().width/2-28, 496-self.move2.get_rect().height/2))
            #button on move 3
            elif self.theButtons.getCurrentbutton() == 2:
                self.display.blit (self.cursorimg, (134-self.move3.get_rect().width/2-28, 552-self.move3.get_rect().height/2))
            #button on move 4
            elif self.theButtons.getCurrentbutton() == 3:
                self.display.blit (self.cursorimg, (368-self.move4.get_rect().width/2-28, 552-self.move4.get_rect().height/2))


        #if the menustate is on switch
        if self.theButtons.getMenustate() ==2:
            #button on pokemon 1
            if self.theButtons.getCurrentbutton() == 0:
                self.display.blit (self.cursorimg, (134-self.switch1.get_rect().width/2-28, 496-self.switch1.get_rect().height/2))
            #button on pokemon 2
            elif self.theButtons.getCurrentbutton() == 1:
                self.display.blit (self.cursorimg, (368-self.switch2.get_rect().width/2-28, 496-self.switch2.get_rect().height/2))
            #button on pokemon 3
            elif self.theButtons.getCurrentbutton() == 2:
                self.display.blit (self.cursorimg, (134-self.switch3.get_rect().width/2-28, 552-self.switch3.get_rect().height/2))

        #if the menustate is on forfeit
        if self.theButtons.getMenustate() == 3:
            #button on yes
            if self.theButtons.getCurrentbutton() == 0:
                self.display.blit (self.cursorimg, (170-self.forfeit1.get_rect().width/2-28, 522-self.forfeit1.get_rect().height/2))
            #button on no
            elif self.theButtons.getCurrentbutton() == 1:
                self.display.blit (self.cursorimg, (330-self.forfeit2.get_rect().width/2-28, 522-self.forfeit2.get_rect().height/2))



        #if the gamestate is in the moves
        if self.moveVisible == True:
            self.display.blit(self.move1, (134-self.move1.get_rect().width/2, 496-self.move1.get_rect().height/2))
            self.display.blit(self.move2, (368-self.move2.get_rect().width/2, 496-self.move2.get_rect().height/2))
            self.display.blit(self.move3, (134-self.move3.get_rect().width/2, 552-self.move3.get_rect().height/2))
            self.display.blit(self.move4, (368-self.move4.get_rect().width/2, 552-self.move4.get_rect().height/2))
        #if the gamestate is in switch
        elif self.switchVisible == True:
            self.display.blit(self.switch1, (134-self.switch1.get_rect().width/2, 496-self.switch1.get_rect().height/2))
            self.display.blit(self.switch2, (368-self.switch2.get_rect().width/2, 496-self.switch2.get_rect().height/2))
            self.display.blit(self.switch3, (134-self.switch3.get_rect().width/2, 552-self.switch3.get_rect().height/2))
        #if the gamestate is in quit
        elif self.forfeitVisible == True:
            self.display.blit(self.forfeit1, (170-self.forfeit1.get_rect().width/2, 522-self.forfeit1.get_rect().height/2))
            self.display.blit(self.forfeit2, (330-self.forfeit2.get_rect().width/2, 522-self.forfeit2.get_rect().height/2))

        #draw the pokemon for the player
    def update(self):
        self.poke1Name = self.receivedPokeList[self.receivedPokeIndex].name.upper()
        self.poke2Name = self.receivedEnemyPoke.name.upper()
        
        self.receivedPokeList = self.game.pokemans#(40, 225)
        self.receivedPokeIndex = self.game.activePoke
        self.receivedEnemyPoke = self.game.oppPoke #(535, 65)
        
        self.move1 = self.myfont.render(self.receivedPokeList[self.receivedPokeIndex].moveset[0].moveName, 1, BLACK)
        self.move2 = self.myfont.render(self.receivedPokeList[self.receivedPokeIndex].moveset[1].moveName, 1, BLACK)
        self.move3 = self.myfont.render(self.receivedPokeList[self.receivedPokeIndex].moveset[2].moveName, 1, BLACK)
        self.move4 = self.myfont.render(self.receivedPokeList[self.receivedPokeIndex].moveset[3].moveName, 1, BLACK)

        #variables for the player's health bar
        self.p1healthMax = self.game.pokemans[self.game.activePoke].stats[5]
        self.p1currentHealth = self.game.pokemans[self.game.activePoke].current
        self.p1healthPercentage = 100*self.p1currentHealth/self.p1healthMax

        #variables for the enemy's health bar
        self.p2healthMax = self.game.oppPoke.stats[5]
        self.p2currentHealth = self.game.oppPoke.current
        self.p2healthPercentage = 100*self.p2currentHealth/self.p2healthMax
        content = ["Battle"]
                        #state changes
        if self.theButtons.getMenustate() == 0 and self.theButtons.getCurrentbutton() == 0:
                        # hovering moves

            if self.game.eventManager.right: #right button
                self.theButtons.setCurrentbutton(1)
            elif self.game.eventManager.enter: #enter button
                self.theButtons.setMenustate(1)
                self.theButtons.setCurrentbutton(0)
                self.moveVisible = True

        elif self.theButtons.getMenustate() == 0 and self.theButtons.getCurrentbutton() == 1:
                        # hovering switch
            if self.game.eventManager.down: #down button
                self.theButtons.setCurrentbutton(2)
            elif self.game.eventManager.left: #left button
                self.theButtons.setCurrentbutton(0)
            elif self.game.eventManager.enter: #enter button
                self.theButtons.setMenustate(2)
                self.theButtons.setCurrentbutton(0)
                self.switchVisible = True
            
        elif self.theButtons.getMenustate() == 0 and self.theButtons.getCurrentbutton() == 2:
                        # hovering forfeit
            if self.game.eventManager.up: #up button
                self.theButtons.setCurrentbutton(1)
            elif self.game.eventManager.enter: #enter button
                self.theButtons.setMenustate(3)
                self.theButtons.setCurrentbutton(0)
                self.forfeitVisible = True

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
                self.theButtons.setMenustate(0)
                self.theButtons.setCurrentbutton(0)
                self.moveVisible =False
                self.switchVisible = False
                self.forfeitVisible = False
                self.game.wait = True

        elif self.theButtons.getMenustate() == 1 and self.theButtons.getCurrentbutton() == 1:
                        # hovering move 2
            if self.game.eventManager.down: #down button
                self.theButtons.setCurrentbutton(3)
            elif self.game.eventManager.left: #left button
                self.theButtons.setCurrentbutton(0)
            elif self.game.eventManager.enter:#sends moves[1]
                content.append(0)
                content.append(1)
                self.game.networkManager.sendPacket(content)
                self.theButtons.setMenustate(0)
                self.theButtons.setCurrentbutton(0)
                self.moveVisible =False
                self.switchVisible = False
                self.forfeitVisible = False
                self.game.wait = True
                    
        elif self.theButtons.getMenustate() == 1 and self.theButtons.getCurrentbutton() == 2:
                        #hovering move 3
            if self.game.eventManager.up: #up button
                self.theButtons.setCurrentbutton(0)
            elif self.game.eventManager.right: #right button
                self.theButtons.setCurrentbutton(3)
            elif self.game.eventManager.enter:#sends moves[2]
                content.append(0)
                content.append(2)
                self.game.networkManager.sendPacket(content)
                self.theButtons.setMenustate(0)
                self.theButtons.setCurrentbutton(0)
                self.moveVisible =False
                self.switchVisible = False
                self.forfeitVisible = False
                self.game.wait = True

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
                self.theButtons.setMenustate(0)
                self.theButtons.setCurrentbutton(0)
                self.moveVisible =False
                self.switchVisible = False
                self.forfeitVisible = False
                self.game.wait = True

        elif self.theButtons.getMenustate() == 2 and self.theButtons.getCurrentbutton() == 0:
                        #hovering poke 1
            if self.game.eventManager.right: #right button
                self.theButtons.setCurrentbutton(1)
            elif self.game.eventManager.down: #down button
                self.theButtons.setCurrentbutton(2)
            elif self.game.eventManager.enter:#sends swap[0]
                content.append(1)
                content.append(0)
                if(self.receivedPokeIndex!=0 and self.receivedPokeList[0].current != 0):#checking to see if it's current pokemon
                    self.game.networkManager.sendPacket(content)
                    self.theButtons.setMenustate(0)
                    self.theButtons.setCurrentbutton(1)
                    self.moveVisible =False
                    self.switchVisible = False
                    self.forfeitVisible = False
                    self.game.wait = True

        elif self.theButtons.getMenustate() == 2 and self.theButtons.getCurrentbutton() == 1:
                        #hovering poke 2
            if self.game.eventManager.left: #left button
                self.theButtons.setCurrentbutton(0)
            elif self.game.eventManager.enter:#sends swap[1]
                content.append(1)
                content.append(1)
                if(self.receivedPokeIndex!=1 and self.receivedPokeList[1].current != 0):#checking to see if it's current pokemon
                    self.game.networkManager.sendPacket(content)
                    self.theButtons.setMenustate(0)
                    self.theButtons.setCurrentbutton(1)
                    self.moveVisible =False
                    self.switchVisible = False
                    self.forfeitVisible = False
                    self.game.wait = True

        elif self.theButtons.getMenustate() == 2 and self.theButtons.getCurrentbutton() == 2:
                        #hovering poke 3
            if self.game.eventManager.up: #up button
                self.theButtons.setCurrentbutton(0)
            elif self.game.eventManager.enter:#sends swap[2]
                content.append(1)
                content.append(2)
                if(self.receivedPokeIndex!=2 and self.receivedPokeList[2].current != 0):#checking to see if it's current pokemon
                    self.game.networkManager.sendPacket(content)
                    self.theButtons.setMenustate(0)
                    self.theButtons.setCurrentbutton(1)
                    self.moveVisible =False
                    self.switchVisible = False
                    self.forfeitVisible = False
                    self.game.wait = True
            
        elif self.theButtons.getMenustate() == 3 and self.theButtons.getCurrentbutton() == 0:
                        #hovering yes
            if self.game.eventManager.right: #right button
                self.theButtons.setCurrentbutton(1)
            elif self.game.eventManager.enter:#sends ff
                content.append(2)
                content.append(0)
                self.game.networkManager.sendPacket(content)
                self.theButtons.setMenustate(0)
                self.theButtons.setCurrentbutton(2)
                self.moveVisible =False
                self.switchVisible = False
                self.forfeitVisible = False
                self.game.wait = True

        elif self.theButtons.getMenustate() == 3 and self.theButtons.getCurrentbutton() == 1:
                        #hovering no
            if self.game.eventManager.left: #left button
                self.theButtons.setCurrentbutton(0)
            elif self.game.eventManager.enter:
                self.theButtons.setMenustate(0)
                self.theButtons.setCurrentbutton(0)
                self.theButtons.setMenustate(0)
                self.theButtons.setCurrentbutton(2)
                self.moveVisible =False
                self.switchVisible = False
                self.forfeitVisible = False
                self.game.wait = True

        if self.theButtons.getMenustate() == 1:
            if self.game.eventManager.cancel:
                self.theButtons.setMenustate(0)
                self.theButtons.setCurrentbutton(0)
                self.moveVisible =False
                self.switchVisible = False
                self.forfeitVisible = False
        elif self.theButtons.getMenustate() == 2:
            if self.game.eventManager.cancel:
                self.theButtons.setMenustate(0)
                self.theButtons.setCurrentbutton(1)
                self.moveVisible =False
                self.switchVisible = False
                self.forfeitVisible = False
        elif self.theButtons.getMenustate() == 3:
            if self.game.eventManager.cancel:
                self.theButtons.setMenustate(0)
                self.theButtons.setCurrentbutton(2)
                self.moveVisible =False
                self.switchVisible = False
                self.forfeitVisible = False

        if(self.game.wait==True):
            self.draw()
            return
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                pygame.display.update()
