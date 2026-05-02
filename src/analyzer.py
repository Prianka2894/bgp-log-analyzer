def analyze_logs(parsed_logs, peers):
    down_peers = set()
    recovered_peers = set()
    error_count = {}

    for log in parsed_logs:
        ip = log.get("ip")
        message = log["message"]
        level = log["level"]

        if not ip or ip not in peers:
            continue

        if level == "ERROR":
            down_peers.add(ip)
            error_count[ip] = error_count.get(ip, 0) + 1

        if "up" in message.lower():
            recovered_peers.add(ip)
            if ip in down_peers:
                down_peers.remove(ip)

    return down_peers, recovered_peers, error_count


def classify_incident(down_peers, peers):
    if len(down_peers) == 0:
        return "No issues"
    elif len(down_peers) < len(peers):
        return "High Severity Incident"
    else:
        return "OUTAGE"
