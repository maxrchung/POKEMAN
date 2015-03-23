class Server:
    def __init__(self):
        self.running = True
        self.networkManager = NetworkManager(self)

    def run(self):
        self.update()

    def update(self):
        self.networkManager.connectionLock.acquire()
        for client in networkManager.clients:
            self.client.messageLock.acquire()
            while len(client.messageQueue) > 0:
                data = client.messageQueue.popleft()
                command = data[0]

                if command == 'Login':
                    client.name = data[2]
                
                
                    
                
            self.client.messageLock.release()
        
        self.networkManager.connectionLock.release()
