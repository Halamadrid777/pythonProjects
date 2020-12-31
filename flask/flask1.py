from flask import Flask, redirect,url_for

app = Flask(__name__)


# this decorator routes the user to the home page
@app.route("/home")
def home():
    return "Hello this is the home page! <h1>Hello</h1>"

@app.route("/")
def mainPage():
    return "This is the main page"

# what "<name>" does is grabs whatever the input is given and returns the value
@app.route("/<name>")
def user(name):
    return f"hello {name}!" 

@app.route("/admin")
def admin():
    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run()