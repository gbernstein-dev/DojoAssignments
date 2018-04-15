from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'mydb')

@app.route('/')
def index():
  friends = mysql.query_db("SELECT * FROM friends_table")
  # year = mysql.query_db("SELECT YEAR(friend_since) FROM friends_table")
  # month = mysql.query_db("SELECT MONTH(friend_since) FROM friends_table")
  # day = mysql.query_db("SELECT DAY(friend_since) FROM friends_table")
  
  return render_template('index.html', all_friends=friends)

@app.route('/', methods=['POST'])
def create():
  query = "INSERT INTO friends_table (first_name, last_name, friend_since) VALUES (:first_name, :last_name, NOW())"

  data = {'first_name': request.form['first_name'],
          'last_name': request.form['last_name']}

  mysql.query_db(query, data)
  return redirect('/')

app.run(debug=True)
