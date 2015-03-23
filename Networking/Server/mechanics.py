'''
Created on Mar 22, 2015

@author: Alex
'''
moves = []


class move():
    def __init__(self,line):
        self.buff = False
        moveline = line.split(',')
        if moveline[0] == 'rapper':
            self.type = 0
        elif moveline[0] == 'nerd':
            self.type = 1
        elif moveline[0] == 'child':
            self.type = 2
        elif moveline[0] == 'gangster':
            self.type = 3
        elif moveline[0] == 'hobo':
            self.type = 4
        self.moveName = moveline[1]
        if moveline[2] != 'buff':
            if moveline[2] == 'very low':
                self.power = 0
            elif moveline[2] == 'low':
                self.power = 1
            elif moveline[2] == 'med':
                self.power = 2
            elif moveline[2] == 'high':
                self.power = 3
            elif moveline[2] == 'very high':
                self.power = 4
            elif moveline[2] == 'vv high':
                self.power = 5
            self.hitchance = int(moveline[3])
            if moveline[4] == 'ph':
                self.atk = 0
            if moveline[4] == 'sp':
                self.atk = 1
        else:
            self.buff = True
            if moveline[4] == 'atk':
                self.buffstat = 0
            elif moveline[4] == 'def':
                self.buffstat = 1
            elif moveline[4] == 'satk':
                self.buffstat = 2
            elif moveline[4] == 'sdef':
                self.buffstat = 3
            elif moveline[4] == 'spd':
                self.buffstat = 4
            elif moveline[4] == 'hp':
                self.buffstat = 5

def effectiveness (move, pokeman):
    if move.type == 0:
        if pokeman.type == 0 or pokeman.type == 1: return 2
        else: return 1
    if move.type == 1:
        if pokeman.type == 0: return 2
        if pokeman.type == 1: return 0.5
        else: return 1
    if move.type == 2:
        if pokeman.type == 0 or pokeman.type == 3: return 2
        if pokeman.type == 2: return 0.5
        else: return 1
    if move.type == 3:
        if pokeman.type == 4 or pokeman.type == 1: return 2
        else: return 1
    if move.type == 4:
        if pokeman.type == 2: return 2
        else: return 1
        
            
        
with open("moves.txt", "r") as ifile:
    for line in ifile:
        moves.append(move(line))
        