from Game import *


game = Game()


while game.login != 3:
    game.prelogin()


game.start()
while game.running:
    game.run()
    
    
    
