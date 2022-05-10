from flask import render_template, request, redirect, make_response
from flask import session
from __init__ import app, socket
from flask_socketio import SocketIO, emit

votes = 0 # this is needed for working upvote/downvote

@app.route("/")
@app.route("/home")
def homepage():
    # print("getting the resquest")
    # # setting up a cookie
    # resp = make_response(render_template('homepage.html'))
    # resp.set_cookie('visits', value="1")
    return render_template('homepage.html')
    # return resp

    # return render_template('homepage.html', votes=votes) # this is for working upvote/downvote
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
        # register_user(username, password)
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