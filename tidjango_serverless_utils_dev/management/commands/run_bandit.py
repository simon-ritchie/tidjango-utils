"""The Bandit command execution script.

Command example:
$ python manage.py run_bandit
"""

import json
from typing import Any

from django.core.management.base import BaseCommand

from tidjango_serverless_utils_dev.management.commands import command_utils

BANDIT_COMMAND: str = "bandit -q -f json -r ./tidjango_serverless_utils"


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:
        """
        Run the bandit command.
        """
        run_bandit()


class BanditError(Exception):
    pass


def run_bandit() -> None:
    """
    Run the Bandit command.

    Raises
    ------
    BanditError
        If errors exist in the Bandit command output.
    """
    output: str = command_utils.run_command_with_no_shell(command=BANDIT_COMMAND)
    results: list[Any] = json.loads(output).get("results", [])
    if results:
        raise BanditError(f"Errors occurred during Bandit command execution:\n{output}")
