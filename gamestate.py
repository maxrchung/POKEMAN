class gamestate():
	def __init__(self, player1, player2):
		self.playerOne = player1.pokemans
		self.playerTwo = player2.pokemans
		self.pokeOne = self.playerOne[0]
		self.pokeTwo = self.playerTwo[0]
	def update(self, commandOne, indexOne, commandTwo, indexTwo):
		if commandOne == 0 or commandTwo == 0: 
			if commandOne == 0: #swap1
				self.pokeOne = self.playerOne[indexOne]
			if commandTwo == 0: #swap2
				self.pokeTwo = self.playerTwo[indexTwo]
		if commandOne == 1 and commandTwo == 1:
			if self.pokeOne.stats[4] >= self.pokeTwo.stats[4]:
				#issue command 1
				#issue command 2
			else:
				# command 2
				# command 1
		elif commandOne == 1:
			# command 1
		elif commandTwo == 1:
			# command 2