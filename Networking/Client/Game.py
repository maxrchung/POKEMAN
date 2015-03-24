from NetworkManager import *
import pygame
from EventManager import *
from TextInput import *
from pokeman import pokeman
from Battle_Window import *
class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.font16 = pygame.font.Font("PKMN RBYGSC.ttf", 16)
        self.font32 = pygame.font.Font("PKMN RBYGSC.ttf", 32)
        self.font64 = pygame.font.Font("PKMN RBYGSC.ttf", 64)
        #must be something real troll to use anything bigger than 64
        self.font128 = pygame.font.Font("PKMN RBYGSC.ttf", 128)
        self.font256 = pygame.font.Font("PKMN RBYGSC.ttf", 256)
        self.gangster = pygame.image.load('criminal.png')
        self.child = pygame.image.load('delinq.png')
        self.hobo = pygame.image.load('hobo.png')
        self.nerd = pygame.image.load('nerd.png')
        self.select = pygame.image.load('select.png')

        # Processes events (essentially all inputs)
        self.eventManager = EventManager(self)

        # Brings up a TextInput that'll be used to enter in text
        self.textInput = TextInput(self)

        pygame.display.set_caption("POKEMANS")
        self.screen = pygame.display.set_mode((800, 600))

        self.running = True
        self.state = "Pre-Login"
        
        self.draft = [pokeman(1,0),pokeman(2,0),pokeman(3,0)] # The pokemans in the draft
        self.pokemans = [] # The pokemans selected
        self.gameState = [] # gameState in battle

        # Sends an alive packet periodically to the server to tell that a player is still online
        self.aliveClock = pygame.time.Clock()
        self.aliveTimer = 0 # Timer to keep track of the clock

        self.sel = 0
        self.login = 0
        self.timer1 = 0
        self.flash1 = False
        self.networkManager = NetworkManager(self)
        

    
    def run(self):
        self.update()
        self.draw()

    def stattype(self,num):
        if num == 0:
            return 'ATK'
        elif num == 1:
            return 'DEF'
        elif num == 2:
            return 'SATK'
        elif num == 3:
            return 'SDEF'
        elif num == 4:
            return 'SPD'
        elif num == 5:
            return 'HP'
    
    def drawpokeman(self,num):
        if num == 0:
            return self.nerd
        elif num == 1:
            return self.nerd
        elif num == 2:
            return self.child
        elif num == 3:
            return self.gangster
        elif num == 4:
            return self.hobo

    def update(self):
        self.aliveTimer += self.aliveClock.tick()
        if self.aliveTimer > 5000:
            self.aliveTimer = 0
            content = ["Alive"]
            self.networkManager.sendPacket(content)

        self.eventManager.run()

        # Handles processing of messages
        self.networkManager.messageLock.acquire()
        while len(self.networkManager.messageQueue) > 0:
            data = self.networkManager.messageQueue.popleft()
            print("Received:", data)
            command = data[0]

            # The server drafts 3 cards for the client
            # Process these into the drafting phase
            if command == "Draft" :
                '''
                Put into some draft data structure
                '''
                self.state = "Draft"
                self.draft = data[1] # Temporary placeholder

            elif command == "Battle":
                self.state = "Battle"
                print()
                print("Switched to Battle")
                '''
                Replace the GameState object of the client with
                the received gameState in data[1]

                The GameState should be in the state managements
                '''
                self.gameState = data[1]
                self.window = Battle_Window(self)
                
        self.networkManager.messageLock.release()
        
        if self.state == "Pre-Login":
            if self.eventManager.enter == True:
                if self.login == 0:
                    self.login = 1
                elif self.login == 1:
                    self.login = 2
                elif self.login == 2:
                    self.state = "Login"
        elif self.state == "Login":
            self.textInput.update()
            
        elif self.state == "Draft":
            # Temporary placeholder
            if len(self.draft) > 0:
#                 print("self.draft:", self.draft)
                if self.eventManager.enter == True:
                    self.pokemans.append(self.draft[int(self.sel)])
                    content = ["Draft", self.sel]
                    self.networkManager.sendPacket(content)
                    self.draft = [] # Reset the draft
                if self.sel == 0:
                    if self.eventManager.right == True:
                        self.sel = 1
                elif self.sel == 1:
                    if self.eventManager.right == True:
                        self.sel = 2
                    if self.eventManager.left == True:
                        self.sel = 0
                elif self.sel == 2:
                    if self.eventManager.left == True:
                        self.sel = 1

 
                # If we have drafted 3 pokemon, then jump to queue mode
                if len(self.pokemans) >= 3:
                    print(self.pokemans)
                    self.state = "Queue"
                    print(self.pokemans)
                    print()
                    print("Switched to Queue")

        elif self.state == "Queue":
            # For now, we don't do anything, but we could update a waiting
            # animation here or something along the likes
            pass

        elif self.state == "Battle":
            self.pokemans=self.gamestate[0]
            self.activePoke= self.gamestate[1]
            self.oppPoke = self.gamestate[2]
            '''
            Update the GameState here
            gameState.update()
            '''
            pass

    def draw(self):
        self.screen.fill((255,255,255))
        if self.state == "Pre-Login":
            enterf = pygame.time.get_ticks()
            if self.login == 0:
                pokemon = self.font64.render('POKEMANS',1,(0,0,0))
                pokemonwidth = pokemon.get_rect().width
                self.screen.blit(pokemon,(400-pokemonwidth*0.5,236))
                if enterf - self.timer1 > 1000:
                    self.timer1 = enterf
                    if self.flash1 == True:
                        self.flash1 = False
                    else:
                        self.flash1 = True
                if self.flash1 == True:
                    pEnter = self.font16.render('PRESS ENTER TO CONTINUE',1,(0,0,0))
                    pEnterwidth = pEnter.get_rect().width
                    self.screen.blit(pEnter,(400-pEnterwidth*0.5,400))
            elif self.login == 1:
                text1 = self.font16.render('In the not so distant future, the upper class'.upper(),1,(0,0,0))
                text2 = self.font16.render('has been gathered by the god emperor Kappa,'.upper(),1,(0,0,0))
                text3 = self.font16.render('the lord of Kappa-talism.  In his infinite wisdom he'.upper(),1,(0,0,0))
                text4 = self.font16.render('has decided that too many of his people are in'.upper(),1,(0,0,0))
                text5 = self.font16.render('debt, and to free them he has decided to host'.upper(),1,(0,0,0))
                text6 = self.font16.render('a tournament in which they can fight for'.upper(),1,(0,0,0))
                text7 = self.font16.render('their freedom.'.upper(),1,(0,0,0))
                        
                text8 = self.font16.render('You are a member of the upper class,'.upper(),1,(0,0,0))
                text9 = self.font16.render('your task is to select a team of three indebted'.upper(),1,(0,0,0))
                text10 = self.font16.render('to enter the tournament and fight for'.upper(),1,(0,0,0))
                text11 = self.font16.render('your entertainment.  Your only cost is to pay'.upper(),1,(0,0,0))
                text12 = self.font16.render('their debts as an entry fee and on the'.upper(),1,(0,0,0))
                text13 = self.font16.render('condition that they should the survive 7 matches,'.upper(),1,(0,0,0))
                text14 = self.font16.render('they shall be absolved of all debt and set free.'.upper(),1,(0,0,0))
                textarray = [text1,text2,text3,text4,text5,text6,text7]
                textarray2 = [text8,text9,text10,text11,text12,text13,text14]
                for i in range(0,7):
                    self.screen.blit(textarray[i],(64,50+32*i))
                for i in range(0,7):
                    self.screen.blit(textarray2[i],(64,50+32*i + 32*7 + 50))
                if enterf - self.timer1 > 700:
                    self.timer1 = enterf
                    if self.flash1 == True:
                        self.flash1 = False
                    else:
                        self.flash1 = True
                if self.flash1 == True:
                    pEnter = self.font16.render('PRESS ENTER TO CONTINUE',1,(0,0,0))
                    pEnterwidth = pEnter.get_rect().width
                    self.screen.blit(pEnter,(400-pEnterwidth*0.5,560))
            elif self.login == 2:
                tips = self.font32.render('TIPS',1,(0,0,0))
                tipsw = tips.get_rect().width
                self.screen.blit(tips,(400-tipsw*0.5,32))
                tips1 = self.font16.render('THERE ARE TWO TYPES OF DAMAGE, PHYSICAL AND SPECIAL.',1,(0,0,0))
                tips1w = tips1.get_rect().width
                self.screen.blit(tips1,(400-tips1w*0.5,96))
                tips2 = self.font16.render('SOME TYPES OF ATTACKS ARE STRONGER OR WEAKER',1,(0,0,0))
                tips2w = tips2.get_rect().width
                self.screen.blit(tips2,(400-tips2w*0.5,96+64))
                tips3 = self.font16.render('AGAINST VARIOUS POKEMANS',1,(0,0,0))
                tips3w = tips3.get_rect().width
                self.screen.blit(tips3,(400-tips3w*0.5,96+3*32))
                tips4 = self.font16.render('EVERY POKEMANS FIRST TWO MOVES BELONG TO HIS TYPE,',1,(0,0,0))
                tips4w = tips4.get_rect().width
                self.screen.blit(tips4,(400-tips4w*0.5,96 + 5*32))
                tips5 = self.font16.render('THE LAST TWO DO NOT BELONG TO HIS TYPE.',1,(0,0,0))
                tips5w = tips5.get_rect().width
                self.screen.blit(tips5,(400-tips5w*0.5,96+6*32))
                if enterf - self.timer1 > 350:
                    self.timer1 = enterf
                    if self.flash1 == True:
                        self.flash1 = False
                    else:
                        self.flash1 = True
                if self.flash1 == True:
                    pEnter = self.font16.render('PRESS ENTER TO CONTINUE',1,(0,0,0))
                    pEnterwidth = pEnter.get_rect().width
                    self.screen.blit(pEnter,(400-pEnterwidth*0.5,560))
        if self.state == "Login":
            self.textInput.draw()
        if self.state == "Draft":
            self.screen.blit(self.font32.render('DRAFT',1,(0,0,0)),(350,32))
            if self.draft != []:
                for i in range(3):
                    self.screen.blit(self.drawpokeman(self.draft[i].type),(100+ 250*i,100))
                    for s in range(6):
                        self.screen.blit(self.font16.render(self.stattype(s) + ': ' +str(self.draft[i].stats[s]),1,(0,0,0)),(125+ 250*i,250+20*s))
                    for s in range(4):
                        self.screen.blit(self.font16.render(str(self.draft[i].moveset[s].moveName).upper(),1,(0,0,0)),(125+ 250*i,400+20*s))
            self.screen.blit(self.select,(164 + 250*self.sel,75))            

        pygame.display.flip()
        
    # This is ran in main after the game.running is set to false
    def disconnect(self):
        self.networkManager.disconnect()
