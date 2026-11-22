from typer.testing import CliRunner

from devlens import __version__
from devlens.cli import app

runner = CliRunner()


def test_version_flag_prints_version() -> None:
    result = runner.invoke(app, ["--version"])

    assert result.exit_code == 0
    assert __version__ in result.output


def test_no_args_shows_help() -> None:
    result = runner.invoke(app, [])

    assert "Usage" in result.output


def test_info_command_runs() -> None:
    result = runner.invoke(app, ["info"])

    assert result.exit_code == 0
    assert "DevLens" in result.output
