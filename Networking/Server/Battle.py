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
            gameState = ['asdf']
            content = ["Battle", gameState]
            self.client1.sendPacket(content)
            self.client2.sendPacket(content)
