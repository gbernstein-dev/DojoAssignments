def tuple_maker(contact_info):
	contact_list = []
	contact_tuple = ()
	for name,number in contact_info.items():
		contact_tuple = contact_tuple + (name,number)
	contact_list.append(contact_tuple)
	print contact_list
# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
tuple_maker(my_dict)
