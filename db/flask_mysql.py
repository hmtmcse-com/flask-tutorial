import click
from flask import Flask, g, current_app
from flask.cli import with_appcontext
import mysql.connector


def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="flask_mysql"
        )
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    mysql_cursor = db.cursor()
    with current_app.open_resource('mysql-schema.sql') as f:
        mysql_cursor.execute(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')


app = Flask(__name__)
app.teardown_appcontext(close_db)
app.cli.add_command(init_db_command)


@app.route('/')
def bismillah():
    return "Flask MySQL Tutorial"


@app.route('/create')
def create():
    try:
        db = get_db()
        db.cursor().execute("INSERT INTO person (first_name, last_name, email) VALUES (%s, %s, %s)", ("First Name", "Last Name", "hmtmcse.com@gmail.com"),)
        db.commit()
    except mysql.connector.Error as err:
        print(err)
        response = "Not able to Insert Data"
    else:
        response = "Data successfully Inserted"
    return response


@app.route('/update')
def update():
    db = get_db()
    db.cursor().execute('UPDATE person SET first_name = %s, last_name = %s WHERE id = %s', ("FName Update", "LName Update", 1))
    db.commit()
    return "Data has been updated."


@app.route('/delete')
def delete():
    db = get_db()
    db.cursor().execute('DELETE FROM person WHERE id = %s', (1,))
    db.commit()
    return "Record has been deleted"


@app.route('/list')
def list():
    response = ""
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM person')
    persons = cursor.fetchall()
    for person in persons:
        response += person[1] + " " + person[2] + " " + person[3] + "<br>"
    return response


if __name__ == '__main__':
    app.run()
