# hello.py
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/hello/")
def hello(name=None):
	return render_template('hello.html', name=name)
	
if __name__ == "__main__":
	app.run()