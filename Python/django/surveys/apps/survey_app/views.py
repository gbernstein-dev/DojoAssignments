from django.shortcuts import render, HttpResponse, redirect

def index(request):
	if request.method == 'POST':
		return render(request, 'survey_app/result.html', {'name':request.session['first_name'], 'location':request.session['dojo_location'], 'language':request.session['favorite_language'], 'comments':request.session['comment_section']})
	else:
		return render(request, 'survey_app/index.html')


