from subprocess import CalledProcessError

import click
from loguru import logger
from lt.shared.cli import cli_logging_options

from .app import App
from .auth import authenticate_live_stream_user
from .utils import ExecutableNotFound, get_version


@click.group()
def cli():
    pass


@cli.command()
@cli_logging_options
def run(**kwargs):
    """
    Run a liquidsoap server.
    """
    app = App(**kwargs)
    return app.run()


@cli.command()
@click.argument("source")
@click.argument("username")
@click.argument("password")
def auth(source, username, password):
    """
    Authenticate a remote user from SOURCE, USERNAME and PASSWORD.
    """
    is_valid_auth = authenticate_live_stream_user(username, password, source)
    return 0 if is_valid_auth else 1


@cli.command()
def version():
    """
    Print liquidsoap versions.
    """
    try:
        print(f"Liquidsoap: {get_version()}")
    except (CalledProcessError, ExecutableNotFound) as error:
        logger.critical(error)
        return 1
