#check if even or odd
def odd_even():
	for number in range(1,2000):
		if number % 2 == 0:
			print "Number is {}. This is an even number.".format(number)
		else:
			print "Number is {}. This is an odd number".format(number)
odd_even()

#multiply each number in array by number
def multiplied(arr,num):
	new_arr = []
	for item in arr:
		new_item = item * num
		new_arr.append(new_item)
	return new_arr
testcase = multiplied([2,4,6,8,10],3)
print testcase

#utilize multiplied() to create an array containing smaller arrays
#with quantity of 1's equal to the integer at that index
def layered_multiples(arr):
	layered_arr = []
	for item in arr:
		item_arr = []
		for i in range(item):
			item_arr.append(1)
		layered_arr.append(item_arr)
  	return layered_arr
testcase2 = layered_multiples(multiplied([2,4,5],3))
print testcase2

