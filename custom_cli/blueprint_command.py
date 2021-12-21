import click
from flask import Blueprint

blue_command = Blueprint('blue_command', __name__)


@blue_command.cli.command('create')
@click.argument('name')
def create(name):
    print("Name : " + str(name))


blue_with_command_group = Blueprint('blue_with_command_group', __name__, cli_group="blue_group")


@blue_with_command_group.cli.command('create')
@click.argument('name')
def blue_group_create(name):
    print("Name : " + str(name))
