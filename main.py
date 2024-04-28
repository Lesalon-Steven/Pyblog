from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)

my_api = "https://api.npoint.io/4e1f43c7040a6fa538fa"

posts = requests.get(my_api).json()


@app.route('/')
def hello():
    return render_template("index.html", posts=posts)


@app.route("/about")
def about_me():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    if request.method == "POST":
        return data_handler()


@app.route("/contact")
def data_handler():
    mail = ""
    passkey = ""
    name_given = request.form["name"]
    email_given = request.form["email"]
    message = request.form["message"]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(mail, passkey)
        connection.sendmail(from_addr=mail, to_addrs=email_given, msg=f"Subject:Complain\n\n {message}", )

    return f"<h1>{name_given}, {email_given}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
