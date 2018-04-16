from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
	response = "placeholder to later display all the list of blogs"
	return HttpResponse(response)

def new(request):
	response = "placeholder to display a new form to create a blog"
	return HttpResponse(response)

def create(request):
	return redirect(index)

def show(request, number):
	return HttpResponse("placeholder to display blog " + number)

def edit(request, number):
	return HttpResponse("placeholder to edit blog " + number)

def destroy(request):
	return redirect(index)
