from flask import render_template, request, redirect, make_response
from flask import session
from __init__ import app

from utils.database import register_user

# @app.route('/getcookie')
# def getcookie():
#     visits = request.cookies.get('visits')
#     print(visits)


@app.route("/")
@app.route("/home")
def homepage():
    # setting up a cookie
    resp = make_response(render_template('homepage.html'))
    resp.set_cookie('visits', value="1")
    return resp

    # return render_template('homepage.html', online_users=online_users)

@app.route("/about")  # not gonna be used
def about():
    return render_template('about.html')

@app.route("/account")  # has settings and dms
def account():
    return render_template('account.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        # TODO authenticate user
        print("login")
        print(f"username: {username}, password {password}")
        # check if successful login
        # if so, add cookie auth_token, add user to online_users
        # else render_template('login.html') ?
        return redirect("/")
    return render_template('login.html')


@app.route("/sign-up", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        print("signup")
        print(f"username: {username}, password: {password}")
        register_user(username, password)
        # -> /login (or bypass login) -> homepage
        return redirect("/")
    return render_template('signup.html')
