from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
	session['total'] = 0
	return render_template("index.html",total=session['total'])

@app.route('/', methods=['POST'])
def increase():
	session['total'] += 2
	return render_template('index.html')

app.run(debug=True)
