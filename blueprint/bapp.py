from flask import Flask
from blueprint.student.student import student_blueprint

app = Flask(__name__)

app.register_blueprint(student_blueprint)


@app.route('/')
def bismillah():
    return "Blueprint Project"


if __name__ == '__main__':
    app.run()
