#garret konrad maurice
def print_to_255():
  for num in range(1,256):
    print num
print_to_255()

def odds():
  for num in range(1,256):
    if num % 2 != 0:
      print num
odds()

def print_ints_and_sum():
  total = 0
  for num in range(0,256):
    total += num
  print total
print_ints_and_sum()

def array_values(arr):
  for item in arr:
    print item
a = [1,2,3]
array_values(a)

def print_max(arr):
  maximum = arr[0]
  for item in arr:
    if item > maximum:
      maximum = item
  print maximum
a = [5,6,10]
print_max(a)

def average(arr):
  total = 0.0
  for num in arr:
    total += num
  print total/(len(arr))
a = [1,2,3,10,11]
average(a)

def odd_array():
  arr1 = []
  for num in range(1,256):
    if num % 2 != 0:
      arr1.append(num)
  print arr1
odd_array()

def sq_arrvals(arr):
  for item in range(len(arr)):
    arr[item] = arr[item]**2
  return arr
a = [5,10,15]
print sq_arrvals(a)

def greater(arr, y):
  arr1 = []
  for num in arr:
    if num > y:
      arr1.append(num)
  print arr1
a = [1,2,3,4,5]
b = 3
greater(a,b)

def zero_out(arr):
  for num in range(len(arr)):
    if arr[num] < 0:
      arr[num] = 0
  print arr 
zero_out([-1,5,10])

def min_max_avg(arr):
  total = 0.0
  maximum = arr[0]
  minimum = arr[0]
  for item in arr:
    if item > maximum:
      maximum = item
  for item in arr:
    if item < minimum:
      minimum = item
  for num in arr:
    total += num
  print total/(len(arr)),minimum,maximum
min_max_avg([1,5,10])

def shift_left(arr):
  for num in range(len(arr)):
    if num > 0:
      arr[num-1] = arr[num]
  arr[-1] = 0
  print arr
shift_left([1,2,3])

def swap_string(arr):

  for num in range(len(arr)):
    if arr[num] < 0:
      arr[num] = 'Dojo'
  print arr
swap_string([-1,5,10])


# arr1 = [1,2,3]
# for num in range(len(arr1)):
#   print arr1[num]




