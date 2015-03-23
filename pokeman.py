'''
Created on Mar 22, 2015

@author: Alex
'''
from mechanics import moves
import random
class pokeman(object):
    '''
    classdocs

    Vvhigh: 85
    Vhigh:80
    High:70
    Med:60
    Low:50
    Vlow:40
    '''
    statBase =[40,50,60,70,80,85]
    def __init__(self, type,gender):
        '''
        Constructor
        '''
        self.type = type
        self.gender = gender
        self.setmoves()
        self.moves=[]
        self.stats=[]
    def setmoves(self):
        a=random.randint(0,3)
        b=random.randint(0,3)
        while(a==b):
            b=random.randint(0,3)
        self.moves.append(moves[self.type*4+a])
        self.moves.append(moves[self.type*4+b])
        a=random.randint(0,19)
        while(a/4==self.type):
            a=random.randint(0,19) 
        b=random.randint(0,19)
        while(a==b and b/4==self.type):
            b=random.randint(0,19)
        self.moves.append(moves[a])
        self.moves.append(moves[b])
        
    def setStats(self):
        global statBase
        if self.type == 0:
            a=random.randint(15)
            self.stats.append(statBase[3]+a)
            self.stats.append(statBase[2]+a)
            self.stats.append(statBase[4]+a)
            self.stats.append(statBase[1]+a)
            self.stats.append(statBase[0]+a)
            self.stats.append(statBase[2]+a)
        if self.type == 1:
            a=random.randint(15)
            self.stats.append(statBase[0]+a)
            self.stats.append(statBase[1]+a)
            self.stats.append(statBase[3]+a)
            self.stats.append(statBase[3]+a)
            self.stats.append(statBase[4]+a)
            self.stats.append(statBase[1]+a)
        if self.type == 2:
            a=random.randint(15)
            self.stats.append(statBase[2]+a)
            self.stats.append(statBase[0]+a)
            self.stats.append(statBase[5]+a)
            self.stats.append(statBase[2]+a)
            self.stats.append(statBase[1]+a)
            self.stats.append(statBase[2]+a)
        if self.type == 3:
            a=random.randint(15)
            self.stats.append(statBase[5]+a)
            self.stats.append(statBase[1]+a)
            self.stats.append(statBase[1]+a)
            self.stats.append(statBase[1]+a)
            self.stats.append(statBase[3]+a)
            self.stats.append(statBase[3]+a)
        if self.type == 4:
            a=random.randint(15)
            self.stats.append(statBase[3]+a)
            self.stats.append(statBase[1]+a)
            self.stats.append(statBase[4]+a)
            self.stats.append(statBase[1]+a)
            self.stats.append(statBase[3]+a)
            self.stats.append(statBase[1]+a)
            