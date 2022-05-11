import sys

from flask import render_template, request, redirect, make_response
from flask import session, flash
from __init__ import app, socket
from flask_socketio import SocketIO, emit

from utils.authentication import generate_auth_token
from utils.database import register, authenticate, add_auth_token
from utils.cookie_parsing import parse_visits, auth_user
from bcrypt import checkpw

votes = 0  # this is needed for working upvote/downvote

online_users = {}


# TODO move public docs into /public

@app.route("/")
@app.route("/home")
def homepage():
    global online_users
    online_user_list = [users for users, status in online_users.items() if status]

    print(f"Cookies: {request.cookies}")
    username: str = auth_user(request.cookies)
    visits: str = parse_visits(request.cookies)

    response = make_response(
        render_template('homepage.html', online_users=online_user_list,
                        name=username, visits=visits))
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
        username, password = request.form.get("username").strip(), request.form.get("password")

        user = authenticate(username)
        if user and checkpw(password.encode(), user["password"]):
            flash(u'Authentication Successful', 'success')
            global online_users
            online_users[username] = True

            response = redirect("/")
            auth_token = generate_auth_token()
            add_auth_token(username, auth_token)
            response.set_cookie('auth_token', value=auth_token, max_age=3600)
            return response
        else:
            flash(u'Incorrect username/password', 'danger')
            return redirect(request.url)

    return render_template('login.html')


@app.route("/sign-up", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username, password = request.form.get("username").strip(), request.form.get("password")
        print(f"username: {username}, password: {password}")
        register(username, password)
        flash(u'Account created successfully', 'success')
        # -> /login (or bypass login) -> homepage
        # return redirect("/")
        return redirect("/login")
    return render_template('signup.html')


# TODO toggle logout button to only show when user is logged in
@app.route("/logout")
def logout():
    username = auth_user(request.cookies)
    if not username:
        flash(u'You have to be logged in to go logout', 'warning')
        return redirect('/login')
    else:
        flash(u'Logged out successfully', 'success')
        online_users.pop(username, None)
        response = redirect("/")
        response.set_cookie('auth_token', expires=0)
        return response


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
