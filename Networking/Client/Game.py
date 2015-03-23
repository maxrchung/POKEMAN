from NetworkManager import *
import pygame
from EventManager import *
from TextInput import *
from pokeman import pokeman

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.font16 = pygame.font.Font("PKMN RBYGSC.ttf", 16)
        self.font32 = pygame.font.Font("PKMN RBYGSC.ttf", 32)

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
        self.state = "Login"
        
        self.draft = [pokeman(1,0),pokeman(2,0),pokeman(3,0)] # The pokemans in the draft
        self.pokemans = [] # The pokemans selected
        self.gameState = [] # gameState in battle

        self.sel = 0
        self.networkManager = NetworkManager(self)
    def run(self):
        self.update()
        self.draw()

    def stattype(self,num):
        if num == 0:
            return 'Atk'
        elif num == 1:
            return 'Def'
        elif num == 2:
            return 'Satk'
        elif num == 3:
            return 'Sdef'
        elif num == 4:
            return 'Spd'
        elif num == 5:
            return 'Hp'
    
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
        self.eventManager.run()

        # Handles processing of messages
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
                
        self.networkManager.messageLock.release()

        if self.state == "Login":
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
            '''
            Update the GameState here
            gameState.update()
            '''
            pass

    def draw(self):
        self.screen.fill((255,255,255))

        if self.state == "Login":
            self.textInput.draw()
        if self.state == "Draft":
            self.screen.blit(self.font32.render('Draft',1,(0,0,0)),(350,50))
            if self.draft != []:
                for i in range(3):
                    self.screen.blit(self.drawpokeman(self.draft[i].type),(100+ 250*i,100))
                    for s in range(6):
                        self.screen.blit(self.font16.render(self.stattype(s) + ': ' +str(self.draft[i].stats[s]),1,(0,0,0)),(125+ 250*i,250+20*s))
                    for s in range(4):
                        self.screen.blit(self.font16.render(str(self.draft[i].moveset[s].moveName),1,(0,0,0)),(125+ 250*i,400+20*s))
            self.screen.blit(self.select,(164 + 250*self.sel,75))            

        pygame.display.flip()
        
    # This is ran in main after the game.running is set to false
    def disconnect(self):
        # For now, I'm not gonna worry about it, but we'll need to worry about
        # Sending disconnect packet
        # Disconnecting sockets
        pass
