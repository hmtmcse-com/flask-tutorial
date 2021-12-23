import os
import sqlite3

import click
from flask import Flask, g, current_app
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        database_path = os.path.join(app.root_path, "flask.sqlite")
        g.db = sqlite3.connect(
            database_path,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()
    with current_app.open_resource('sqlite-schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


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
    return "Flask SQLite Tutorial"


@app.route('/create')
def create():
    try:
        db = get_db()
        db.execute("INSERT INTO person (first_name, last_name, email) VALUES (?, ?, ?)", ("First Name", "Last Name", "hmtmcse.com@gmail.com"),)
        db.commit()
    except db.IntegrityError:
        response = "Not able to Insert Data"
    else:
        response = "Data successfully Inserted"
    return response


@app.route('/update')
def update():
    db = get_db()
    db.execute('UPDATE person SET first_name = ?, last_name = ? WHERE id = ?', ("FName Update", "LName Update", 1))
    db.commit()
    return "Data has been updated."


@app.route('/delete')
def delete():
    db = get_db()
    db.execute('DELETE FROM person WHERE id = ?', (1,))
    db.commit()
    return "Record has been deleted"


@app.route('/list')
def list():
    response = ""
    db = get_db()
    persons = db.execute(
        'SELECT * FROM person'
    ).fetchall()
    for person in persons:
        response += person["first_name"] + " " + person["last_name"] + " " + person["email"] + "<br>"
    return response


if __name__ == '__main__':
    app.run()
