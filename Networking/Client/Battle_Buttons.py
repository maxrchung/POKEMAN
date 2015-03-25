import pygame

class Battle_Buttons:

    #Buttons for Battle 
    def __init__(self):
        self.keys = [False, False, False, False, False, False]
        self.menuButtons = ['ATTK', 'SWAP', 'FLEE']
        self.pokeButtons = ['Poke 1', 'Poke 2','Poke 3']
        self.moveButtons = ['Move 1', 'Move 2', 'Move 3', 'Move 4']
        self.forfeitButtons = ['Yes','No']
        self.currentButton = 0 #used to determine what button you are on
        self.menustate = 0 #0: menu, 1: attack, 2: switch, 3: forfeit

                    
    #returns a string that represents the menu button
    def getMenu(self, i):
        return self.menuButtons[i]


    def getMove(self, i): return self.moveButtons[i]
    def getPoke(self, i): return self.pokeButtons[i]
    def getForfeit(self, i): return self.forfeitButtons[i]

    #returns the menu state
    def getMenustate(self): return self.menustate
    #returns the current button state 
    def getCurrentbutton(self): return self.currentButton


    #sets the current menu state
    def setMenustate(self, i): self.menustate = i
    #sets the current button state
    def setCurrentbutton(self, i): self.currentButton = i
