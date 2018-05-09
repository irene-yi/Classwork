class Stack:
	def __init__(self):
		self.items = []

#pushing in information
	def push(self,items):
		self.items.append(items)
	def pop(self,items):
		a = []
		if self.items == a:
			print('ERROR.SHUTDOWN')
			return False
		else:
			self.items.pop(items)
	def isEmpty(self):
		a = []
		if self.items == a:
			print('true')
			return True
		else:
			print('false')
			return False

	def bubbles(self):
		n = len(self.items)
		for x in range(n):
			for y in range(0,n-x-1):
				if self.items[y] > self.items[y+1]:
					self.items[y],self.items[y+1] = self.items[y+1],self.items[y]
		print(self.items)


horse_stack = Stack()
horse_stack.push(120)
horse_stack.push(5000)
horse_stack.push(10)
horse_stack.bubbles()