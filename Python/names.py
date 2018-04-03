
def name_output(dict):
	str_len = 0
	student_num = 1
	instuctor_num = 1
	for student in dict['Students']:
		str_len = len(student['first_name'])+len(student['last_name'])
		print '{} - {} {} - {}'.format(student_num,student['first_name'],student['last_name'],str_len)
		student_num += 1
	for instuctor in dict['Instructors']:
		str_len = len(instuctor['first_name'])+len(instuctor['last_name'])
		print '{} - {} {} - {}'.format(instuctor_num,instuctor['first_name'],instuctor['last_name'],str_len)
		instuctor_num += 1
		
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
testcase = name_output(users)
print testcase

