import io
import sys
from unittest.mock import patch, Mock
import pytest

from calculator import main, arguments, eprint


@pytest.fixture(autouse=True)
def reset_arguments():
    arguments.clear()
    yield
    arguments.clear()


@patch("builtins.input", side_effect=io.StringIO("").readline)
def test_empty_input(mock_input, capfd):
    main()
    captured = capfd.readouterr()
    assert captured.out.strip() == "0"
    mock_input.assert_called_once()


@patch("builtins.input", side_effect=io.StringIO("1 2 3\n4 5\n").readline)
def test_valid_integers(mock_input, capfd):
    main()
    captured = capfd.readouterr()
    assert captured.out.strip() == "15"
    assert not captured.err.strip()


@patch("builtins.input", side_effect=io.StringIO("10 20 30\n").readline)
def test_valid_integers_single_line(mock_input, capfd):
    main()
    captured = capfd.readouterr()
    assert captured.out.strip() == "60"
    assert not captured.err.strip()


@patch("builtins.input", side_effect=io.StringIO("1 abc 2 3.5 def\n4 5\n").readline)
def test_invalid_arguments(mock_input, capfd):
    main()
    captured = capfd.readouterr()
    assert captured.out.strip() == "12"
    stderr_lines = captured.err.strip().split("\n")
    assert len(stderr_lines) == 3
    assert any("abc" in line for line in stderr_lines)
    assert any("3.5" in line for line in stderr_lines)
    assert any("def" in line for line in stderr_lines)


@patch("builtins.input", side_effect=io.StringIO("foo 1 bar 2\n3\n").readline)
def test_mixed_valid_invalid(mock_input, capfd):
    main()
    captured = capfd.readouterr()
    assert captured.out.strip() == "6"
    stderr_lines = captured.err.strip().split("\n")
    assert any("foo" in line for line in stderr_lines)
    assert any("bar" in line for line in stderr_lines)
