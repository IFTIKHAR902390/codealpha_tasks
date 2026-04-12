from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root123",
    password="root123",
    database="codealpha"
)

@app.route("/", methods=["GET","POST"])
def index():

    message=""

    if request.method == "POST":

        name=request.form["name"]
        email=request.form["email"]

        cursor=db.cursor()

        cursor.execute("SELECT * FROM users WHERE email=%s",(email,))
        result=cursor.fetchone()

        if result:
            message="Duplicate data detected!"
        else:
            cursor.execute("INSERT INTO users(name,email) VALUES(%s,%s)",(name,email))
            db.commit()
            message="User added successfully"

    return render_template("index.html",message=message)

app.run(debug=True)