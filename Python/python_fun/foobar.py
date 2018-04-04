# Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.

# For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. 
# If it is a prime number, print "Foo". If it is a perfect square, print "Bar". 
# If it is neither, print "FooBar". Do not use the python math library for this exercise. 
# For example, if the number you are evaluating is 25, you will have to figure out if it is a perfect square. It is, so print "Bar".

def foobar():
	for number in range (100, 1000):
		prime = True
		for item in range(2, number):
			if number%item == 0:
				prime = False
		if prime == True:
			print number,"Foo"
		elif number**0.5 == int(number**0.5):
			print number, number**0.5, "Bar"
		elif prime == False and number**0.5 != int(number**0.5):
			print "Foobar"
foobar()
