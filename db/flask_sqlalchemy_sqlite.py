from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flask-sqlalchemy.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=True)
    email = db.Column(db.String(150), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def bismillah():
    return "Flask SQLAlchemy"


@app.route('/create')
def create():
    person = Person(first_name="First Name", last_name="Last Name", email="hmtmcse.com@gmail.com")
    db.session.add(person)
    db.session.commit()
    response = "Data successfully Inserted"
    return response

@app.route('/update')
def update():
    person = Person.query.filter_by(id=1).first()
    if person:
        person.first_name = "FName Update"
        person.last_name = "LName Update"
        db.session.add(person)
        db.session.commit()
    return "Data has been updated."


@app.route('/delete')
def delete():
    person = Person.query.filter_by(id=1).first()
    if person:
        db.session.delete(person)
        db.session.commit()
    return "Record has been deleted"


@app.route('/list')
def list():
    response = ""
    persons = Person.query.limit(1).all()
    for person in persons:
        response += person.first_name + " " + person.last_name + " " + person.email + "<br>"
    return response


if __name__ == '__main__':
    app.run()
