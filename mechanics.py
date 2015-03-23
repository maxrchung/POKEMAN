'''
Created on Mar 22, 2015

@author: Alex
'''
moves = []
class move(object):
    def __init__(self,line):
        self.parse(line)
    def parse(self,line):
        self.buff = False
        movefile = open(line)
        moveline = movefile.readline().split(',')
        self.className = moveline[0]
        self.moveName = moveline[1]
        if moveline[2] != 'buff':
            self.power = moveline[2]
            self.hitchance = moveline[3]
            self.type = moveline[4]
        else:
            self.buff = True
            self.buffstat = moveline[4]
            
        
        