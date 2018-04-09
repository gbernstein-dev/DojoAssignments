from flask import Flask, render_template, request, redirect, session
import random
app=Flask(__name__)
app.secret_key = 'secret'

@app.route('/')

def index():
  session['total'] = 0
  session['response'] = 'Click a value to begin!'
  return render_template("index.html", total=session['total'], response=session['response'])

@app.route('/', methods=['POST'])

def process_money():
  farm_range = random.randrange(-10,11)
  apartment_range = random.randrange(-50,51)
  mansion_range = random.randrange(-100,101)

  last_total = session['total']

  if request.form['building'] == 'farm':
    session['total'] += farm_range
    session['response'] = "Gold increment: "+str(farm_range)
  elif request.form['building'] == 'apartment':
    session['total'] += apartment_range
    session['total'] += apartment_range
    session['response'] = "Gold increment: "+str(apartment_range)
  elif request.form['building'] == 'mansion':
    session['total'] += mansion_range
    session['total'] += mansion_range
    session['response'] = "Gold increment: "+str(mansion_range)
  if session['total'] < 0:
    session['total'] = 0
    session['response'] = "You went negative!"


  return render_template("index.html", total=session['total'], response=session['response'], last_total=last_total)

app.run(debug=True)