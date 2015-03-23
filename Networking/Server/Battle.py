import pygame

class Battle:
    def __init__(self, client1, client2):
        self.client1 = client1
        self.client2 = client2
        
        # So we don't send too many game updates at once
        # Only sends a game update after a certain updateTimer limit has passed
        self.updateClock = pygame.time.Clock()
        self.updateTimer = 0

        # self.gameState = GameState()

    def update(self):
        # Update gameState here
        # self.gameState.update()
        self.updateTimer += self.updateClock.tick()
        if self.updateTimer > 50:
            self.updateTimer = 0
            # After the battles are updated, send the gamestate out if
            # one person did not win/lose
            pState1 = [self.client1.pokemans,self.client1.active,self.client2.pokemans[self.client2.active]]
            pState2 = [self.client2.pokemans,self.client2.active,self.client1.pokemans[self.client1.active]]
            content1 = ["Battle", pState1]
            content2 = ["Battle", pState2]
            self.client1.sendPacket(content1)
            self.client2.sendPacket(content2)