from flask import Flask, render_template, request, redirect
app=Flask(__name__)

@app.route('/')

def index():
	return render_template("index.html")


@app.route('/process', methods=['GET','POST'])
def process():
	print "Got data!"

	name = request.form['name']
	# redirects back to the '/' route
	return redirect('/')

app.run(debug=False) # run our server
