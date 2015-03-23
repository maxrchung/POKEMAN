'''
Created on Mar 22, 2015

@author: Alex
'''
import random
from pokeman import pokeman
class generator(object):

    def __init__(self, params):
        '''
        Constructor
        '''
        self.pokemans=[]
        self.selector()
    def selected(self,num):
        self.pokemans.append(self.choices[num])
        if(len(self.pokemans)==3):
            return
        self.selector()
    def selector(self): 
        self.draft = []
        for i in range(2):
            r=random.randint(4)
            g=random.randint(1)
            self.draft.append(pokeman(r,g))
            
            