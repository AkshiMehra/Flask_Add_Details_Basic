from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


# Define the Student model representing the table structure in the database
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)
    phone_number = db.Column(db.String(20))
    college = db.Column(db.String(80))
    comments = db.Column(db.Text)

    def __init__(self, name, age, phone_number, college, comments):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.college = college
        self.comments = comments


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data from the request
        name = request.form['name']
        age = int(request.form['age'])
        phone_number = request.form['phone_number']
        college = request.form['college']
        comments = request.form['comments']

        # Create a new Student object with the provided form data
        student = Student(name=name, age=age, phone_number=phone_number, college=college, comments=comments)
        db.session.add(student)
        db.session.commit()

    # Retrieve all students from the database
    students = Student.query.all()
    return render_template('index.html', students=students)


if __name__ == '__main__':
    with app.app_context():
        # Create the database tables
        db.create_all()
    # Start the Flask development server
    app.run(debug=True)
