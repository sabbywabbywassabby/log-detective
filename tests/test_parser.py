import pytest

from log_detective.parser import parse_log_line


def test_parse_log_line():
    line = "2026-10-25 14:30:01 | 192.0.2.10 | LOGIN_FAILED"

    result = parse_log_line(line)

    assert result["timestamp"] == "2026-10-25 14:30:01"
    assert result["ip"] == "192.0.2.10"
    assert result["status"] == "LOGIN_FAILED"


def test_parse_invalid_log_line():
    line = "2026-10-25 14:30:01 | 192.0.2.10"

    with pytest.raises(ValueError):
        parse_log_line(line)

def test_parse_invalid_status():
    line = "2026-10-25 14:30:01 | 192.0.2.10 | UNKNOWN"

    with pytest.raises(ValueError):
        parse_log_line(line)