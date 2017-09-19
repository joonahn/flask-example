# hello.py
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'blog'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

@app.route("/hello/")
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route("/loadData")
def loadData():
	cursor = mysql.connect().cursor()
	cursor.execute("select * from blog")

	result = []

	for row in cursor:
		result.append(row)

	print (result)
	return "load Test" + ''.join(str(e) for e in result)


@app.route("/home")
def home():
	cursor = mysql.connect().cursor()
	cursor.execute("select * from blog")

	posts = []

	for row in cursor:
		post = {}
		post['href'] = "./{}".format(row[0])
		post["title"] = row[1]
		post["content"] = row[2]
		posts.append(post)


	return render_template('home.html', posts=posts)
	
if __name__ == "__main__":
	app.run()