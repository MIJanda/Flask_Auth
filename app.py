from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)


@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html")


if __name__ in "__main__":
    # todo: change to false in production
    app.run(debug=True)
