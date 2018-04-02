def checkerboard():
  count = 0
  for item in range(6):
    count+=1
    if count % 2 != 0:
      print "* * * * *"
    else:
      print " * * * * * "
checkerboard()

