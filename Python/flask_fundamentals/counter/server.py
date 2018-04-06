from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
	session['total'] = 0
	return render_template("index.html",total=session['total'])

@app.route('/', methods=['POST'])
def increase():
	if request.form['action'] == 'increase':
		session['total'] += 2
	elif request.form['action'] == 'reset':
		session['total'] = 1
	return render_template('index.html')

app.run(debug=True)
