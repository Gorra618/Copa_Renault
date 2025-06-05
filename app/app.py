from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "NikoStasyszyn"
app.config["MYSQL_DB"] = "book_shop"

mysql = MySQL(app)


@app.route("/")
def index():
    data = {
        "title": "Copa Renault 🏆",
    }
    return render_template("main_page.html", data=data)


if __name__ == "__main__":
    app.run(debug=True, port=3300)
