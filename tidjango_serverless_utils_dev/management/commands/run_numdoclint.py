"""The numdoclint command execution script.

Command example:
$ python manage.py run_numdoclint
"""

from typing import Any

from django.core.management.base import BaseCommand

from tidjango_serverless_utils_dev.management.commands import command_utils

NUMDOCLINT_COMMAND: str = (
    "numdoclint -r "
    "-f test,sample,_test,_sample,mock_,teardown,setup,wrapped,inner_wrapped -p ./"
)


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:
        """
        Run the numdoclint command.
        """
        run_numdoclint()


class NumdoclintError(Exception):
    pass


def run_numdoclint() -> None:
    """
    Run the numdoclint command.

    Raises
    ------
    NumdoclintError
        If errors exist in the numdoclint command output.
    """
    output: str = command_utils.run_command_with_no_shell(command=NUMDOCLINT_COMMAND)
    if output != "":
        raise NumdoclintError(
            f"Errors occurred during numdoclint command execution:\n{output}"
        )
