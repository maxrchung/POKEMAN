import pygame
from mechanics import effectiveness

class Battle:
    def __init__(self, client1, client2):
        self.client1 = client1 
        self.client2 = client2
        self.playerOne = client1.pokemans
        self.playerTwo = client2.pokemans
        self.client1.win = False
        self.client1.lose = False
        self.client2.win = False
        self.client2.lose = False
        self.pokeOne = self.playerOne[0] #active pokeman 1
        self.pokeTwo = self.playerTwo[0] #active pokeman 2
        self.buffsOne = [0,0,0,0,0] #buffs array for p1
        self.over = False
        self.buffsTwo = [0,0,0,0,0] #buffs array for p2
        # So we don't send too many game updates at once
        # Only sends a game update after a certain updateTimer limit has passed
        self.updateClock = pygame.time.Clock()
        self.updateTimer = 0
        
        self.lastTurn = []

        # self.gameState = GameState()

    def update(self):
        # Update gameState here
        # self.gameState.update()
        self.pokeOne = self.playerOne[self.client1.active] #updates the active pokeman
        self.pokeTwo = self.playerTwo[self.client2.active] #^
        self.updateTimer += self.updateClock.tick() 
        if self.updateTimer > 50:
            self.updateTimer = 0
            # After the battles are updated, send the gamestate out if
            if(self.client1.win or self.client1.lose): #if there is a loser
                self.over = True #quit
                return
            if(self.client1.ready and self.client2.ready):#if they have both sent commands
                print(self.client1.waitingCommand, self.client2.waitingCommand) #what command they sent
                self.turn(self.client1.waitingCommand[0],self.client1.waitingCommand[1],self.client2.waitingCommand[0],self.client2.waitingCommand[1])
                print("Just sent a command")

                #sends a packet to each client with the relevant information
                pState1 = [self.client1.pokemans,self.client1.active,self.client2.pokemans[self.client2.active]]
                pState2 = [self.client2.pokemans,self.client2.active,self.client1.pokemans[self.client1.active]]
                content1 = ["Battle", pState1]
                content2 = ["Battle", pState2]
                self.client1.ready = False #resets to a command isn't sent
                self.client2.ready = False
                self.client1.sendPacket(content1)
                self.client2.sendPacket(content2)
            if not(self.client1.ready or self.client2.ready): #if someone didn't send a command update
                pState1 = [self.client1.pokemans,self.client1.active,self.client2.pokemans[self.client2.active]]
                pState2 = [self.client2.pokemans,self.client2.active,self.client1.pokemans[self.client1.active]]
                content1 = ["Battle", pState1]
                content2 = ["Battle", pState2]
#                 self.client1.sendPacket(content1)
#                 self.client2.sendPacket(content2)
    def turn(self, commandOne, indexOne, commandTwo, indexTwo):
        self.lastTurn = [commandOne, indexOne, commandTwo, indexTwo]
        if commandOne == 2: #if p1 flees
            self.client1.lose=True
            self.client2.win=True
            return
        if commandTwo == 2: #p2 flees
            self.client2.lose=True
            self.client1.win =True
            return
        if commandOne == 1 or commandTwo == 1: #someone is swapping out 
            if commandOne == 1: #swap1
                self.client1.active = indexOne
                self.pokeOne = self.playerOne[indexOne]
            if commandTwo == 1: #swap2
                self.client2.active = indexTwo
                self.pokeTwo = self.playerTwo[indexTwo]
        if commandOne == 0 and commandTwo == 0: #no one is swapping out
            if self.pokeOne.stats[4] >= self.pokeTwo.stats[4]: #based on speed
                #issue command 1
                self.command(1,self.pokeOne.moveset[indexOne])
                #issue command 2
                self.command(2,self.pokeTwo.moveset[indexTwo])
            else:
                # command 2
                self.command(2,self.pokeTwo.moveset[indexTwo])
                # command 1
                self.command(1,self.pokeOne.moveset[indexOne])
        elif commandOne == 0: #happens after swap
            # command 1
            self.command(1,self.pokeOne.moveset[indexOne])
        elif commandTwo == 0:
            # command 2
            self.command(2,self.pokeTwo.moveset[indexTwo])
    '''
    0 is move
    1 is swap
    2 is flee
    '''
    def command(self,player,ability): #used for moves
        if(ability.buff==True):
            if(ability.buffstat!=5): #not a heal
                if(player==1):
                    self.buffsOne[ability.buffstat]+=10
                else:
                    self.buffsTwo[ability.buffstat]+=10
            else: #heal
                if(player == 1):
                    if(self.pokeOne.current<self.pokeOne.stats[5]-20):
                        self.pokeOne.current+=20
                else:
                    if(self.pokeTwo.current<self.pokeTwo.stats[5]-20):
                        self.pokeTwo.current+=20
        else: #it's an attack
            if(player == 1): #p1
                self.pokeTwo.current-=self.damage(self.pokeOne,self.pokeTwo,ability)
                if self.pokeTwo.current<0: #if p2 is dead
                    self.pokeTwo.current=0 
                    x = self.nextActive(self.playerTwo)
                    if x != -1: #they have another alive pokeman
                        self.client2.active = x
                    else:
                        self.client2.lose=True
                        self.client1.win =True
                    #ded
            else: #p2
                self.pokeOne.current-=self.damage(self.pokeTwo,self.pokeOne,ability)
                if self.pokeOne.current<0:
                    self.pokeOne.current=0
                    self.client1.active = self.nextActive(self.playerOne)
                    x = self.nextActive(self.playerTwo)
                    if x != -1:
                        self.client2.active = x
                    else:
                        self.client1.lose=True
                        self.client2.win =True
                    #ded

    def damage(self,attker,defender,ability):
        if(attker.type==ability.type):
            stab=1.5
        else:
            stab=1
        if(ability.type==0): #physical
            return ability.power*attker.stats[0]/defender.stats[1]*stab*effectiveness(ability,defender)
        else: #special
            return ability.power*attker.stats[2]/defender.stats[3]*stab*effectiveness(ability,defender)
    def nextActive(self,pokeList): #returns the next alive pokemon in the list
        for i in range (3):
            if pokeList[i].current !=0:
                return i
        return -1    
        