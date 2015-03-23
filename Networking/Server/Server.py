from NetworkManager import *
from collections import deque

class Server:
    def __init__(self):
        self.running = True
        self.waitingQueue = deque()
        self.networkManager = NetworkManager(self)
        self.battles = []

    def run(self):
        self.update()

    def update(self):
        # Processes messages received on the server
        self.networkManager.connectionLock.acquire()
        for client in self.networkManager.clients:
            client.messageLock.acquire()
            while len(client.messageQueue) > 0:
                data = client.messageQueue.popleft()
                print("Received:", data)
                command = data[0]

                if command == "Login":
                    client.name = data[1]
                    '''
                    Generate 3 Pokemon to send to the client
                    For now, I'm just using placeholder ints 0, 1, and 2
                    client.draft = draftPokemans()
                    '''
                    client.draft = [0, 1, 2] # Temporary placeholder

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
                        '''
                        client.draft = draftPokemans()
                        '''
                        client.draft = [0, 1, 2] # Temporary placeholder

                        content = ["Draft", client.draft]
                        client.sendPacket(content)

                    # Else put the client into the queue
                    else:
                        client.draft = [] # Resets draft
                        self.waitingQueue.append(client)

            client.messageLock.release()
        self.networkManager.connectionLock.release()

        while len(self.waitingQueue) >= 2:
            client1 = self.waitingQueue.popleft()
            client2 = self.waitingQueue.popleft()
            self.battles.append(Battle(client1, client2))

        for battle in self.battles:
            '''
            Battle will contain the GameState that will be updated
            '''
            battle.update()

            # After the battles are updated, send the gamestate out if
            # one person did not win/lose
            gameState = []
            content = ["Battle", gameState]
            battle.client1.sendPacket(content)
            battle.client2.sendPacket(content)
