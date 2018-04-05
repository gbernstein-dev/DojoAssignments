class Product(object):
	def __init__(self,price,item_name,weight,brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = "For Sale"

	def sell(self):
		self.status = "Sold"
		return self

	def add_tax(self):
		self.price = (self.price * 0.15) + self.price
		return self
	
	def return_item(self,reason):
		if reason == "Defective":
			self.status = "Defective"
			self.price = 0
		elif reason == "Unopened":
			self.status = "For Sale"
		elif reason == "Opened":
			self.status = "Used"
			self.price = self.price - (self.price*0.2)
		return self 

	def display_info(self):
		print "Price: ${}. Item Name: {}. Weight: {}. Brand: {}. Status: {}.".format(self.price,self.item_name,self.weight,self.brand,self.status)
		return self
		

apple = Product(1,"Apple","0.3lbs","Red Delicious")
apple.display_info().sell().add_tax().display_info().return_item("Opened").display_info()