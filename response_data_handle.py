import os

from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/string-response')
def string_response():
    return "Response String"


@app.route('/json-response')
def json_response():
    response_dict = {
        "name": "HMTMCSE Education",
        "location": "Bangladesh & Canada",
        "description": "This is an Educational organization, which aim to provide professional training."
    }
    return response_dict


@app.route('/html-template-response')
def html_template_response():
    return render_template("html-template-response.html")


@app.route('/custom-response')
def custom_response():
    status_code = 201
    headers = {
        "custom": "Custom Data"
    }
    response_data = "Custom Response"
    response = (response_data, status_code, headers)
    return response


@app.route('/file-response')
def file_response():
    file = os.path.join(app.root_path, 'resources', 'download.zip')
    return send_file(file)


if __name__ == '__main__':
    app.run()
