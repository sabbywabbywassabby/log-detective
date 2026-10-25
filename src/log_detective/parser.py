def parse_log_line(line):
    parts = line.split("|")

    if len(parts) != 3:
        raise ValueError("Invalid log format: expected 3 fields")

    timestamp = parts[0].strip()
    ip = parts[1].strip()
    status = parts[2].strip()

    if status not in ("LOGIN_SUCCESS", "LOGIN_FAILED"):
        raise ValueError("Invalid login status")

    return {
        "timestamp": timestamp,
        "ip": ip,
        "status": status
    }