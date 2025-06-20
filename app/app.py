from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "NikoStasyszyn"
app.config["MYSQL_DB"] = "Copa_Renault"

mysql = MySQL(app)

app.secret_key = "clave_secreta_segura"


@app.route("/")
def index():
    data = {
        "title": "Copa Renault 🏆",
    }
    return render_template("main_page.html", data=data)


@app.route("/login", methods=["GET", "POST"])
def login():
    data = {"title": "Login"}
    if "usuario" in session:
        return redirect(url_for("index"))
    error = None
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM usuarios WHERE email=%s AND password=%s",
            (email, password),
        )
        usuario = cur.fetchone()
        cur.close()
        if usuario:
            session["usuario"] = email
            session["nombre"] = usuario[1]
            return redirect(url_for("index"))
        else:
            error = "Contraseña Incorrecta intentelo de nuevo"
    return render_template("login.html", data=data, error=error)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if "usuario" in session:
        return redirect(url_for("index"))
    if request.method == "POST":
        dni = request.form["dni"]
        nombre = request.form["nombre"].upper()
        apellidos = request.form["apellidos"].upper()
        email = request.form["email"]
        password = request.form["password"]
        actividad = request.form["actividad"]
        escuela = request.form["escuela"]

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO usuarios (dni, nombre, apellidos, email, password, actividad, escuela) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (dni, nombre, apellidos, email, password, actividad, escuela),
        )
        mysql.connection.commit()
        cur.close()
        session["usuario"] = email
        session["nombre"] = nombre
        return redirect(url_for("index"))
    data = {"title": "Sign Up"}
    return render_template("signup.html", data=data)


@app.context_processor
def inject_user():
    return dict(nombre_usuario=session.get("nombre"))

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=3300)
