def dictionary(name, age, birth_country, language):
	citizen = {'Name':name,'Age':age,'birth_country':birth_country,'language':language}
	return "my name is {}. My age is {}. My country of birth is {}. My favorite language is {}.".format(citizen['Name'],citizen['Age'],citizen['birth_country'],citizen['language'])
testcase = dictionary("garret",25,"USA","Python")
print testcase

