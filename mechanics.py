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
            self.classN = 0
        elif moveline[0] == 'nerd':
            self.classN = 1
        elif moveline[0] == 'child':
            self.classN = 2
        elif moveline[0] == 'gangster':
            self.classN = 3
        elif moveline[0] == 'hobo':
            self.classN = 4
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
            self.type = moveline[4]
        else:
            self.buff = True
            self.buffstat = moveline[4]
            
        
with open("moves.txt", "r") as ifile:
    for line in ifile:
        moves.append(move(line))
        