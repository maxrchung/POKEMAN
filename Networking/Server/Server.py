from NetworkManager import *
from collections import deque
from Battle import *
import random
from pokeman import pokeman

class Server:
    def __init__(self):
        self.running = True
        self.waitingQueue = deque()
        self.networkManager = NetworkManager(self)
        self.battles = []

    def run(self):
        self.update()

    def update(self):
        toRemove = []
        
        # Processes messages received on the server
        self.networkManager.connectionLock.acquire()
        for client in self.networkManager.clients:
            client.aliveTimer += client.aliveClock.tick()
            if client.aliveTimer > 10000: # If more than 10 seconds have passed since the last update, remove the client
                print(client.aliveTimer)
                toRemove.append(client)

            client.messageLock.acquire()
            while len(client.messageQueue) > 0:
                data = client.messageQueue.popleft()
                command = data[0]

                if command == "Alive":
                    client.aliveTimer = 0

                elif command == "Disconnect":
                    toRemove.append(client)

                elif command == "Login":
                    client.name = data[1]
                    '''
                    Generate 3 Pokemon to send to the client
                    For now, I'm just using placeholder ints 0, 1, and 2
                    client.draft = draftPokemans()
                    '''

                    client.draft = [] # clear draft
                    for i in range(3):#new draft
                        r=random.randint(0,4)#random class
                        g=random.randint(0,1)#random gender
                        client.draft.append(pokeman(r,g))

                    content = ["Draft", client.draft]
                    client.sendPacket(content)

                elif command == "Draft":
                    index = data[1]
                    '''
                    Keep track that the client has chosen a particular pokeman
                    '''
                    client.pokemans.append(client.draft[int(index)])

                    # If the client does not have 3, then send another draft
                    # Remember that we need to reset the pokemans list to []
                    # to eliminate length problems!
                    if len(client.pokemans) < 3:
                        client.draft = [] # clear draft
                        for i in range(3):#new draft
                            r=random.randint(0,4)#random class
                            g=random.randint(0,1)#random gender
                            client.draft.append(pokeman(r,g))
                        content = ["Draft", client.draft]
                        client.sendPacket(content)

                    # Else put the client into the queue
                    else:
                        client.draft = [] # Resets draft
                        self.waitingQueue.append(client)
                elif command == "Battle":
                    client.ready=True
                    client.waitingCommand = [data[1],data[2]]
                    content = ["BattleWait"]
                    client.sendPacket(content)

            client.messageLock.release()

        for client in toRemove:
            print('Removed:', client.addr)
            client.disconnect()
            try:
                self.waitingQueue.remove(client)
            except:
                pass
            
            try:
                self.networkManager.clients.remove(client)
            except:
                pass

            for battle in self.battles:
                if client == battle.client1 or client == battle.client2:
                    pass

        self.networkManager.connectionLock.release()

        while len(self.waitingQueue) >= 2:
            client1 = self.waitingQueue.popleft()
            client2 = self.waitingQueue.popleft()
            self.battles.append(Battle(client1, client2))
            content = ["BattleStart", client2.pokemans[0]]
            client1.sendPacket(content)
            content = ["BattleStart", client1.pokemans[0]]
            client2.sendPacket(content)
        for battle in self.battles:
            '''
            Battle will contain the GameState that will be updated
            '''
            if battle.over == True:
                if battle.client1.lose==True:
                    client = battle.client1
                    winner = battle.client2
                else:
                    client = battle.client2
                    winner = battle.client1
                client.draft = [] # clear draft
                client.pokemans =[] #clears pokeman
                for i in range(3):#new draft
                    r=random.randint(0,4)#random class
                    g=random.randint(0,1)#random gender
                    client.draft.append(pokeman(r,g))
                content = ["Draft", client.draft]
                client.sendPacket(content)
                self.waitingQueue.append(winner)
                self.battles.remove(battle)
            battle.update()
