def draw_stars(arr):
	for item in arr:
		row = ""
		if item == str(item):
			for i in range(len(item)):
				row+=item[0]
		else:
			for i in range(item):
				row+="*"	
		print row
draw_stars([1,2,3,"hello","world",7])