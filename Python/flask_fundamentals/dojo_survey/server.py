from flask import Flask, render_template, request, redirect
app=Flask(__name__)

@app.route('/')

def index():
  return render_template("index.html")

@app.route('/result', methods=['GET','POST'])

def process():
  first_name = request.form.get('first_name')
  dojo_location = request.form.get('dojo_location')
  favorite_language = request.form.get('favorite_language')
  comment_section = request.form.get('comment_section')
  print dojo_location
  return render_template("result.html", name=first_name, location=dojo_location, language=favorite_language, comments=comment_section)

app.run(debug=True)
