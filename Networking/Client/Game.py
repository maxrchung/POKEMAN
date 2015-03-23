from NetworkManager import *

class Game:
    def __init__(self):
        self.running = True
        self.state = "Login"
        self.networkManager = NetworkManager(self)

    def run(self):
        self.update()
        self.draw()

    def update(self):
        if self.state == "Login":
            name = input("Enter a name: ")
            content = ["Login", name]
            self.networkManager.sendPacket(content)
            
        pass

    def draw(self):
        pass
        
