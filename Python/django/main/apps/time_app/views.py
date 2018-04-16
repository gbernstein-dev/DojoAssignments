from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# the index function is called when root is visited
def index(request):
	context = {
	'day': strftime("%b %d, %Y", gmtime()),
	'time': strftime("%H:%M %p", gmtime())
	}
	return render(request, 'index.html', context)
