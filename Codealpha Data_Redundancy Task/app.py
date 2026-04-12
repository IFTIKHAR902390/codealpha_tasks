from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root123",
    password="root123",
    database="codealpha"
)

@app.route("/", methods=["GET", "POST"])
def index():

    message = ""

    cursor = db.cursor()

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]

        # Check if user already exists
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            message = "User already exists!"
        else:
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (%s, %s)",
                (name, email)
            )
            db.commit()
            message = "User added successfully!"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
