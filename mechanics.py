'''
Created on Mar 22, 2015

@author: Alex
'''
moves = []
class move(object):
    def __init__(self,line):
        self.parse(line)
    def parse(self,line):
        