from NetworkManager import *
import pygame
from EventManager import *
from TextInput import *
from pokeman import pokeman
from Battle_Window import *
from random import randint
from Battletext import battletext
from TextScroll import *
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
        self.rapper = pygame.image.load('NAKEDMAN2.png')
        self.rapperw = self.rapper.get_rect().width
        self.gangster = pygame.image.load('NAKEDMAN3.png')
        self.gangsterw = self.gangster.get_rect().width
        self.child = pygame.image.load('NAKEDMAN4.png')
        self.childw = self.child.get_rect().width
        self.hobo = pygame.image.load('NAKEDMAN.png')
        self.hobow = self.hobo.get_rect().width
        self.nerd = pygame.image.load('NAKEDMAN5.png')
        self.nerdw = self.nerd.get_rect().width
        self.select = pygame.image.load('select.png')
        self.selectw = self.select.get_rect().width
        self.wait = False
        # Processes events (essentially all inputs)
        self.eventManager = EventManager(self)

        # Brings up a TextInput that'll be used to enter in text
        self.textInput = TextInput(self)
        self.p1name = ''
        self.p2name = ''

        pygame.display.set_caption("POKEMANS")
        self.screen = pygame.display.set_mode((800, 600))
        self.streak = 0
        self.running = True
        self.state = "Pre-Login"
        
        self.battlestr = ''
        
        self.draft = [pokeman(1,0),pokeman(2,0),pokeman(3,0)] # The pokemans in the draft
        self.pokemans = [] # The pokemans selected
        self.gameState = [] # gameState in battle

        # Sends an alive packet periodically to the server to tell that a player is still online
        self.aliveClock = pygame.time.Clock()
        self.aliveTimer = 0 # Timer to keep track of the clock

        self.sel = 0
        self.login = 0
        self.timer1 = 0
        self.preb_timer = 0
        self.preb = True
        self.flash1 = False
        self.networkManager = NetworkManager(self)
        
        colorPicker = randint(0, 5)
        backgroundColor = None
        if colorPicker == 0:
            backgroundColor = (255, 0, 0)
        elif colorPicker == 1:
            backgroundColor = (0, 255, 0)
        elif colorPicker == 2:
            backgroundColor = (0, 0, 255)
        elif colorPicker == 3:
            backgroundColor = (255, 255, 0)
        elif colorPicker == 4:
            backgroundColor = (0, 255, 255)
        elif colorPicker == 5:
            backgroundColor = (255, 0, 255)

        self.background = pygame.Surface((800, 600))
        self.background.set_alpha(50)
        self.background.fill(backgroundColor)

        self.textScroll = TextScroll(self)
    
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
            return self.rapper
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
#                 self.state = "Pre-Battle"
                self.state = "Battle"
                self.wait = False
                '''
                Replace the GameState object of the client with
                the received gameState in data[1]

                The GameState should be in the state managements
                '''
                self.gameState = data[1]
#                 self.window = Battle_Window(self)
            elif command == "BattleStart":
                self.textScroll.clear()
                self.eventManager.textScrollActive = False
                self.textScroll.waitForFlee = False
                self.state = "Battle"
                self.preb = True
                self.preb_timer = pygame.time.get_ticks()
                self.activePoke = 0
                self.oppPoke = data[1]
                self.p2name = data[2]
                self.gameState = []
                self.gameState.append(self.pokemans)
                self.gameState.append(self.activePoke)
                self.gameState.append(self.oppPoke)
                self.battle_window = Battle_Window(self)
                print("Switched to Battle")
            elif command == "BattleWait":
                self.wait = True
            elif command == "Battletext":
                if data[2] != 'FF':
                    self.battlestr = battletext(self,data)
                    self.battlestr += '  ' + battletext(self,data[3:len(data)])
                else:
                    self.battlestr = battletext(self,data)
                    if data[1] == 1:
                        self.textScroll.waitForFlee = True
                print("Battletext:",self.battlestr)
                self.textScroll.load(self.battlestr)
            elif command == "Result":
                if data[1] == "Win":
                    self.streak+=1
                    for pokeman in self.pokemans:
                        pokeman.current = pokeman.stats[5]
                    if not self.textScroll.waitForFlee:
                        self.state = "Queue"
                if data[1] == "Loss":
                    self.streak = 0
                    self.pokemans = []
                    self.state = "Draft"
                
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
            self.textScroll.clear()
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
                    self.activePoke = 0
                    self.state = "Queue"
                    print(self.pokemans)
                    
                    print()
                    print("Switched to Queue")

        elif self.state == "Queue":
            self.eventManager.textScrollActive = False
            self.textScroll.clear()
            # For now, we don't do anything, but we could update a waiting
            # animation here or something along the likes
            pass

        elif self.state == "Battle":
            if self.preb != True:
                self.pokemans=self.gameState[0]
                self.activePoke= self.gameState[1]
                self.oppPoke = self.gameState[2]
                self.battle_window.update()
                self.textScroll.update()
    def draw(self):
        self.screen.fill((255,255,255))
        if self.state == "Pre-Login":
            enterf = pygame.time.get_ticks()
            if self.login == 0:
                pokemon = self.font64.render('POKEMANS',0,(0,0,0))
                pokemonwidth = pokemon.get_rect().width
                self.screen.blit(pokemon,(400-pokemonwidth*0.5,300-pokemon.get_rect().height/2 - 10))
                if enterf - self.timer1 > 500:
                    self.timer1 = enterf
                    if self.flash1 == True:
                        self.flash1 = False
                    else:
                        self.flash1 = True
                if self.flash1 == True:
                    pEnter = self.font16.render('PRESS ENTER TO CONTINUE',0,(0,0,0))
                    pEnterwidth = pEnter.get_rect().width
                    self.screen.blit(pEnter,(400-pEnterwidth*0.5,350 - 10))
            elif self.login == 1:
                text1 = self.font16.render('In the not so distant future, the upper class'.upper(),0,(0,0,0))
                text2 = self.font16.render('has been gathered by the god emperor Kappa,'.upper(),0,(0,0,0))
                text3 = self.font16.render('the lord of Kappa-talism.  In his infinite wisdom he'.upper(),0,(0,0,0))
                text4 = self.font16.render('has decided that too many of his people are in'.upper(),0,(0,0,0))
                text5 = self.font16.render('debt, and to free them he has decided to host'.upper(),0,(0,0,0))
                text6 = self.font16.render('a tournament in which they can fight for'.upper(),0,(0,0,0))
                text7 = self.font16.render('their freedom.'.upper(),0,(0,0,0))
                        
                text8 = self.font16.render('You are a member of the upper class,'.upper(),0,(0,0,0))
                text9 = self.font16.render('your task is to select a team of three indebted'.upper(),0,(0,0,0))
                text10 = self.font16.render('to enter the tournament and fight for'.upper(),0,(0,0,0))
                text11 = self.font16.render('your entertainment.  Your only cost is to pay'.upper(),0,(0,0,0))
                text12 = self.font16.render('their debts as an entry fee and on the'.upper(),0,(0,0,0))
                text13 = self.font16.render('condition that they should the survive 7 matches,'.upper(),0,(0,0,0))
                text14 = self.font16.render('they shall be absolved of all debt and set free.'.upper(),0,(0,0,0))
                textarray = [text1,text2,text3,text4,text5,text6,text7]
                textarray2 = [text8,text9,text10,text11,text12,text13,text14]
                for i in range(0,7):
                    self.screen.blit(textarray[i],(64,50+32*i))
                for i in range(0,7):
                    self.screen.blit(textarray2[i],(64,50+32*i + 32*7 + 50))
                if enterf - self.timer1 > 500:
                    self.timer1 = enterf
                    if self.flash1 == True:
                        self.flash1 = False
                    else:
                        self.flash1 = True
                if self.flash1 == True:
                    pEnter = self.font16.render('PRESS ENTER TO CONTINUE',0,(0,0,0))
                    pEnterwidth = pEnter.get_rect().width
                    self.screen.blit(pEnter,(400-pEnterwidth*0.5,560))
            elif self.login == 2:
                tips = self.font32.render('TIPS',0,(0,0,0))
                tipsw = tips.get_rect().width
                self.screen.blit(tips,(400-tipsw*0.5,32))
                tips1 = self.font16.render('THERE ARE TWO TYPES OF DAMAGE: PHYSICAL AND SPECIAL.',0,(0,0,0))
                tips1w = tips1.get_rect().width
                self.screen.blit(tips1,(400-tips1w*0.5,96))
                tips2 = self.font16.render('SOME TYPES OF ATTACKS ARE STRONGER OR WEAKER',0,(0,0,0))
                tips2w = tips2.get_rect().width
                self.screen.blit(tips2,(400-tips2w*0.5,96+64))
                tips3 = self.font16.render('AGAINST VARIOUS POKEMANS.',0,(0,0,0))
                tips3w = tips3.get_rect().width
                self.screen.blit(tips3,(400-tips3w*0.5,96+3*32))
                tips4 = self.font16.render("EVERY POKEMAN'S FIRST TWO MOVES BELONG TO HIS TYPE,",0,(0,0,0))
                tips4w = tips4.get_rect().width
                self.screen.blit(tips4,(400-tips4w*0.5,96 + 5*32))
                tips5 = self.font16.render('THE LAST TWO DO NOT BELONG TO HIS TYPE.',0,(0,0,0))
                tips5w = tips5.get_rect().width
                self.screen.blit(tips5,(400-tips5w*0.5,96+6*32))
                if enterf - self.timer1 > 500:
                    self.timer1 = enterf
                    if self.flash1 == True:
                        self.flash1 = False
                    else:
                        self.flash1 = True
                if self.flash1 == True:
                    pEnter = self.font16.render('PRESS ENTER TO CONTINUE',0,(0,0,0))
                    pEnterwidth = pEnter.get_rect().width
                    self.screen.blit(pEnter,(400-pEnterwidth*0.5,560))
        if self.state == "Login":
            self.textInput.draw()
        if self.state == "Draft":
            enterf = pygame.time.get_ticks()            
            if enterf - self.timer1 > 500:
                self.timer1 = enterf
                if self.flash1 == True:
                    self.flash1 = False
                else:
                    self.flash1 = True

            pokestring = ''
            for p in self.pokemans:
                pokestring += (str(p)) + ' the ' + p.typeName + ', '
            pokestring = pokestring[0:-2]
            self.screen.blit(self.font16.render('ROSTER: ' + pokestring,0,(0,0,0)),(400 - self.font16.render('ROSTER: ' + pokestring,0,(0,0,0)).get_rect().width*0.5,550))
            
            self.screen.blit(self.font32.render('DRAFT',0,(0,0,0)),(400-self.font32.render('DRAFT',0,(0,0,0)).get_rect().width/2,32))
            if self.draft != []:
                for i in range(3):
                    self.screen.blit(self.drawpokeman(self.draft[i].type),(150+ 250*i-self.nerdw*0.5 ,100))
                    self.screen.blit(self.font16.render(self.draft[i].name,0,(0,0,0)),(150+ 250*i-self.font16.render(self.draft[i].name,0,(0,0,0)).get_rect().width*0.5,250))
                    self.screen.blit(self.font16.render(self.draft[i].typeName,0,(0,0,0)),(150+ 250*i-self.font16.render(self.draft[i].typeName,0,(0,0,0)).get_rect().width*0.5,275))
                    for s in range(6):
                        self.screen.blit(self.font16.render(self.stattype(s) + ': ' +str(self.draft[i].stats[s]),0,(0,0,0)),(150+ 250*i - 50,300+20*s))
                    for s in range(4):
                        self.screen.blit(self.font16.render(str(self.draft[i].moveset[s].moveName).upper(),0,(0,0,0)),(150+ 250*i - 55,450+20*s))
            if self.flash1:
                self.screen.blit(self.select,(150 + 250*self.sel-self.selectw*0.5,60
))
            rect = pygame.Rect(150 + 250*self.sel - 100, 90, 200, 450)
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 5)
        
        if self.state == "Queue":
            self.screen.blit(self.font32.render('YOUR ROSTER: ',0,(0,0,0)),(240,16))
            self.screen.blit(self.font16.render('(CURRENTLY IN QUEUE)',0,(0,0,0)),(280,64))
            for i in range(3):
                self.screen.blit(self.drawpokeman(self.pokemans[i].type),(150+ 250*i-self.nerdw*0.5 ,100))
                self.screen.blit(self.font16.render(self.pokemans[i].typeName,0,(0,0,0)),(150+ 250*i-self.font16.render(self.pokemans[i].typeName,0,(0,0,0)).get_rect().width*0.5,275))
                self.screen.blit(self.font16.render(self.pokemans[i].name,0,(0,0,0)),(150+ 250*i-self.font16.render(self.pokemans[i].name,0,(0,0,0)).get_rect().width*0.5,250))
                for s in range(6):
                    self.screen.blit(self.font16.render(self.stattype(s) + ': ' +str(self.pokemans[i].stats[s]),0,(0,0,0)),(150+ 250*i - 50,300+20*s))
                for s in range(4):
                    self.screen.blit(self.font16.render(str(self.pokemans[i].moveset[s].moveName).upper(),0,(0,0,0)),(150+ 250*i - 55,450+20*s))
            self.screen.blit(self.font16.render('WINSTREAK: ' + str(self.streak),0,(0,0,0)),(400 - self.font16.render('WINSTREAK: ' + str(self.streak),0,(0,0,0)).get_rect().width*0.5,550))
        
        if self.state == "Battle":
            if self.preb == True:
                self.screen.blit(self.font32.render(self.p1name,0,(0,0,0)),(150 - self.font32.render(self.p1name,0,(0,0,0)).get_rect().width*0.5,284))
                self.screen.blit(self.font32.render(self.p2name,0,(0,0,0)),(650 - self.font32.render(self.p2name,0,(0,0,0)).get_rect().width*0.5,284))
                self.screen.blit(self.font64.render("BATTLE FOUND!",0,(0,0,0)),(400 - self.font64.render("BATTLE FOUND!",0,(0,0,0)).get_rect().width*0.5,64))
                self.screen.blit(self.font64.render("VS",0,(0,0,0)),(400 - self.font64.render("VS",0,(0,0,0)).get_rect().width*0.5,300-self.font64.render("VS",0,(0,0,0)).get_rect().height*0.5))
                self.screen.blit(self.font64.render(str(int(6 - ((pygame.time.get_ticks() - self.preb_timer) /1000))),0,(0,0,0)),(400 - self.font64.render(str(int(5 - ((pygame.time.get_ticks() - self.preb_timer) /1000))),0,(0,0,0)).get_rect().width*0.5,450))
                if pygame.time.get_ticks() - self.preb_timer > 5000:
                    self.preb = False
            else:
                self.battle_window.draw()
                self.textScroll.draw()

        self.screen.blit(self.background, (0,0))

        pygame.display.flip()
        
    # This is ran in main after the game.running is set to false
    def disconnect(self):
        self.networkManager.disconnect()
