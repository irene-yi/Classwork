class Player (object):
	def ___int___ (self, name, type, hp):
		self.name = name
		self.hp = hp

		if type == 'water':
			{
				'Blood Bending': random.randint(30,80),
				'Water Octopus': random.randint(10,20),
				'Heal': random.randint (-20,-30)
			}
		elif type == 'fire':
			{
				'Fire Ball': random.randint(20,40),
				'Thunderbolt': random.randint(40,60)
			}
		else
			print ('Not a choice')

		for moves in self.type:
			print(moves)

	def battle
		for x in self.type:
			print (x)

			print ('Player turn to attack' (self.name, enemy.name))

			user_choice = input('God has given you the ability to choose an attack. Choose wisely?')

			chosen_attack = self.type[user_choice]

			if (self.hp > 1)
				enemy.hp = enemy.hp - chosen_attack
				print ('%s did %d damage to %s' (self.name, chosen_attack, enemy.name))
				print ('%s HP left' %(enemy.name, enemy.hp))
				if (enemy.hp > 1):
					retrn enemy.battle(self)
			else
				print('%s is knoked out, %s won'%(enemy.name, self.name))
			
#ABSTRACTED FORM
Katara = Player('Katara', 'water', 100)
Zuko = Player('Zuko', 'fire', 100)
Player.battle(Katara, Zuko)