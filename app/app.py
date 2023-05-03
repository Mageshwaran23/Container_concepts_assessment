
from flask import Flask, request, render_template
from flask import *
import mysql.connector
import os

app = Flask(__name__)


db = mysql.connector.Connect(
    host="localhost",
    user="root",
    password="Magesh_99414",
    database="vaccination"
)
cursor = db.cursor()
cursor.execute("select * from status")

@app.route("/", methods=["GET"])
def main():

    return render_template("home.html")


@app.route("/register", methods=["POST"])
def register():

    if request.method == 'POST':
        result = request.form.to_dict()
        name = str(result['name'])
        regno = int(result['regno'])
        status = str(result['status'])

        cursor.execute(
            "insert into status (name,regno,status) values (%s,%s,%s)", (name, regno, status))
        db.commit()
        cursor.close()
        return render_template("register.html", result=result)

@ app.route("/register", methods=["GET"])
def register_get():

    return render_template("register.html")

@ app.route("/login", methods=["GET"])
def login_get():

    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))
