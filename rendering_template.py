from flask import Flask, render_template
from blueprint.student.student import student_blueprint

app = Flask(__name__)

app.register_blueprint(student_blueprint)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/render-with-string')
@app.route('/render-with-string/<string:name>')
def render_with_string(name="HMTM"):
    return render_template("render-with-string.html", name=name)


@app.route('/render-with-dictionary')
def render_with_dictionary():
    persons = [
        {'name': 'Touhid', 'age': 34},
        {'name': 'Rakib', 'age': 17},
        {'name': 'Thomas', 'age': 44},
        {'name': 'Habib', 'age': 14},
        {'name': 'Robert', 'age': 23},
        {'name': 'Shammi', 'age': 20}
    ]
    return render_template("render-with-dictionary.html", persons=persons)


if __name__ == '__main__':
    app.run()
