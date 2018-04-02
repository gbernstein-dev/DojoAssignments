#numbers
def check(number):
  if number >= 100:
    print "that's a big number"
  else:
    print "that's a small number"
check(102)
check(40)

#strings
def check(sentence):
  if len(sentence) >= 50:
    print "long string"
  else:
    print "short string"
check("Donec quis mi sed elit posuere lobortis. Quisque lobortis odio semper nisi elementum, eget sollicitudin lorem tincidunt. Phasellus volutpat elit sit amet leo posuere venenatis. Curabitur vitae consectetur est.")
check("wow")

#lists
def check(arr):
  if len(arr) >= 10:
    print "that's a big list"
  else:
    print "that's a small list"
check([1,2,3,4,5,6,7,8,9,10,11])
check([1,2,3])