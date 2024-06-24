from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///employee.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
# start python and type the following to create tables in the database.
#>>> from App import app, db
#>>> with app.app_context():
#...     db.create_all()
# check the ./instance folder.

@app.route('/')
def Index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
