import re

LOG_PATTERN = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)"
IP_PATTERN = r"\d+\.\d+\.\d+\.\d+"

def parse_line(line):
    match = re.search(LOG_PATTERN, line)
    if not match:
        return None

    return {
        "date": match.group(1),
        "time": match.group(2),
        "level": match.group(3),
        "message": match.group(4),
    }

def extract_ip(message):
    ip_match = re.search(IP_PATTERN, message)
    return ip_match.group() if ip_match else None
