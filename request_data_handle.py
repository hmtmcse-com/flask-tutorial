from flask import Flask, request

app = Flask(__name__)


@app.route('/url-params/<int:age>/<string:country>/<float:salary>')
def url_params(age: int, country: str, salary: float):
    return "URL Parameter data are: " + str(age) + ", " + country + ", " + str(salary)


@app.route('/query-arguments')
def query_arguments():
    # Get all argument
    all_argument = request.args

    # array arguments
    data_type = None
    argument_array = request.args.getlist("skill", data_type)

    # Get specific data from dictionary
    age = -1
    if "age" in request.args:
        age = request.args["age"]

    # Get specific data by method
    salary = request.args.get("salary")  # if key doesn't exist, returns None

    # if key doesn't exist, returns a 400, bad request error
    country = request.args['country']

    print(all_argument)
    print(argument_array)
    return "Query Arguments Data: " + str(age) + ", " + country + ", " + str(salary)


@app.route('/form')
def form():
    return '''
               <form action="/form-data" method="POST">
                   <div><label>Age:</label><input type="number" name="age"></div>
                   <div><label>Country:</label><input type="text" name="country"></div>
                   <div><label>Salary:</label><input type="number" name="salary"></div>
                   <div><label>Skill:</label>
                        <select name="skill" multiple>
                        <option value="python">Python</option>
                        <option value="typescript">Typescript</option>
                        <option value="react">React</option>
                        <option value="flask">Flask</option>
                        </select>
                   </div>
                   <input type="submit" value="Submit">
               </form>
               '''


@app.route('/form-data', methods=["POST"])
def form_data():
    form_all_data = request.form

    default_value = None
    data_type = None
    age = request.form.get("age", default_value, data_type)

    argument_array = request.form.getlist("skill", data_type)

    country = ''
    if "country" in request.form:
        country = request.form["country"]

    salary = request.form.get("salary", 0.0, float)

    print(form_all_data)
    print(argument_array)
    return "Form Data: " + str(age) + ", " + country + ", " + str(salary)


@app.route('/file-submission')
def file_submission():
    return '''
               <form action="/file-data" method="POST" enctype="multipart/form-data">
                   <div><label>File:</label><input type="file" name="file"></div>
                   <input type="submit" value="Submit">
               </form>
               '''


@app.route('/file-data', methods=["POST"])
def file_data():
    form_files = request.files
    file_list = []
    for file_name in form_files:
        file = form_files[file_name]
        file_list.append({
            "inputName": file.name,
            "filename": file.filename,
            "contentType": file.content_type,
            "mimetype": file.mimetype,
        })
    return {"fileInfoList": file_list}


@app.route('/json-data', methods=["POST"])
def json_data():
    json_data_object = request.get_json()
    age = 0
    if "age" in json_data_object:
        age = json_data_object["age"]

    country = ''
    if "country" in json_data_object:
        country = json_data_object["country"]

    salary = 0.0
    if "salary" in json_data_object:
        salary = json_data_object["salary"]

    argument_array = []
    if "skill" in json_data_object:
        argument_array = json_data_object["skill"]

    print(json_data_object)
    print(argument_array)
    return "JSON Data: " + str(age) + ", " + country + ", " + str(salary)


@app.route('/get-url-info')
def get_url_info():
    url_info = {
        'relative_url': str(request.url_rule),
        'relative_url_with_param': str(request.full_path),
        'host_with_port': str(request.host),
        'method': str(request.method),
        'charset': str(request.url_charset)
    }
    return url_info


@app.route('/get-header')
def get_header():
    default_value = None
    auth = request.headers.get("auth", default_value)
    return "Header : " + auth


if __name__ == '__main__':
    app.run()
