#odd numbers 1-1000
def odd():
  for number in range(1001):
    if number % 2 != 0:
      print number
odd()

#sum of all values
def sum_of_all(arr):
  total = 0
  for num in arr:
    total += num
  print total
sum_of_all([1, 2, 5, 10, 255, 3])

#average value of list
def average(arr):
  total = 0
  for num in arr:
    total += num
  print total/(len(arr))
average([1, 2, 5, 10, 255, 3])