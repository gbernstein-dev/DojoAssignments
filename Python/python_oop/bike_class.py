class Bike(object):
	def __init__(self,price,max_speed,miles):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def display_info(self):
		print "The price is {}. This car has a max speed of {} mph. Currently has: {} miles.".format(self.price,self.max_speed,self.miles)

	def ride(self):
		self.miles += 10
		print "Drove 10 miles."

	def reverse(self):
		if self.miles > 5:
			self.miles -= 5
			print "Going back in time..."
		else:
			print "Could not reverse time."


bike1 = Bike("$1000",100,30000)
bike1.display_info()
bike1.ride()
print bike1.miles
bike1.reverse()
print bike1.miles
bike1.reverse()
print bike1.miles