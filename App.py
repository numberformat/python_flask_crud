from flask import Flask, render_template, request, redirect, url_for, flash
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

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = Data(name, email, phone)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

        return redirect(url_for('Index'))

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        employee_id = request.form.get('id')
        # Use Session.get() instead of Query.get()
        employee = db.session.get(Data, employee_id)

        if not employee:
            flash("Employee not found.")
            return redirect(url_for('Index'))

        employee.name = request.form['name']
        employee.email = request.form['email']
        employee.phone = request.form['phone']

        db.session.commit()
        flash("Employee Updated Successfully")
        return redirect(url_for('Index'))

@app.route('/delete', methods = ['POST'])
def delete():
    employee_id = request.form['id']
    # Use Session.get() instead of Query.get()
    employee = db.session.get(Data, employee_id)

    if not employee:
        flash("Employee not found.")
        return redirect(url_for('Index'))

    db.session.delete(employee)
    db.session.commit()

    flash("Employee Deleted Successfully")
    return redirect(url_for('Index'))

@app.route('/')
def Index():
    all_data = Data.query.all()
    return render_template("index.html", employees = all_data)

if __name__ == '__main__':
    app.run(debug=True)
