'''
Created on Mar 22, 2015

@author: Alex
'''
import mechanics
from _random import Random
from random import randint
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
        a=Random.randint(0,3)
        b=Random.randint(0,3)
        while(a==b):
            b=Random.randint(0,3)
        self.moves.append(mechanics.moves[self.type*4+a])
        self.moves.append(mechanics.moves[self.type*4+b])
        a=Random.randint(0,19)
        while(a/4==type):
            a=Random.randint(0,19) 
        b=Random.randint(0,19)
        while(a==b and b/4==type):
            b=Random.randint(0,19)
        self.moves.append(mechanics.moves[a])
        self.moves.append(mechanics.moves[b])
        
    def setStats(self):
        global statBase
        if type == 0:
            a=Random.randint(15)
            self.stats.append(statBase[3]+a)
            self.stats.append(statBase[2]+a)
            self.stats.append(statBase[4]+a)
            self.stats.append(statBase[1]+a)
            self.stats.append(statBase[0]+a)
            self.stats.append(statBase[2]+a)
        if type == 1:
            a=Random.randint(15)
            self.stats.append(statBase[0]+a)
            self.stats.append(statBase[1]+a)
            self.stats.append(statBase[3]+a)
            self.stats.append(statBase[3]+a)
            self.stats.append(statBase[4]+a)
            self.stats.append(statBase[1]+a)
        if type == 2:
            a=Random.randint(15)
            self.stats.append(statBase[2]+a)
            self.stats.append(statBase[0]+a)
            self.stats.append(statBase[5]+a)
            self.stats.append(statBase[2]+a)
            self.stats.append(statBase[1]+a)
            self.stats.append(statBase[2]+a)
        if type == 3:
            a=Random.randint(15)
            self.stats.append(statBase[5]+a)
            self.stats.append(statBase[1]+a)
            self.stats.append(statBase[1]+a)
            self.stats.append(statBase[1]+a)
            self.stats.append(statBase[3]+a)
            self.stats.append(statBase[3]+a)
        if type == 4:
            a=Random.randint(15)
            self.stats.append(statBase[3]+a)
            self.stats.append(statBase[1]+a)
            self.stats.append(statBase[4]+a)
            self.stats.append(statBase[1]+a)
            self.stats.append(statBase[3]+a)
            self.stats.append(statBase[1]+a)
            