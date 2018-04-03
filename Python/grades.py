def grades():
	import random
	for student in range(11):
		grade = ""
		score = random.randint(60,100)
		if score > 90:
			grade = "A"
		elif 80 < score < 90:
			grade = "B"
		elif 70 < score < 80:
			grade = "C"
		elif 60 < score < 70:
			grade = "D"
		else:
			grade = "F"
		print "Score: {}; Your grade is {}.".format(score,grade) 
grades()