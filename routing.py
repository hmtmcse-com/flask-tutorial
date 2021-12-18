from flask import Flask, request, url_for, abort, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return 'Home Page'


@app.route('/other')
def hello():
    return 'Other Page'


@app.route('/operator/edit/<operator_id>')
def edit_operator(operator_id):
    return "Operator id: " + operator_id


@app.route('/operator/edit-with-type/<int:operator_id>')
def edit_operator_with_data_type(operator_id: int):
    return "Operator id with data type: " + str(operator_id)


@app.route('/path/<path:sub_path>')
def show_sub_path(sub_path):
    return "Sub-path : " + sub_path


@app.route('/method/post-only', methods=['POST'])
def post_only():
    return "Yeh the request method is POST"


@app.route('/method/post-or-get', methods=['POST', 'GET'])
def post_or_get():
    if request.method == 'POST':
        return "Yeh the request method is POST"
    else:
        return "Yeh the request method is GET"


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/url-for-test')
def url_for_test():
    print(url_for('index'))
    print(url_for('index', next='/other'))
    print(url_for('edit_operator', operator_id='10'))
    return 'URL for print in console'


@app.errorhandler(404)
def page_404(error):
    return "404 Not found!"


@app.errorhandler(500)
def page_500(error):
    return "500 Internal error!"


@app.errorhandler(401)
def page_401(error):
    return "401 Unauthorized!"


@app.route('/show-error')
def show_error():
    abort(401)
    return "Should not show"


@app.route('/redirect-to-other')
def redirect_to_other():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
