from flask import Flask, render_template, request, redirect, flash
app=Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def process():

  first_name = request.form.get('first_name')
  dojo_location = request.form.get('dojo_location')
  favorite_language = request.form.get('favorite_language')
  comment_section = request.form.get('comment_section')
  if len(first_name) > 0 and len(comment_section) > 0:
    return render_template("result.html", name=first_name, location=dojo_location, language=favorite_language, comments=comment_section)
  else:
    flash("Must enter valid name, and comment!")
    return redirect('/')

app.run(debug=True)
