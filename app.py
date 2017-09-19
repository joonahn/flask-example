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
def homeView():
    cursor = mysql.connect().cursor()
    cursor.execute("select * from blog")
    posts = []
    for row in cursor:
        post = {}
        post['href'] = "./post/{}".format(row[0])
        post["title"] = row[1]
        post["summary"] = row[2]
        posts.append(post)
    return render_template('home.html', posts=posts)

@app.route("/post/<postId>")
def postView(postId):
    cursor = mysql.connect().cursor()
    cursor.execute("select * from blog where articleNumber = %s", [postId])
    posts = []
    for row in cursor:
        post = {}
        post["title"] = row[1]
        post["content"] = row[2]
        posts.append(post)
    
    if len(posts) == 0 or len(posts) > 1:
        return render_template('404.html'), 404
    else:
        return render_template('post.html', posts=posts)

if __name__ == "__main__":
    app.run()
