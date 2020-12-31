from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/admin")
def admin():
    return "Hello you  are in the admin page"


@app.route("/tutorial9")
def render9():
    return render_template("tutorial9.html",fromFlask2="This is imported from Flask2 backends!")

if __name__ == "__main__":
    app.run()
