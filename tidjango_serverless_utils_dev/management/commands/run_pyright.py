"""The Pyright command execution script.

Command example:
$ python manage.py run_pyright
"""

from typing import Any, Match
import re

from django.core.management.base import BaseCommand

from tidjango_serverless_utils_dev.management.commands import command_utils

PYRIGHT_COMMAND: str = "pyright ./"


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:
        """
        Run the Pyright command.
        """
        run_pyright()


class PyrightError(Exception):
    pass


def run_pyright() -> None:
    """
    Run the Pyright command.

    Raises
    ------
    PyrightError
        If errors exist in the Pyright command output.
    """
    output: str = command_utils.run_command_with_no_shell(command=PYRIGHT_COMMAND)
    match_: Match | None = re.search(
        pattern=r"0 errors, 0 warnings, 0 informations",
        string=output,
        flags=re.MULTILINE,
    )
    if match_ is not None:
        return
    raise PyrightError(f"Errors occurred during Pyright command execution:\n{output}")
