from flask import Flask, render_template, request, url_for
import smtplib
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send_mail", methods=["GET", "POST"])
def send_mail():
    if request.method == "POST":
        name = request.form['name']
        mail = request.form['mail']
        sub = request.form['subject']
        msg = request.form['message']
        user = {"name": [name], "mail": [mail], "sub": [sub], "msg": msg}
        my_mail = "rizzpython@gmail.com"
        app_pass = "zafqvfsooxqtdnul"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail, password=app_pass)
            connection.sendmail(from_addr=my_mail,
                                to_addrs=user["mail"][0],
                                msg=f"subject:{user["sub"][0]}\n\n {user["msg"][0:]}")


    return "mail sent successfully"

if __name__ == "__main__":
    app.run(debug=True)
