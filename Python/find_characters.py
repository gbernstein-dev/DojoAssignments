def find_var(arr,var):
  results = []
  for item in arr:
    for letter in item:
      if letter == var:
        results.append(item)
  print results
find_var(["hello","world","super"],"o")