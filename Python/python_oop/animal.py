class Animal(object):
	def __init__(self,name,health):
		self.name = name
		self.health = health

	def walk(self):
		self.health = self.health - 1
		return self

	def run(self):
		self.health = self.health - 5
		return self

	def display_health(self):
		print self.health
		return self

class Dog(Animal):
	def __init__(self,name,health=150):
		# Animal.__init__(self)
		super(Dog, self).__init__(name,health)

	def pet(self):
		self.health = self.health + 5
		return self

class Dragon(Animal):
	def __init__(self,name,health=170):
		super(Dragon, self).__init__(name,health)

	def fly(self):
		self.health = self.health - 10
		return self

	def dragon_health(self):
		Dragon.display_health(self)
		print "I am a dragon"
		return self

# animal_test = Animal("Giraffe",10)
# animal_test.display_health().walk().run().display_health()
# dog = Dog("fido")
# dog.walk().walk().walk().run().run().pet().display_health()
# dragon = Dragon("sindragosa")
# dragon.dragon_health()
