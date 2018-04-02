def find_and_replace(sentence, word):
  word_index = sentence.find(word)
  new_sentence = sentence.replace(word, "month")
  print word_index, new_sentence
find_and_replace("It's thanksgiving day. It's my birthday, too!", "day")

def min_max(arr):
  maximum = max(arr)
  minimum = min(arr)
  print "the maximum is {} and the minimum is {}".format(maximum,minimum)
min_max([50,40,70,75,15])

def first_last(arr):
  new_arr = [arr[0],arr[-1]]
  print new_arr
first_last([1,3,2,"sandwich"])

def new_list(arr):
  sorted_arr = sorted(arr)
  half_one = sorted_arr[0:int((len(arr)/2))]
  half_two = sorted_arr[int((len(arr)/2)):-1]
  half_two.insert(0,half_one)
  print half_two
new_list([19,2,54,-2,7,12,98,32,10,-3,6])



