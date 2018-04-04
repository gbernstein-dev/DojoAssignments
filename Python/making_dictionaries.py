def make_dict(list1, list2):
  new_dict = {}
  # your code here
  for items in range(len(list1)):
  		new_dict[list1[items]] = list2[items]
  print new_dict
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
make_dict(name,favorite_animal)

