#this was Robert's attempt to start the graphics and web page part of the assignment.
#this code does not work and can be deleted
#you can also start the index.html part of this from scratch
import flask
from flask import Flask, render_template
import jinja2

app = Flask(__name__)

@app.route("/")
def index():
    headline = "hello"
    return render_template("index.html",headline=headline)

if __name__=="__main__":
    app.run()