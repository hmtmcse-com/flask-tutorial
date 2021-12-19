from flask import Flask, make_response, request, session

app = Flask(__name__)

app.secret_key = 'SecretKey'


@app.route('/set-cookie')
def set_cookie():
    response = make_response("Set Cookie")
    response.set_cookie('cookieData', 'This is Cookie Data')
    return response


@app.route('/get-cookie')
def get_cookie():
    all_cookies = request.cookies
    cookie_data = request.cookies.get("cookieData")
    print(all_cookies)
    return "CookieData : " + cookie_data


@app.route('/set-session')
def set_session():
    session['sessionData'] = "This is session data."
    return "Set Session Data"


@app.route('/get-session')
def get_session():
    if 'sessionData' in session:
        return "The session data is : " + session["sessionData"]
    return "Session not exists!"


if __name__ == '__main__':
    app.run()