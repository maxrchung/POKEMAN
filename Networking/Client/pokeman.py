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
    nameList = ['JALAPENO','MCCHUCK','FLUSHWORTHY','MAMARINO','SUDOKU','MANE','LUCCA','GUCCI','1337','DILDOE',
                'MAX WAX CHUG DA GWAD CHUNG','MAX','WAX','CHUG','DA','GWAD','CHUNG','DURA KNIGHT','MAXIMILLION',
                'PEGASUS','PIKACHUNG','DANGER','TRIAD','DOLAN','GOOBY','TOMOTHY','D00K','FIGSWORTH','KIPPA',
                'NEDWORTH','WINSTON','OBAMA','VINCE','JETT','CHEETO','GINGER','69ER','GREEN MACHINE','JUICE',
                'CORN SYRUP','BOBBOTHY','DEREKT','BIBLETHUMP','FRANKERZ','KEEPO','KREYGASM','RALPHERZ','KILLA',
                'OGNA','TESMA','CHIP','MCGEE','GLOCK','SOY','NUTS','BUTTERS','SHAMWOW','GRELLY','MOIST','VIN',
                'PJSALT','FRAPPA','KAPPY','PASTA','CHANP','GUST','SCRUB','SCRUBLET','FRACTO','TIMZER','CENA','DWAG',
                'KAUFMANN','H','BACH','KINGERY','BOWEN','DOWNS','AVERY','JORGE','HAMILTON','NIMMO','BUTCHER','ROWWING',
                'SWAPT','DARUDE','DRYUS','HOTPOTGG','SPHINCTER','THROB','PLATOLET','MACCACHROONI','BIERSCH',
                'WONKTER','DOOSBY','HYU','DOGER','GIET','BLUEBY','TEMPNAME','KIRKLE','BLOPY','???','KINGU',
                'HALP','BOOTHSE','KOKMAW','PYTH','HONT','FLAOW','JONK','BRO','MANG','KARLVE','DOSKEY','RICHARD',
                'POPSTER','WONN','SWAGSON','CH0L0','GOG','H4CKER','DOMEN','GENRAY','CANCER, THE WORST KIND',
                'DAYTUCKER','NIGHTHUKKR','T00MIR','DIBSTA','BLOBOI','BLEHKSTA','YUUSUUPU','KOUME','CYL','CHARKLEY',
                'JLAM SAM','BARKLES','DOGESWORTH','SWOOGITYLORD','MUH','PACE KAM','ACE NAM','GASE WAM','CHASE PAM']
    statBase =[40,50,60,70,80,85]
    def __init__(self, type,gender):
        '''
        Constructor
        '''
        self.type = type
        self.gender = gender
        self.moveset=[]
        self.stats=[]
        self.typeName = ''
        self.setmoves()
        self.setStats()
        self.setname()
    
    def __str__(self):
        return self.name
        
    def setname(self):
        self.name = self.nameList[random.randint(0,len(self.nameList)-1)]
    
    def setmoves(self):
        a=random.randint(0,3)
        b=random.randint(0,3)
        while(a==b):
            b=random.randint(0,3)
        self.moveset.append(moves[self.type*4+a])
        self.moveset.append(moves[self.type*4+b])
        a=random.randint(0,19)
        while(int(a/4)==self.type):
            a=random.randint(0,19) 
        b=random.randint(0,19)
        while(a==b or int(b/4)==self.type):
            b=random.randint(0,19)
        self.moveset.append(moves[a])
        self.moveset.append(moves[b])
        
    def setStats(self):
        statBase = pokeman.statBase
        if self.type == 0:
            self.typeName = 'RAPPER'
            a=random.randint(0,15)
            self.stats.append(statBase[3]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[2]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[4]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[1]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[0]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[2]+a)
        if self.type == 1:
            self.typeName = 'DELINQUENT'
            a=random.randint(0,15)
            self.stats.append(statBase[0]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[1]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[3]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[3]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[4]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[1]+a)
        if self.type == 2:
            self.typeName = 'NERD'
            a=random.randint(0,15)
            self.stats.append(statBase[2]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[0]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[5]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[2]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[1]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[2]+a)
        if self.type == 3:
            self.typeName = 'GANGSTER'
            a=random.randint(0,15)
            self.stats.append(statBase[5]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[1]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[1]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[1]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[3]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[3]+a)
        if self.type == 4:
            self.typeName = 'HOBO'
            a=random.randint(0,15)
            self.stats.append(statBase[3]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[1]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[4]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[1]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[3]+a)
            a=random.randint(0,15)
            self.stats.append(statBase[1]+a)
        self.current=0+self.stats[5]
                
print(len(pokeman.nameList))