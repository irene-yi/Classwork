class Player(object):
	def ___int___ (self, name, hp, type):
		self.name = name
		self.hp = hp

		if type == 'water':
			self.type = {
				'Blood Bending': random.randint(30,80),
				'Water Octopus': random.randint(10,20),
				'Heal': random.randint (-30,-20)
			}
		elif type == 'fire':
			self.type = {
				'Fire Ball': random.randint(20,40),
				'Thunderbolt': random.randint(40,60)
			}
		else:
			print ('Not a choice')

	#	for moves in self.type:
	#		print(moves)

	def battle(self, enemy):
		for x in self.type:
			print (x)

			print ('Player turn to attack' (self.name, enemy.name))

			user_choice = input('God has given you the ability to choose an attack. Choose wisely?')

			chosen_attack = self.type[user_choice]

			if (self.hp > 1):
				enemy.hp = enemy.hp - chosen_attack
				print ('%s did %d damage to %s' (self.name, chosen_attack, enemy.name))
				print ('%s HP left' %(enemy.name, enemy.hp))
				if (enemy.hp > 1):
					return enemy.battle(self)
			else:
				print('%s is knoked out, %s won'%(enemy.name, self.name))
			
#ABSTRACTED FORM
katara = Player('Katara', 100, 'water')
zuko = Player('Zuko', 100, 'fire')
Player.battle(katara, zuko)