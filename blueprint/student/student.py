from flask import Blueprint, render_template

student_blueprint = Blueprint(
    name='student',
    import_name=__name__,
    url_prefix='/student',
    static_folder="student-static",
    static_url_path="student-static",
    template_folder="student-template"
)


@student_blueprint.route("/")
def index():
    return render_template("index.html")
