from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def home():
    return render_template("index.html")

# adds path to the hosted page (localhost7000/mech)
@app.route("/mech", methods = ["GET"])
def mech():
    return render_template("mech.html")



if __name__ == "__main__":
    app.run( port = 7000, debug = True)