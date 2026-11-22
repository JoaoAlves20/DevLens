"""Command-line entry point.

Day 1 only ships the skeleton (``--version``). The ``analyze`` command arrives on Day 2.
"""

from typing import Annotated

import typer
from rich.console import Console

from devlens import __version__

app = typer.Typer(
    name="devlens",
    help="Static engineering analysis for code repositories.",
    no_args_is_help=True,
    add_completion=False,
)
console = Console()


def _version_callback(value: bool) -> None:
    if value:
        console.print(f"devlens {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            "-V",
            help="Show the DevLens version and exit.",
            callback=_version_callback,
            is_eager=True,
        ),
    ] = False,
) -> None:
    """DevLens analyzes a repository and produces a technical report."""


@app.command()
def info() -> None:
    """Show what this DevLens build can do (placeholder until the engine lands)."""
    console.print(f"[bold]DevLens[/bold] {__version__}")
    console.print("Engine not available yet - see the roadmap in README.md.")
