"""The flake8 command execution script.

Command example:
$ python manage.py run_flake8
"""

from typing import Any

from django.core.management.base import BaseCommand

from tidjango_serverless_utils_dev.management.commands import command_utils

FLAKE8_COMMAND = "flake8 ."


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:
        """
        Run the flake8 command.
        """
        run_flake8()


class Flake8Error(Exception):
    pass


def run_flake8() -> None:
    """
    Run the flake8 command.

    Raises
    ------
    Flake8Error
        If errors exist in the flake8 command output.
    """
    output: str = command_utils.run_command_with_no_shell(command=FLAKE8_COMMAND)
    if output != "":
        raise Flake8Error(f"Errors occurred during flake8 command execution:\n{output}")
