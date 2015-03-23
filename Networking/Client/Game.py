from NetworkManager import *

class Game:
    def __init__(self):
        self.running = True
        self.state = "Login"
        self.networkManager = NetworkManager(self)
        self.draft = [] # The pokemans in the draft
        self.pokemans = [] # The pokemans selected
        self.gameState = [] # gameState in battle

        '''
        Initialize the GameLogic that'll handle the different parts
        Will probably want to pass in self so that it can reference the overall game's variables

        clientLogic = new clientLogic(self)
        '''

    def run(self):
        self.update()
        self.draw()

    def update(self):
        # Handles processing of messages
        self.networkManager.messageLock.acquire()
        while len(self.networkManager.messageQueue) > 0:
            data = self.networkManager.messageQueue.popleft()
            print("Received:", data)
            command = data[0]

            # The server drafts 3 cards for the client
            # Process these into the drafting phase
            if command == "Draft" and self.state == "Draft":
                '''
                Put into some draft data structure
                '''
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
                pass

                
        self.networkManager.messageLock.release()
            
        if self.state == "Login":
            '''
            Need to put the TextInput in here to enter the name
            For now, I have an input to temporarily take the place of it

            TextInput.run()
            onEnter... sendPacket
            '''
            # Temporary placeholder
            name = input("Enter a name: ")
            content = ["Login", name]
            self.networkManager.sendPacket(content)
            self.state = "Draft" # Switch to draft state after
            print()
            print("Switched to Draft")
            
        elif self.state == "Draft":
            '''
            Choose a pokemon out of the 3 choices
            ...
            index = some_selection
            self.pokemans.append(draft[index])
            onSelection... sendPacket
            '''
            # Temporary placeholder
            if len(self.draft) > 0:
                print("self.draft:", self.draft)
                index = input("Choose a pokeman: ")
                self.pokemans.append(self.draft[int(index)])
                content = ["Draft", index]
                self.networkManager.sendPacket(content)

                self.draft = [] # Reset the draft

                # If we have drafted 3 pokemon, then jump to queue mode
                if len(self.pokemans) >= 3:
                    print(self.pokemans)
                    self.state = "Queue"
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
        '''
        Handle all the drawing here

        if self.state == "Login":
        ...
        elif self.state == "Draft":
        ...
        etc.

        '''
        pass
        
