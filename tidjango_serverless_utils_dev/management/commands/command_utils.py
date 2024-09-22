"""Command-related utilities and definitions.
"""

import shlex
import subprocess as sp
import logging

_COMMAND_INFO_LOGGER_NAME: str = "command_info_logger"
_info_logger: logging.Logger = logging.getLogger(_COMMAND_INFO_LOGGER_NAME)
_formatter: logging.Formatter = logging.Formatter("%(asctime)s - %(message)s")
_console_handler: logging.StreamHandler = logging.StreamHandler()
_console_handler.setFormatter(_formatter)
_info_logger.addHandler(_console_handler)
_info_logger.setLevel(logging.INFO)


def run_command_with_no_shell(*, command: str) -> str:
    """
    Run the specified command without using a shell.

    Parameters
    ----------
    command : str
        The command to run.

    Returns
    -------
    output : str
        The output of the command.
    """
    _info_logger.info(f"Running command: $ {command}")
    command_: list[str] = shlex.split(command)
    complete_process: sp.CompletedProcess = sp.run(
        command_,
        stdout=sp.PIPE,
        stderr=sp.STDOUT,
    )
    output: str = complete_process.stdout.decode()
    output = output.strip()
    print(output)
    return output


def print_message(*, message: str) -> None:
    """
    Print a message with a timestamp.

    Parameters
    ----------
    message : str
        The message to print.
    """
    _info_logger.info(message)
