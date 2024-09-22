"""The mysql_db_name environment variable is used to set the name of the MySQL database.

Command example:
$ python manage.py run_mypy
"""

from typing import Any, Match
import re

from django.core.management.base import BaseCommand

from tidjango_serverless_utils_dev.management.commands import command_utils

MYPY_COMMAND = "mypy ."


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:
        """
        Run the mypy command.
        """
        run_mypy()


class MypyError(Exception):
    pass


def run_mypy() -> None:
    """
    Run the mypy command.

    Raises
    ------
    MypyError
        If errors exist in the mypy command output.
    """
    output: str = command_utils.run_command_with_no_shell(command=MYPY_COMMAND)
    match_: Match | None = re.search(
        pattern=r"Found \d+? error",
        string=output,
        flags=re.MULTILINE,
    )
    if match_ is None:
        return
    raise MypyError(f"Errors occurred during mypy command execution:\n{output}")
