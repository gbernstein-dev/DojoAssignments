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
  low_range = random.randrange(-10,11)
  mid_range = random.randrange(-50,51)
  high_range = random.randrange(-100,101)

  last_total = session['total']

  if request.form['bet'] == 'low':
    session['total'] += low_range
    session['response'] = "Gold increment: "+str(low_range)
  elif request.form['bet'] == 'mid':
    session['total'] += mid_range
    session['response'] = "Gold increment: "+str(mid_range)
  elif request.form['bet'] == 'high':
    session['total'] += high_range
    session['response'] = "Gold increment: "+str(high_range)
  if session['total'] < 0:
    session['total'] = 0
    session['response'] = "You went negative!"


  return render_template("index.html", total=session['total'], response=session['response'], last_total=last_total)

app.run(debug=True)