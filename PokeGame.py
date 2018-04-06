class Player (object):
	def ___int___ (self, name, type, hp)
		self.name = name
		self.hp = hp

		if type == 'water'
			{
				'Blood Bending': random.randint(30,80),
				'Water Octopus': random.randint(10,20),
				'Heal': random.randint (20,30)
			}
		elif type == 'fire'
			{
				'Fire Ball': random.randint(20,40),
				'Thunderbolt': random.randint(40,60)
			}

		for moves in self.type:
			print(moves)

	def battle
		for x in self.type:
			print(x)
#ABSTRACTED FORM
Katara = Player('Katara', 'water', 100)
Zuko = Player('Zuko', 'fire', 100)
Player.battle(Katara, Zuko)