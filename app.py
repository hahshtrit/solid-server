from flask import Flask, render_template, request, redirect

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/")
@app.route("/home")
def homepage():
    return render_template('homepage.html')


@app.route("/about")  # not gonna be used
def about():
    return render_template('about.html')


@app.route("/account")
def account():
    return render_template('account.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        print("login")
        print(f"username: {username}, password {password}")
        return redirect("/")
    return render_template('login.html')


@app.route("/sign-up", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        print("signup")
        print(f"username: {username}, password: {password}")

        return redirect("/")
    return render_template('signup.html')
