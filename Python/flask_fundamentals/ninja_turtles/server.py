from flask import Flask, render_template, request, redirect
app=Flask(__name__)

@app.route('/')

def index():
  return render_template("index.html")

@app.route('/ninja')

def ninja():
  return render_template("ninja.html")

@app.route('/ninja/<color>')

def ninja_color(color):
  if color == "blue":
    return render_template("ninja_blue.html")
  elif color == "orange":
    return render_template("ninja_orange.html")
  elif color == "purple":
    return render_template("ninja_purple.html")
  elif color == "red":
    return render_template("ninja_red.html")
  else:
    return render_template("wrong_entry.html")

app.run(debug=True)