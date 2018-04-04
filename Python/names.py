
def name_output(a):
	for job,people in a.items():
		print job
		for names in range(len(people)):
			str_len = len(people[names]["first_name"])+len(people[names]["last_name"])
			print "{} - {} {} - {}".format(names+1,people[names]["first_name"],people[names]["last_name"],str_len)
		
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

name_output(users)
