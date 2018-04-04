def cointoss():
	import random
	heads = 0
	tails = 0
	for toss in range(5000):
		result = random.randint(1,2)
		if result == 1:
			heads += 1
		else:
			tails += 1
	print "there were {} heads and {} tails.".format(heads, tails)
cointoss() 