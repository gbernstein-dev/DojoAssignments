class Car(object):
	def __init__(self,price,speed,fuel,mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage

		if price >= 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12

	def display_all(self):
		print "The price is {}. This car has a max speed of {} mph. Has a {} fuel tank. Tax is {}.".format(self.price,self.fuel,self.mileage,self.tax)


car1 = Car(12000,"40mph","Full","15mpg")
print car1.tax
car1.display_all()

