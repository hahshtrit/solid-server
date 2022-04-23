from flask import render_template
from flasking import app

@app.route("/")
@app.route("/home")
def homepage():
    return render_template('homepage.html', title="Home Page")

@app.route("/about")
def about():
    return render_template('about.html', title="about")

@app.route("/account")
def account():
    return render_template('account.html', title="account")