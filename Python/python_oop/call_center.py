class Call(object):
	def __init__(self,unique_id,name,p_number,time_of_call,reason):
		self.unique_id = unique_id
		self.name = name
		self.p_number = p_number
		self.time_of_call = time_of_call
		self.reason = reason

	def display_attr(self):
		print self.unique_id, self.name, self.p_number, self.time_of_call, self.reason
		return self

class Call_center(object):
	def __init__(self,calls):
		self.calls = []

	def add_call(self,call):
		self.calls.append(call)
		return self

	def remove_call(self):
		self.calls.pop(0)
		return self

	def call_info(self):
		for items in self.calls:
			for key,value in vars(items):
				print "{}: {}".format(key, value)
		return self






call_one = Call(1,"GB","847-555-5555","6:00pm","Pizza")
call_two = Call(2,"HB","847-555-5555","7:00pm","More Pizza")

call_cent = Call_center("Test")
call_cent.add_call(call_one).remove_call().add_call(call_two).call_info()



