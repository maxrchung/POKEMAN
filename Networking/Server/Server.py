from NetworkManager import *

class Server:
    def __init__(self):
        self.running = True
        self.networkManager = NetworkManager(self)

    def run(self):
        self.update()

    def update(self):
        self.networkManager.connectionLock.acquire()
        for client in self.networkManager.clients:
            client.messageLock.acquire()
            while len(client.messageQueue) > 0:
                data = client.messageQueue.popleft()
                command = data[0]

                if command == 'Login':
                    client.name = data[1]
                    print(client.name)
                    
            client.messageLock.release()
        
        self.networkManager.connectionLock.release()
