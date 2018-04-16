from django.shortcuts import render, HttpResponse, redirect

def index(request):
  return render(request, 'survey_app/index.html')

def process(request):
  context = {
  request.session['first_name']: request.POST['first_name'],
  request.session['dojo_location']: request.POST['dojo_location'],
  request.session['favorite_language']: request.POST['favorite_language'],
  request.session['comment_section']: request.POST['comment_section']
  }
  
  print request.session['first_name']

  return redirect(request,'/survey_app/result.html',context)


