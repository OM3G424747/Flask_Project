from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
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

# adds path to the hosted page (localhost7000/mech)
@app.route("/mech", methods = ["GET"])
def mech():
    return render_template("mech.html")

@app.route("/signup", methods = ["GET"])
def signup():
    return render_template("mech.html")

if __name__ == "__main__":
    app.run( port = 7000, debug = True)