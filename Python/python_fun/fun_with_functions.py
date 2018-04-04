def odd_even():
	for number in range(1,2001):
		if number % 2 == 0:
			print "Number is {}. This is an even number.".format(number)
		else:
			print "Number is {}. This is an odd number".format(number)
odd_even()