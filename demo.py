from flask import Flask, render_template, request, session, redirect, url_for, g
import model

app = Flask(__name__)

# Placeholder secret key, to be replaced later
app.secret_key = "swordfish"

username = ""
user = model.check_users()

@app.route("/", methods = ["GET", "POST"])
def home():
    if username in session:
        g.user = session["username"]
        return render_template("mech.html")
    return render_template("homepage.html", message = "Login or Sign Up")
    
    """
    if request.method == "GET":
        return render_template("homepage.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        user_pass = model.check_pass(username)

        if password == model.check_pass(username):
            message = model.show_word(username)
            return render_template("mech.html", message = message)
        else:
            error_message = "Wrong Username or Password"
            return render_template("index.html", message = error_message)
    """

# adds path to the hosted page (localhost7000/mech)
@app.route("/mech", methods = ["GET"])
def mech():
    return render_template("mech.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        session.pop("username", None)
        areyouuser = request.form["username"]
        pwd = model.check_pass(areyouuser)
        if pwd == model.check_pass(areyouuser):
            session["username"] = request.form["username"]
            return redirect(for_url("home"))
    
    
    if request.method == "GET":
        message = "Please login to your account"
        return render_template("login.html", message = message)
    else:
        username = request.form["username"]
        password = request.form["password"]

        # checks if the password matches the username in DB
        if password == model.check_pass(username):
            message = model.show_word(username)
            return render_template("mech.html", message = message)
        else:
            # condition for wrong password
            error_message = "Wrong Username or Password"
            return render_template("login.html", message = error_message)


@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method == "GET":
        message = "Please register your account"
        return render_template("signup.html", message = message)
    else:
        username = request.form["username"]
        password = request.form["password"]
        secret_word = request.form["secret_word"]
        message = model.signup(username, password, secret_word)
        return render_template("signup.html", message = message)

if __name__ == "__main__":
    app.run( port = 7000, debug = True)