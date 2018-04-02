#prints sum of all numbers in arr, prints concatenated version of strings in arr, prints both if mixed
def list_type(arr):
  arr_str = []
  str_count = 0
  arr_int = []
  int_count = 0
  int_total = 0
  for item in arr:
    if type(item) is str:
      arr_str.append(item)
      str_count += 1
    else:
      arr_int.append(item)
      int_count +=1
      int_total += item
  if str_count == 0:
    print "all number array: {}. the total of these numbers is {}".format(arr_int, int_total)

  elif int_count == 0:
    string_join = " ".join(arr_str)
    print "all string array: {}. all these strings together is {}.".format(arr_str,string_join)
  else:
    print "mixed array. the strings are {}, and the integers are {}. the total of the numbers in this array is {}.".format(arr_str,arr_int,int_total)
list_type(["a",2,"c","attack helicopter",999])
list_type([1,2,3,4])
list_type(["a","b","c"])
