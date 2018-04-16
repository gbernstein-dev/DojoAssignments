from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# the index function is called when root is visited
def index(request):
	if request.method == 'POST':
		if request.POST.get('fun') == 'gen_word': 
			request.session['word'] = get_random_string(length=32)
			request.session['attempt'] += 1
			return render(request, 'random_word/index.html', {'word':request.session['word'], 'attempt':request.session['attempt']})
		else:
			request.session['attempt'] = 0
			return render(request, 'random_word/index.html', {'word':request.session['word'], 'attempt':request.session['attempt']})
	else:
		request.session['word'] = get_random_string(length=32)
		request.session['attempt'] = 1
		return render(request, 'random_word/index.html', {'word':request.session['word'], 'attempt':request.session['attempt']})

# def reset(request):
# 	request.session['attempt'] = 0
# 	return render(request, 'random_word/index.html', {'word':request.session['word'], 'attempt':request.session['attempt']})
