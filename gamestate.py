import mechanics
class gamestate():
	def __init__(self, player1, player2):
		self.playerOne = player1.pokemans
		self.playerTwo = player2.pokemans
		self.pokeOne = self.playerOne[0]
		self.pokeTwo = self.playerTwo[0]
		self.buffsOne[0,0,0,0,0]
		self.buffsTwo[0,0,0,0,0]
	def update(self, commandOne, indexOne, commandTwo, indexTwo):
		if commandOne == 0 or commandTwo == 0: 
			if commandOne == 0: #swap1
				self.pokeOne = self.playerOne[indexOne]
			if commandTwo == 0: #swap2
				self.pokeTwo = self.playerTwo[indexTwo]
		if commandOne == 1 and commandTwo == 1:
			if self.pokeOne.stats[4] >= self.pokeTwo.stats[4]:
				#issue command 1
				self.command(1,self.pokeOne.moves[indexOne])
				#issue command 2
				self.command(2,self.pokeTwo.moves[indexTwo])
			else:
				# command 2
				self.command(2,self.pokeTwo.moves[indexTwo])
				# command 1
				self.command(1,self.pokeOne.moves[indexOne])
		elif commandOne == 1:
			# command 1
			self.command(1,self.pokeOne.moves[indexOne])
		elif commandTwo == 1:
			# command 2
			self.command(2,self.pokeTwo.moves[indexTwo])
	def command(self,player,ability):
		if(ability.buff==True):
			if(ability.buffstat!=5):
				if(player==1):
					self.buffsOne[ability.buffstat]+=10
				else:
					self.buffsTwo[ability.buffstat]+=10
			else:
				if(player == 1):
					if(self.pokeOne.current<self.pokeOne.stats[5]-20):
						self.pokeOne.current+=20
				else:
					if(self.pokeTwo.current<self.pokeTwo.stats[5]-20):
						self.pokeTwo.current+=20
		else:
			if(player == 1):
				self.pokeTwo.curent-=self.damage(self.pokeOne,self.pokeTwo,ability)
				if self.pokeTwo.current<0:
					self.pokeTwo.current=0
					#ded
			else:
				self.pokeOne.curent-=self.damage(self.pokeTwo,self.pokeOne,ability)
				if self.pokeOne.current<0:
					self.pokeOne.current=0
					#ded

	def damage(self,attker,defender,ability):
		if(attker.type==ability.classN):
			stab=1.5
		else:
			stab=1
		if(ability.type==0):
			return ability.power*attker.stats[0]/defender.stats[1]*stab*mechanics.effective(defender.type,ability.classN)
		else:
			return ability.power*attker.stats[2]/defender.stats[3]*stab*mechanics.effective(defender.type,ability.classN)

		