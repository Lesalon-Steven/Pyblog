from flask import Flask, render_template
import requests

app = Flask(__name__)

my_api = "https://api.npoint.io/4e1f43c7040a6fa538fa"


posts = requests.get(my_api).json()





@app.route('/')
def hello():
    return render_template("index.html", posts=posts)


@app.route("/about")
def about_me():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
