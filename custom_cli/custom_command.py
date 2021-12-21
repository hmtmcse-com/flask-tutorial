import click
from flask import Flask
from flask.cli import AppGroup, with_appcontext

from custom_cli.blueprint_command import blue_command, blue_with_command_group

app = Flask(__name__)
app.register_blueprint(blue_command)
app.register_blueprint(blue_with_command_group, cli_group='blue_group')


@app.cli.command("create-user")
@click.argument("name")
def simple_create_user(name):
    print(name)


user_cli = AppGroup('user')
@user_cli.command('create')
@click.argument('name')
def group_create_user(name):
    print(name)


app.cli.add_command(user_cli)

@click.command("with-app-context")
@with_appcontext
def command_with_appcontext():
    print("Run command with app context")


app.cli.add_command(command_with_appcontext)


if __name__ == '__main__':
    app.run()
