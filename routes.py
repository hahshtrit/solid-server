import sys

import bcrypt
from flask import render_template, request, redirect, make_response
from flask import session
from __init__ import app, socket
from flask_socketio import SocketIO, emit

votes = 0 # this is needed for working upvote/downvote

from utils.authentication import generate_auth_token
from utils.database import register, authenticate, add_auth_token
from utils.cookie_parsing import parse_visits, auth_user


@app.route("/")
@app.route("/home")
def homepage():
    online_users = ["mike", "placeholder", "names"]
    print(f"Cookies: {request.cookies}")
    username: str = auth_user(request.cookies)
    visits: str = parse_visits(request.cookies)

    response = make_response(
        render_template('homepage.html', online_users=online_users, name=username, visits=visits))
    response.set_cookie('visits', value=visits)
    sys.stdout.flush()
    return response


@app.route("/about")  # not gonna be used
def about():
    return render_template('about.html')


@app.route("/account")  # has settings and dms
def account():
    return render_template('account.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username, password = request.form.get("username").strip(), request.form.get("password").strip()
        print(f"username: {username}, password: {password}")
        user = authenticate(username)
        if user and bcrypt.checkpw(password.encode(), user["password"]):
            # TODO add user to online_users
            # session[user] = True
            response = redirect("/")

            auth_token = generate_auth_token()
            add_auth_token(username, auth_token)

            response.set_cookie('auth_token', value=auth_token)
            return response
        else:
            print("Incorrect username/password")
            return render_template('login.html')

    return render_template('login.html')


@app.route("/sign-up", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username, password = request.form.get("username").strip(), request.form.get("password").strip()
        print(f"username: {username}, password: {password}")
        register(username, password)
        # -> /login (or bypass login) -> homepage
        return redirect("/")
    return render_template('signup.html')

# this is working socket stuff for upvote/downvote
# @socket.on('upvote')
# def upvote(data):
#     print("upvote")
#     print(data)
#     global votes
#     votes += 1
#     print(votes)
#     # data['votes'] = str(int(data['votes']) + 1)
#     # print(data)
#     # emit('update_votes', {'votes': data['votes']})
#     emit('update_votes', votes, broadcast=True)

# @socket.on('downvote')
# def downvote(data):
#     print("downvote")
#     print(data)
#     global votes
#     votes -= 1
#     print(votes)
#     # data['votes'] = str(int(data['votes']) + 1)
#     # print(data)
#     # emit('update_votes', {'votes': data['votes']})
#     emit('update_votes', votes, broadcast=True)

@app.route('/draw')
def draw():
    return render_template('draw.html')

@socket.on('draw')
def draw(data):
    print(data)
    emit('drawing', data, broadcast=True)

@socket.on('stop_drawing')
def stop_draw(data):
    print(data)
    emit('stopping_drawing', data, broadcast=True)