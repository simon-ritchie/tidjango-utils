"""Command-related utilities and definitions.
"""

import shlex
import subprocess as sp


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
    command_: list[str] = shlex.split(command)
    complete_process: sp.CompletedProcess = sp.run(
        command_, stdout=sp.PIPE, stderr=sp.STDOUT,
    )
    output: str = complete_process.stdout.decode()
    output = output.strip()
    return output
