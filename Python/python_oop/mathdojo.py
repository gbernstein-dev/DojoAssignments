class MathDojo(object):
	def __init__(self,total=0):
		self.total = total

	def add(self, *items):
		for i in items:
			if type(i) is list:
				ls_total = 0
				for j in i:
					ls_total += j
				self.total += ls_total
			else:
				self.total = self.total + i
		return self

	def subtract(self, *items):
		mini_total = 0
		for i in items:
			if type(i) is list:
				for j in i:
					mini_total = mini_total + j
			else:
				mini_total = mini_total + i
		self.total -= mini_total
		return self

	def result(self):
		print self.total

md = MathDojo()
md.add([2,2],2).subtract([1,2,3],4).result()


